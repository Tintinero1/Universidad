from django.urls import path

from NFLP import views

app_name = "NFLP_app"

urlpatterns = [
	path('', views.index, name="index"),
	path('jugadores/', views.jugadores, name="jugadores"),
	path('porjugador/<nombre>/', views.porjugador, name="porjugador"),
	path('posiciones/', views.posiciones, name="posiciones"),
	path('listaJP/<posicion>/', views.listaJP, name="listaJP"),
	path('equipos/', views.equipos, name="equipos"),
	path('estadios/', views.estadios, name="estadios"),
	path('detalles_jugadores/', views.detalles_jugadores, name="detalles_jugadores"),
	path('detalleequipo/<equipo>/', views.detalleequipo, name="detalleequipo"),
	path('detalles_estadios/', views.detalles_estadios, name="detalles_estadios"),
	path('detalleEq/', views.detalleEq, name="detalleEq"),
	path('detalleEs/', views.detalleEs, name="detalleEs"),
	path('detalleJu/', views.detalleJu, name="detalleJu"),
	path('agregarJugador/', views.agregarJugador, name="agregarJugador"),
	path('agregarEquipo/', views.agregarEquipo, name="agregarEquipo"),
	path('agregarEstadio/', views.agregarEstadio, name="agregarEstadio"),
	path('agregarPosicion/', views.agregarPosicion, name="agregarPosicion"),


	#path('listaExentos/', views.listaExentos, name="listaExentos"),
	#path('listaMortales/', views.listaMortales, name="listaMortales"),
	#path('listaPythoners/', views.listaPythoners, name="listaPythoners"),
	#path('listaDjangueros/', views.listaDjangueros, name="listaDjangueros"),
	#path('listaCorredor/', views.listaCorredor, name="listaCorredor"),
	#path('listaMariscal/', views.listaMariscal, name="listaMariscal"),
	#path('listaSafetie/', views.listaSafetie, name="listaSafetie"),
	#path('listaCornerBack/', views.listaCornerBack, name="listaCornerBack"),
] 