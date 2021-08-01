from django.urls import path
from . import views #form current directory import views.py

app_name='hello' #to reference urls of the app in the templates

urlpatterns = [
    path("", views.index, name="index"),
    path("mama", views.mama, name="mama"),
    path("menna", views.menna, name="menna"),
    path("<str:name>", views.hello_pepole, name="hello_pepole")
]
