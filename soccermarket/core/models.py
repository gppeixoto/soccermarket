from __future__ import unicode_literals

from django.db import models

# ENUMS
POSITIONS = (
	('GK', 'Goleiro'),
	('RB', 'Lateral direito'),
	('CB', 'Zagueiro'),
	('LB', 'Lateral esquerdo'),
	('CM', 'Volante'),
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

	class Meta:
		abstract = True

class Player(Person):
	position = models.CharField(max_length = 100, choices = POSITIONS)
	market_value = models.DecimalField(max_digits = 20, decimal_places = 2)
	dominant_foot = models.CharField(max_length = 100, choices = FOOTS)
	shirt_number = models.IntegerField(blank = True, null = True)
	agent = models.CharField(blank = True, max_length = 100, null = True)
	url_profile = models.URLField(blank = True, null = True)

class Coach(Person):
	preferred_formation = models.CharField(max_length = 10)
	win_percentage = models.DecimalField(max_digits = 5, decimal_places = 2)

class Team(models.Model):
    name = models.CharField(max_length=100)
    nameCompleto = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    badge = models.ImageField(upload_to = "assets/badges")
    imagemCamisa = models.ImageField(upload_to = "assets/shirts")

class Player_History(models.Model):
	player = models.ForeignKey(Player, on_delete = models.CASCADE)
	team = models.ForeignKey(Team, on_delete = models.CASCADE)

class Coach_History(models.Model):
	coach = models.ForeignKey(Coach, on_delete = models.CASCADE)
	team = models.ForeignKey(Team, on_delete = models.CASCADE)

class Transfer(models.Model):
	player = models.ForeignKey(Player, on_delete = models.CASCADE)
	destiny = models.ForeignKey(Team, on_delete = models.CASCADE, related_name = 'team_destiny')
	origin = models.ForeignKey(Team, null = True, on_delete = models.CASCADE, related_name = 'team_origin')
	value = models.DecimalField(null = True, max_digits = 20, decimal_places = 2)
	date = models.DateField()
	is_top = models.BooleanField(default = False)

class Plays(models.Model):
	player = models.ForeignKey(Player, on_delete = models.CASCADE)
	team = models.ForeignKey(Team, on_delete = models.CASCADE)
	contract_ends = models.DateField(auto_now_add = False) 
	on_loan = models.BooleanField(default = False)
	is_capitan = models.BooleanField(default = False)

class Coaches(models.Model):
	coach = models.ForeignKey(Coach, on_delete = models.CASCADE)
	team = models.ForeignKey(Team, on_delete = models.CASCADE)
	contract_ends = models.DateField(auto_now_add = False)
	coach_term = models.DurationField()