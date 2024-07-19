#!/bin/sh

celery -A config beat -l info

exec "$@"
