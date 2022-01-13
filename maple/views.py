from rest_framework import viewsets

from maple.models import Character
from maple.serializers import CharacterSerializer


class MapleViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer