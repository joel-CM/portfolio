#|/usr/bin/bash

NAME="portfolio"
DJANGODIR=$(dirname $(cd `dirname $0` && pwd))
SOCKFILE=/tmp/gunicorn-portfolio.sock
LOGDIR=/home/joel/logs/gunicorn-portfolio.log
USER=joel
GROUP=joel
NUM_WORKERS=3
DJANGO_WSGI_MODULE=portfolio.wsgi

rm -frv $SOCKFILE

echo $DJANGODIR

cd $DJANGODIR

exec ${DJANGODIR}/venv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=$LOGDIR