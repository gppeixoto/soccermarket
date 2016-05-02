from __future__ import unicode_literals

from django.db import models

# ENUMS
POSITIONS = (
	('GK', 'Goleiro'),
	('RB', 'Lateral direito'),
	('CB', 'Zagueiro'),
	('LB', 'Lateral esquerdo'),
	('CM', 'Volante'),
	('AM', 'Meia avançado'),
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
	market_value = models.DecimalField(decimal_places = 2)
	dominant_foot = models.CharField(max_length = 100, choices = FOOTS)
	shirt_number = models.IntegerField(blank = True, max_length = 2, null = True)
	agent = models.CharField(blank = True, max_length = 100, null = True)
	url_profile = models.URLField(blank = True, null = True)