from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

# Imports of all child card classes are necessary
# for the 'eval' function in 'def card_type_cards'
from .models import Card, MonsterCard, SpellCard, TrapCard
from .serializers import CardPolymorphicSerializer


class CardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cards to be viewed or edited.
    """
    queryset = Card.objects.all()
    serializer_class = CardPolymorphicSerializer

    @list_route()
    def card_type_cards(self, request, card_type=None):
        try:
            queryset = Card.objects.instance_of(eval('%sCard' % card_type.title()))
        except NameError:
            queryset = Card.objects.all()
        return Response(self.get_serializer(queryset, many=True).data)
