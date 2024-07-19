from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = "kitchen_sink"

urlpatterns = [
    path("", views.home, name="home"),
]
