#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: jorge
"""

#Geolocalización
from geopy.geocoders import Nominatim
import time
import math


# Crear Objeto Nominatim
geolocator = Nominatim(user_agent="AppMap")

#Pasamos el lugar 
location = geolocator.geocode("175 5th Avenue NYC")
print(location.address)

#Imprimimos el lugar
print((location.latitude, location.longitude))

