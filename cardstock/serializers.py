from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer
from .models import MonsterCard, SpellCard, TrapCard


class MonsterCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonsterCard
        fields = ('id', 'name', 'rarity', 'level', 'atk', 'defense', 'type')


class SpellCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpellCard
        fields = ('id', 'name', 'rarity', 'type')


class TrapCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrapCard
        fields = ('id', 'name', 'rarity', 'type')


class CardPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        MonsterCard: MonsterCardSerializer,
        SpellCard: SpellCardSerializer,
        TrapCard: TrapCardSerializer
    }
