#!/bin/sh

celery --app=config worker -l INFO -Q celery,celery:1,celery:2,celery:3


exec "$@"
