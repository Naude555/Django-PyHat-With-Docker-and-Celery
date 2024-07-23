# pull official base image
FROM python:3.12.4-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh ./celery_entrypoint.sh ./celery_beat_entrypoint.sh ./
RUN sed -i 's/\r$//g' entrypoint.sh celery_entrypoint.sh celery_beat_entrypoint.sh
RUN chmod +x entrypoint.sh celery_entrypoint.sh celery_beat_entrypoint.sh

# copy project
COPY . /usr/src/app/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
