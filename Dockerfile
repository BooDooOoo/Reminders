FROM python:3.8

WORKDIR /usr/src/Reminders

COPY ./requirements.txt /usr/src/Reminders/requirements.txt

RUN pip install -r /usr/src/Reminders/requirements.txt

COPY ./manage.py /usr/src/Reminders/manage.py
COPY ./Reminders /usr/src/Reminders/Reminders
COPY ./board /usr/src/Reminders/board
COPY ./templates /usr/src/Reminders/templates

COPY ./local_settings.py /usr/src/Reminders/local_settings.py


EXPOSE 8000

ENV TZ Europe/Moscow
