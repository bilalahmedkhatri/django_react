from rest_framework.serializers import ModelSerializer
from .models import App5Notes


class App5NotesSerializer(ModelSerializer):
    class Meta:
        model = App5Notes
        fields = '__all__' 