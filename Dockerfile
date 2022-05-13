FROM reg.aichallenge.ir/python:3.8 AS base

ENV PYTHONUNBUFFERED 1
WORKDIR /app

# Set the timezone.
RUN echo "Asia/Tehran" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

RUN apt-get update

ADD requirements.txt .
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt

FROM base AS build

ENV STATIC_ROOT /app/static

COPY . /app

RUN ["./manage.py", "collectstatic", "--no-input"]

CMD ["gunicorn", "--bind=0.0.0.0:8000", "--timeout=90", "--preload", "AIC22_Backend.wsgi:application"]

FROM reg.aichallenge.ir/nginx:1.17.6 AS static

COPY --from=build /app/static /usr/share/nginx/html/static