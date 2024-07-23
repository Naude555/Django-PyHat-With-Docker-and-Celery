from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from .tasks import test_redis_q


def home(request):
    test_redis_q.delay("Redis recieved message")
    return render(request, "home.html")
