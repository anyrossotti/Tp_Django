from rest_framework.viewsets import ModelViewSet
from .models import Perfil
from .serializers import PerfilSerializer

class PerfilViewSet(ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer