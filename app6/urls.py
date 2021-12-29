from .views import App6Notes, App6Note
from django.urls import path
from django.views.generic import TemplateView 

urlpatterns = [
    path('app/', App6Notes, name='app6notes'),
    path('app/<str:pk>/', App6Note, name='app6note'),
    path('frontend/', TemplateView.as_view(template_name='index.html'))
]