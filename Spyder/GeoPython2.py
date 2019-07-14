#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 21:16:48 2019

@author: jorge
"""

#Geolocalización
from geopy.geocoders import Nominatim
import time
import math


# Crear Objeto Nominatim
geolocator = Nominatim(user_agent="AppMap")#

location_lista = ["Mexico","Madrid","Paris"]

#Recorremos la lista
for i in location_lista:
    address = geolocator.geocode(i, timeout=10)
    print ("Ciudad de "+ i + " : " + str(address.longitude) + "," + str(address.latitude))
    time.sleep(1)
    