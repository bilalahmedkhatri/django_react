from django.urls import path
from .views import App4views

urlpatterns = [
    path('app4notes/', App4views, name='app 4 notes'),
]