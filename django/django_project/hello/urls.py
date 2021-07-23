from django.urls import path
from . import views #form current directory import views.py

urlpatterns = [
    path("", views.index, name="index"),
    path("mama", views.mama, name="mama"),
    path("menna", views.menna, name="menna"),
    path("<str:name>", views.hello_pepole, name="hello_pepole")
]
