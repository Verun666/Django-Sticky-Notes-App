from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_note, name="add_note"),
    path("view/<int:post_id>/", views.view_note, name="view_note"),
    path("edit/<int:post_id>/", views.edit_note, name="edit_note"),
    path("delete/<int:post_id>/", views.delete_note, name="delete_note")
]
