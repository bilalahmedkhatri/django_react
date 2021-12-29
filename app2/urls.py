from django.urls import path
from .views import app2Notes

urlpatterns = [
    path('appnotes/', app2Notes, name="app 2 notes"),
]