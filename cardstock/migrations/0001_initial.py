# Generated by Django 2.2.1 on 2019-05-30 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('Monster', 'Monster'), ('Spell', 'Spell'), ('Trap', 'Trap')], max_length=7)),
                ('rarity', models.CharField(choices=[('Common', 'Common'), ('Rare', 'Rare'), ('Starfoil', 'Starfoil'), ('Super Rare', 'Super Rare'), ('Ultra Rare', 'Ultra Rare'), ('Secret Rare', 'Secret Rare')], max_length=15)),
            ],
        ),
    ]
