from django.urls import path

from .views import getNotes, testApi, getNote

urlpatterns = [
    path("", testApi, name="testapi"),
    path("notes/", getNotes, name="notes"),
    path("notes/<str:pk>", getNote, name="note"),
]