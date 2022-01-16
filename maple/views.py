from rest_framework import viewsets

from maple.models import Character
from maple.serializers import CharacterSerializer


class MapleViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(job__icontains=query)

        return qs

