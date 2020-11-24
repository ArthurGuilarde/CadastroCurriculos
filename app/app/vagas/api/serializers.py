from app.vagas.models import Vaga
from rest_framework import serializers

# Serializers define the API representation.
class VagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaga
        fields = '__all__'
