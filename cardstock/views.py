from rest_framework import viewsets
from .models import Card
from .serializers import CardPolymorphicSerializer


class CardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cards to be viewed or edited.
    """
    queryset = Card.objects.all()
    serializer_class = CardPolymorphicSerializer
