from rest_framework import serializers
from api.models import FundoImobiliario


class FundoImobiliarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundoImobiliario # define qual modelo esse serializer deve serializar
        fields = "__all__" # define os campos que serão serializados, no caso, todos
