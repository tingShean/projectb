#!/bin/bash

# Prepare log files and start outputting logs to stdout
mkdir -p /code/logs
touch /code/logs/gunicorn.log
touch /code/logs/gunicorn-access.log
tail -n 0 -f /code/logs/gunicorn*.log &

export DJANGO_SETTINGS_MODULE=projectb.settings

exec gunicorn projectb:application \
	--name breakfast \
	--bind 0.0.0.0:8000 \
	--worker-class gevent \
	--workers 3 \
	--timeout 60 \
	--log-level=debug \
	--log-file=/code/logs/gunicorn.log \
	--access-logfile=/code/logs/gunicorn-access.log \
"$@"
