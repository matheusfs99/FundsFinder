from api.serializers import FundoImobiliarioSerializer
from rest_framework import viewsets, permissions
from api.models import FundoImobiliario


class FundoImobiliárioViewSet(viewsets.ModelViewSet):
    queryset = FundoImobiliario.objects.all() #  Configura o queryset base para ser utilizado pela API
    serializer_class = FundoImobiliarioSerializer # Configura qual Serializer deversá ser usado para consumir dados que chegam à API e produzir dados que serão enviados como resposta.
    permission_classes = [permissions.IsAuthenticated] # Lista contendo as permissões necessárias para acessar o endpoint exposto por essa ViewSet. Nesse caso, irá permitir apenas o acesso a usuários autenticados.
