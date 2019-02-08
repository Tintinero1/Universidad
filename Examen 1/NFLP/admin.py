from django.contrib import admin
from .models import Jugador, Equipo, Estadio, Posicion, Numero
# Register your models here.

admin.site.register(Jugador)
admin.site.register(Equipo)
admin.site.register(Estadio)
admin.site.register(Posicion)
admin.site.register(Numero)
'''
class JugadorAdmin(admin.ModelAdmin):
	list_display = [
		"id",
		"equipo",
		"numero",
		"nombre",
		"fuerza",
		"velocidad",
		"resistencia",
		"posicion"

	]


class AdminEquipo(admin.ModelAdmin):
	list_display = [
		"equipo",
		"estadio"

	]

class AdminEstadio(admin.ModelAdmin):
	list_display = [
		"estadio"

	]
'''