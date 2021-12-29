from django.urls import path
from .views import app5Notes

urlpatterns = [
    path('app5notes/', app5Notes, name='app5notes')
]