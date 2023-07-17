from django.urls import path

from . import views

urlpatterns = [
    path("studysite/", views.members, name="index"),
]

#start/