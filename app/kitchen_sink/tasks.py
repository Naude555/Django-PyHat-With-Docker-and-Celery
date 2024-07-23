from celery import shared_task
import time


@shared_task
def tp(queue="celery:"):
    time.sleep(3)
    return


@shared_task
def tp1(queue="celery:1"):
    time.sleep(3)
    return


@shared_task
def tp2(queue="celery:2"):
    time.sleep(3)
    return


@shared_task
def tp3(queue="celery:3"):
    time.sleep(3)
    return


@shared_task
def test_redis_q(text):
    time.sleep(10)
    print(text)
