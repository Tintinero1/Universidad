from django.db import models
from django.conf import settings

# Create your models here.


class Jugador(models.Model):
	equipo = models.CharField(max_length=60)
	numero = models.CharField(max_length=60)
	nombre = models.CharField(max_length=60)
	posicion = models.CharField(max_length=60)
	fuerza = models.IntegerField()
	velocidad = models.IntegerField()
	resistencia = models.IntegerField()

	def __str__(self):
		return self.nombre

class Equipo(models.Model):
	equipo = models.CharField(max_length=60)
	estadio = models.CharField(max_length=60)

	def __str__(self):
		return self.equipo


class Estadio(models.Model):
	estadio = models.CharField(max_length=60)

	def __str__(self):
		return self.estadio

class Numero(models.Model):
	numero = models.IntegerField()

	def __int__(self):
		return int(self.numero)

class Posicion(models.Model):
	posicion = models.CharField(max_length=60)

	def __str__(self):
		return self.posicion


#models.ForeignKey(
#		'Equipo', on_delete=models.CASCADE)
