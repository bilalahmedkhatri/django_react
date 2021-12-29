from rest_framework.serializers import ModelSerializer
from ..models import App2

class appNotesSerializer(ModelSerializer):
    class Meta:
        model = App2
        fields = '__all__'