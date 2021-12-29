from rest_framework.serializers import ModelSerializer
from .models import App3Model

class App3Serializer(ModelSerializer):
    class Meta:
        model = App3Model
        fields = '__all__'

