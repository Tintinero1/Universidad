from django import forms

from .models import Jugador
from .models import Equipo
from .models import Estadio
from .models import Posicion

class FormJugador(forms.ModelForm):
	equipo = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	numero = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	nombre = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	posicion = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	fuerza = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	velocidad = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	resistencia = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))

	
	class Meta:
		model = Jugador
		fields = [
	
		"equipo",
		"numero",
		"nombre",
		"posicion",
		"fuerza",
		"velocidad",
		"resistencia",
		
		]


class FormEquipo(forms.ModelForm):
	equipo = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	estadio = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))

	
	class Meta:
		model = Equipo
		fields = [
	
		"equipo",
		"estadio",

		
		]


class FormEstadio(forms.ModelForm):
	estadio = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	
	class Meta:
		model = Estadio
		fields = [
	
		"estadio",

		]

class FormPosicion(forms.ModelForm):
	posicion = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	
	class Meta:
		model = Posicion
		fields = [
	
		"posicion",

		]