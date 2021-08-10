from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/search>", views.search, name="search"),
    path("wiki/new_page", views.new_page, name="new_page"),
    path("wiki/random", views.random_entry, name="random_entry"),
    path("wiki/<str:title>", views.display_entry, name="display_entry"),
    path("wiki/edit_entry/<str:title>", views.edit_entry, name="edit_entry"),
]
