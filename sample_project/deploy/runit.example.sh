#!/bin/sh

GUNICORN=../vtenv/bin/gunicorn
PID=/var/run/django_sample_env.pid
USER=user
APP=deploy
DIR=/path/to/application

if [ -f $PID ]; then rm $PID; fi

cd $DIR
exec sudo -H -u $USER DJANGO_MODE="development" $GUNICORN $APP
#exec sudo -H -u cyberj $GUNICORN --pid=$PID $APP
