#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 21:22:57 2019

@author: jorge
"""

#Geolocalización
import geopy
import time
import math

#Dibujar mapas
from mpl_toolkits.basemap.test import Basemap
import matplotlib.pyplot as plt


geolocator = Nominatim(user_agent="AppMap")

location = geolocator.geocode("175 5th Avenue NYC")
print(location.address)

#Dimensiónd de la figura
plt.figure(figsize=(16,12))

#Distribución lines costeras
eq_map=Basemap(projection='robin',lon_0=0,lat_0=0)

#Dibujar lineas costeras y paises
eq_map.drawcoastlines()
eq_map.drawcountries()

#Definir colores
eq_map.fillcontinents(color="brown")
eq_map.drawmapboundary(fill_color="aqua")

#Situo el lugar en el mapa
x,y = eq_map(location.longitude,location.latitude)
eq_map.plot(x,y, "ro", markersize=17, alpha=0.8)

