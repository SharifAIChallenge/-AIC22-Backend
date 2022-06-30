from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.db.models import Q
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_tracking.mixins import LoggingErrorsMixin

from team.permissions import HasTeam, IsFinalist
from .models.match import Match
from .models.submission import Submission
from .models.tournament import TournamentTypes, Tournament
from .serializers.submission import SubmissionSerializer
from .serializers.match import MatchSerializer
from .serializers.tournament import TournamentSerializer


class SubmissionsListAPIView(GenericAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = (IsAuthenticated, HasTeam)

    def get(self, request):
        data = self.get_serializer(
            self.get_queryset().filter(team=request.user.team),
            many=True).data
        return Response(data={'submissions': data}, status=status.HTTP_200_OK)


class SubmissionAPIView(LoggingErrorsMixin, GenericAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = (IsAuthenticated, HasTeam, IsFinalist)

    def get(self, request):
        data = self.get_serializer(
            self.get_queryset().filter(team=request.user.team),
            many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request):
        submission = self.get_serializer(
            data=request.data,
            context={'request': request}
        )
        if submission.is_valid(raise_exception=True):
            submission = submission.save()
            return Response(
                data={'submission_id': submission.id},
                status=status.HTTP_200_OK
            )
        return Response(
            data={'errors': 'Something Went Wrong'},
            status=status.HTTP_406_NOT_ACCEPTABLE
        )

    # def put(self, request, submission_id):
    #     submission = get_object_or_404(Submission, id=submission_id)
    #     try:
    #         submission.set_final()
    #         return Response(
    #             data={'details': 'Final submission changed successfully'},
    #             status=status.HTTP_200_OK
    #         )
    #     except ValueError as e:
    #         return Response(data={'errors': [str(e)]},
    #                         status=status.HTTP_406_NOT_ACCEPTABLE)


class TournamentAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TournamentSerializer
    queryset = Tournament.objects.filter(
        type__in=[TournamentTypes.NORMAL, TournamentTypes.FINAL]).exclude(
        start_time=None
    ).filter(is_hidden=False)

    def get(self, request):
        curr_time = timezone.now()
        queryset = self.get_queryset().order_by('id')
        data = self.get_serializer(queryset, many=True).data

        return Response(
            data={'data': data},
            status=status.HTTP_200_OK
        )


class MatchAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated, HasTeam]
    serializer_class = MatchSerializer
    queryset = Match.objects.all()
    # pagination_class = MatchPagination

    def get(self, request):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)

        data = self.get_serializer(
            instance=page,
            many=True
        ).data

        # return self.get_paginated_response(
        #     data={'data': data},
        # )
        return Response(
            data={'data': data},
            status=status.HTTP_200_OK
        )

    def get_queryset(self):
        match_status = self.request.query_params.get('status')

        tournament_id = self.request.query_params.get(
            'tournament_id',
        )
        try:
            tournament_id = int(tournament_id)
        except TypeError:
            tournament_id = None

        if not tournament_id:
            queryset = self.queryset.exclude(
                tournament__type=TournamentTypes.NORMAL)
        else:
            queryset = self.queryset.filter(
                tournament_id=tournament_id
            )

        queryset = queryset.filter(
            Q(team1=self.request.user.team) | Q(team2=self.request.user.team)
        )

        if match_status:
            queryset = queryset.filter(
                status=match_status
            )

        return queryset.order_by('-id')
