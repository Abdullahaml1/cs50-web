from django.urls import path
from . import views #form current directory import views.py

urlpatterns = [
    path("", views.index, name="index")
]
