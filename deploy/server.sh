#!/bin/bash

DJANGODIR=$(dirname $(cd `dirname $0` && pwd))
DJANGO_SETTINGS_MODULE=portfolio.settings.production
source "$DJANGODIR/venv/bin/activate"
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
exec python "$DJANGODIR/manage.py" runserver 0:3001