from django.shortcuts import render, redirect
from .models import Equipo, Jugador, Estadio, Posicion
from .forms import FormJugador, FormEquipo, FormPosicion, FormEstadio

# Create your views here.

def index(request):
	context = {
		"lista": [1,2,3,4,5],
	}
	return render(request, "NFLP/index.html", context)

def agregarJugador(request):
	form = FormJugador(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return redirect('NFLP_app:jugadores')
	else:
		form = FormJugador()
		context = {
			"form": form
		}
		return render(request, "NFLP/agregarJugador.html", context)

def agregarEquipo(request):
	form = FormEquipo(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return redirect('NFLP_app:equipos')
	else:
		form = FormEquipo()
		context = {
			"form": form
		}
		return render(request, "NFLP/agregarEquipo.html", context)

def agregarPosicion(request):
	form = FormPosicion(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return redirect('NFLP_app:posiciones')
	else:
		form = FormPosicion()
		context = {
			"form": form
		}
		return render(request, "NFLP/agregarPosicion.html", context)

def agregarEstadio(request):
	form = FormEstadio(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return redirect('NFLP_app:estadios')
	else:
		form = FormEstadio()
		context = {
			"form": form
		}
		return render(request, "NFLP/agregarEstadio.html", context)

def jugadores(request):
	queryset1 = Jugador.objects.all()
	context = {
		"objects": queryset1
	}

	return render(request, "NFLP/jugadores.html", context)

def posiciones(request):
	querysetposicion = Posicion.objects.all()
	context = {
		"objects": querysetposicion
	}

	return render(request, "NFLP/posiciones.html", context)

def listaJP(request, posicion):
	querysetlistaJP = Jugador.objects.filter(posicion=posicion)
	context = {
		"objects": querysetlistaJP
	}

	return render(request, "NFLP/listaJP.html", context)

def detalles_jugadores(request):
	queryset11 = Jugador.objects.all()
	context = {
		"objects": queryset11
	}

	return render(request, "NFLP/detalle_jugador.html", context)

def porjugador(request, nombre):
	querysetporjugador = Jugador.objects.filter(nombre=nombre)
	context = {
		"objects": querysetporjugador
	}

	return render(request, "NFLP/porjugador.html", context)

def equipos(request):
	queryset2 = Equipo.objects.all()
	context = {
		"objects": queryset2
	}

	return render(request, "NFLP/equipos.html", context)

def detalleequipo(request, equipo):
	queryset22 = Jugador.objects.filter(equipo=equipo)
	context = {
		"objects": queryset22
	}

	return render(request, "NFLP/detalleequipo.html", context)

def detalleEq(request):
	querysetEq = Equipo.objects.all()
	context = {
		"objects": querysetEq
	}

	return render(request, "NFLP/detalleEq.html", context)

def detalleEs(request):
	querysetEs = Estadio.objects.all()
	context = {
		"objects": querysetEs
	}

	return render(request, "NFLP/detalleEs.html", context)

def detalleJu(request):
	querysetJu = Jugador.objects.all()
	context = {
		"objects": querysetJu
	}

	return render(request, "NFLP/detalleJu.html", context)

def estadios(request):
	queryset3 = Estadio.objects.all()
	context = {
		"objects": queryset3
	}

	return render(request, "NFLP/estadios.html", context)

def detalles_estadios(request):
	queryset33 = Estadio.objects.all()
	context = {
		"objects": queryset33
	}

	return render(request, "NFLP/detalle_estadio.html", context)
'''
def listaExentos(request):
	context = {
		"nombre": ["Marc Albrand","Juan Gomez","Fernando Palencia"],
		"equipo": ["Exentos","Exentos","Exentos"]
	}

	return render(request, "NFLP/listaExentos.html", context)

def listaMortales(request):
	context = {
		"nombre": ["Sofia Vergara","Christian Benitez","Homero Simpson"],
		"equipo": ["Mortales","Mortales","Mortales"]
	}

	return render(request, "NFLP/listaMortales.html", context)

def listaPythoners(request):
	context = {
		"nombre": ["Angel Palencia","Georgina Corrales","Juan Esmeraldo"],
		"equipo": ["Pythoners","Pythoners","Pythoners"]
	}

	return render(request, "NFLP/listaPythoners.html", context)

def listaDjangueros(request):
	context = {
		"nombre": ["Lolita Fernandez","Carlos Gomez","Francisco Bernal"],
		"equipo": ["Djangueros","Djangueros","Djangueros"]
	}

	return render(request, "NFLP/listaDjangueros.html", context)

def listaMariscal(request):
	context = {
		"nombre": ["Lolita Fernandez","Carlos Gomez","Francisco Bernal"],
	}

	return render(request, "NFLP/listaMariscal.html", context)

def listaCorredor(request):
	context = {
		"nombre": ["Angel Palencia","Georgina Corrales","Juan Esmeraldo"],
	}

	return render(request, "NFLP/listaCorredor.html", context)

def listaCornerBack(request):
	context = {
		"nombre": ["Sofia Vergara","Christian Benitez","Homero Simpson"],
	}

	return render(request, "NFLP/listaCornerBack.html", context)

def listaSafetie(request):
	context = {
		"nombre": ["Marc Albrand","Juan Gomez","Fernando Palencia"],
	}

	return render(request, "NFLP/listaSafetie.html", context)
'''