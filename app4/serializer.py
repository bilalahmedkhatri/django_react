from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import App4Notes

class SerializerApp4notes(ModelSerializer):
    class Meta:
        model = App4Notes
        fields = ('id', 'text_body')