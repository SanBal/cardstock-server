from django.db import models


class Card(models.Model):
    TYPES = (
        ('Monster', 'Monster'),
        ('Spell', 'Spell'),
        ('Trap', 'Trap')
    )
    RARITIES = (
        ('Common', 'Common'),
        ('Rare', 'Rare'),
        ('Starfoil', 'Starfoil'),
        ('Super Rare', 'Super Rare'),
        ('Ultra Rare', 'Ultra Rare'),
        ('Secret Rare', 'Secret Rare')
    )
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=7, choices=TYPES)
    rarity = models.CharField(max_length=15, choices=RARITIES)

    def __str__(self):
        return "Card: {name: %s, type: %s, rarity: %s}" % (self.name, self.type, self.type)
