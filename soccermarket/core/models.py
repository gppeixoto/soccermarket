from __future__ import unicode_literals

from django.db import models

# ENUMS
POSITIONS = (
    ('GK', 'Goleiro'),
    ('RB', 'Lateral direito'),
    ('CB', 'Zagueiro'),
    ('LB', 'Lateral esquerdo'),
    ('DM', 'Volante'),
    ('CM', 'Meia central'),
    ('AM', 'Meia avancado'),
    ('RM', 'Ponta direita'),
    ('LM', 'Ponta esquerda'),
    ('CF', 'Atacante')
)
FOOTS = (
    ('R', 'Destro'),
    ('L', 'Canhoto')
)

# Create your models here.
class Person(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length = 100)
    nationality = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True

class Player(Person):
    position = models.CharField(max_length = 100, choices = POSITIONS)
    market_value = models.DecimalField(max_digits = 20, decimal_places = 2)
    dominant_foot = models.CharField(max_length = 100, choices = FOOTS)
    shirt_number = models.IntegerField(blank = True, null = True)
    agent = models.CharField(blank = True, max_length = 100, null = True)
    url_profile = models.URLField(blank = True, null = True)

    class Meta:
        verbose_name = "Jogador"
        verbose_name_plural = "Jogadores"

class Coach(Person):
    preferred_formation = models.CharField(max_length = 10)
    win_percentage = models.DecimalField(max_digits = 5, decimal_places = 2, null = True, blank = True)

    class Meta:
        verbose_name = "Treinador"
        verbose_name_plural = "Treinadores"

class Team(models.Model):
    name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    badge = models.URLField(blank = True, null = True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Time"
        verbose_name_plural = "Times"

class History(models.Model):
    player = models.ForeignKey(Player, on_delete = models.CASCADE)
    team = models.ForeignKey(Team, on_delete = models.CASCADE)

    def __unicode__(self):
        return self.player.name + " - " + self.team.name

    class Meta:
        verbose_name = "Historico"
        verbose_name_plural = "Historicos"

class Transfer(models.Model):
    player = models.ForeignKey(Player, on_delete = models.CASCADE)
    destiny = models.ForeignKey(Team, on_delete = models.CASCADE, related_name = 'team_destiny')
    origin = models.ForeignKey(Team, null = True, on_delete = models.CASCADE, related_name = 'team_origin', blank = True)
    value = models.DecimalField(null = True, max_digits = 20, decimal_places = 2, blank = True)
    date = models.DateField()

    def __unicode__(self):
        return self.origin.name + " - " + self.player.name + " - " + self.destiny.name

    class Meta:
        verbose_name = "Transferencia"
        verbose_name_plural = "Transferencia"

class Plays(models.Model):
    player = models.ForeignKey(Player, on_delete = models.CASCADE)
    team = models.ForeignKey(Team, on_delete = models.CASCADE)

    def __unicode__(self):
        return self.player.name + " - " + self.team.name

    class Meta:
        verbose_name = "Joga"
        verbose_name_plural = "Joga"

class Coaches(models.Model):
    coach = models.ForeignKey(Coach, on_delete = models.CASCADE)
    team = models.ForeignKey(Team, on_delete = models.CASCADE)

    def __unicode__(self):
        return self.coach.name + " - " + self.team.name

    class Meta:
        verbose_name = "Treina"
        verbose_name_plural = "Treina"