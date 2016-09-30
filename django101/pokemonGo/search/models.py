from django.db import models

# Create your models here.

class Pokedex(models.Model):
    pokemon_name = models.CharField(max_length=128, unique=True)
    pokemon_type = models.CharField(max_length=128)
    pokemon_image = models.CharField(max_length=128)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.pokemon_name

class Scoreboard(models.Model):
	user_number=models.CharField(max_length=128,unique=True)
	total_score = models.CharField(max_length=128)

	def __unicode__(self):
		return self.total_score
