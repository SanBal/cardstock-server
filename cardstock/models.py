from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from polymorphic.models import PolymorphicModel


class Card(PolymorphicModel):
    RARITIES = (
        ('Common', 'Common'),
        ('Rare', 'Rare'),
        ('Starfoil', 'Starfoil'),
        ('Super Rare', 'Super Rare'),
        ('Ultra Rare', 'Ultra Rare'),
        ('Secret Rare', 'Secret Rare')
    )

    name = models.CharField(max_length=50)
    rarity = models.CharField(max_length=15, choices=RARITIES)


class MonsterCard(Card):
    TYPES = (
        ('Aqua', 'Aqua'),
        ('Dinosaurier', 'Dinosaurier'),
        ('Donner', 'Donner'),
        ('Drache', 'Drache'),
        ('Fee', 'Fee'),
        ('Fels', 'Fels'),
        ('Fisch', 'Fisch'),
        ('Göttliches Ungeheuer', 'Göttliches Ungeheuer'),
        ('Geflügeltes Ungeheuer', 'Geflügeltes Ungeheuer'),
        ('Hexer', 'Hexer'),
        ('Insekt', 'Insekt'),
        ('Krieger', 'Krieger'),
        ('Maschine', 'Maschine'),
        ('Pflanze', 'Pflanze')
    )

    level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(12)])
    atk = models.PositiveSmallIntegerField()
    defense = models.PositiveSmallIntegerField()
    type = models.CharField(max_length=20, choices=TYPES)

    def __str__(self):
        return "MonsterCard: {name: %s, type: %s, atk: %d, def: %d, rarity: %s}" % (
            self.name, self.type, self.atk, self.defense, self.rarity)


class SpellCard(Card):
    TYPES = (
        ('Ausrüstung', 'Ausrüstung'),
        ('Normal', 'Normal'),
        ('Permanent', 'Permanent'),
        ('Ritual', 'Ritual'),
        ('Schnell', 'Schnell'),
        ('Spielfeld', 'Spielfeld')
    )
    type = models.CharField(max_length=10, choices=TYPES)

    def __str__(self):
        return "SpellCard: {name: %s, type: %s, rarity: %s" % (self.name, self.type, self.rarity)


class TrapCard(Card):
    TYPES = (
        ('Konter', 'Konter'),
        ('Normal', 'Normal'),
        ('Permanent', 'Permanent'),
    )
    type = models.CharField(max_length=10, choices=TYPES)

    def __str__(self):
        return "TrapCard: {name: %s, type: %s, rarity: %s" % (self.name, self.type, self.rarity)
