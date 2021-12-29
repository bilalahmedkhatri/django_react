from django.urls import path
from .views import App3Notes

urlpatterns = [
    path('app3notes/', App3Notes, name="app 3 notes"),
]