from rest_framework import serializers
from horario.models import Horario

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'