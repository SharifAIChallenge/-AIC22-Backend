from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import Staff, Tweet, Prize, PastAIC, FrequentlyAskedQuestions
from .serializers import StaffSerializer, TweetSerializer, PrizeSerializer, PastAICSerializer, FAQSerializer
from permissions import AdminWritePermission


class StaffsListViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = (AdminWritePermission, )


class TweetsListViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = (AdminWritePermission,)


class PrizesListViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    queryset = Prize.objects.all()
    serializer_class = PrizeSerializer
    permission_classes = (AdminWritePermission,)


class PastAICsListViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    queryset = PastAIC.objects.all()
    serializer_class = PastAICSerializer
    permission_classes = (AdminWritePermission,)


class FAQListViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    queryset = FrequentlyAskedQuestions.objects.all()
    serializer_class = FAQSerializer
    permission_classes = (AdminWritePermission, )
