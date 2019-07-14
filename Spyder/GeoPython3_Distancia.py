#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 21:19:31 2019

@author: jorge
"""

#Geolocalización
import geopy
import time
import math


##Creamos función distancia para calcularla
def distancia(lugar1,lugar2):
    origen = geolocator.geocode(lugar1)
    destino = geolocator.geocode(lugar2)

    coord_origen=(origen.longitude,origen.latitude)
    coord_destino=(destino.longitude,destino.latitude)

    distancia = geopy.distance.distance(coord_origen,coord_destino)
    
    return print ("La distancia entre " + lugar1 + " y " + lugar2 + " es de " + str(distancia))

#Llamamos a la función
lugar1 = input ("Introduce ciudad de Origen: ")
lugar2 = input ("Introduce ciudad de Destino: ")
distancia(lugar1,lugar2)