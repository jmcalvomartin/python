<h1>DataScience Incendios de Australia</h1>
En esta practica se nos pide un estudio de Analisis de Datos sobre los ultimos incendios producidos en Australia. Se nos facilita un Dataset donde debemos realziar los siguientes puntos.

<h4>Cargar el DataSet</h4>

* Cargar el DataSet
* Realizar un estudio de DataCleaning
    * Localizar valores nulos
    * Despreciar valores (si lo consideras oportuno)
    * Creación de Variables Dummies
* Guardar el Dataset "Limpio" con otro nombre para identificarlo
* Estudio de los Datos mediante gráficos (Los gráficos deben estar explicados y bien etiquetados) 
    * Histograma
    * Barras
    * Grafico de Puntos
* Filtra Dataset por los datos necesarios para el estudio (según vuestro criterio como analistas)
* Mostrar los datos usando un Mapa Gráfico
    * Usar marcación de puntos mediante Cluster
    
<h5>Columnas</h5>

* Latitude: Center of 1km fire pixel but not necessarily the actual location of the fire as one or more fires can be detected within the 1km pixel.

* Longitude: Center of 1km fire pixel but not necessarily the actual location of the fire as one or more fires can be detected within the 1km pixel.

* Brightness temperature 21 (Kelvin): Channel 21/22 brightness temperature of the fire pixel measured in Kelvin.

* Scan pixel size: The algorithm produces 1km fire pixels but MODIS pixels get bigger toward the edge of scan. Scan and track reflect actual pixel size.

* Track pixel size: The algorithm produces 1km fire pixels but MODIS pixels get bigger toward the edge of scan. Scan and track reflect actual pixel size.

* Acquisition Date: Date of MODIS acquisition.

* Acquisition Time: Time of acquisition/overpass of the satellite (in UTC).

* Satellite: A = Aqua and T = Terra.

* Instrument: Constant value for MODIS.

* Confidence (0-100%): This value is based on a collection of intermediate algorithm quantities used in the detection process. It is intended to help users gauge the quality of individual hotspot/fire pixels. Confidence estimates range between 0 and 100% and are assigned one of the three fire classes (low-confidence fire, nominal-confidence fire, or high-confidence fire).

* Version (Collection and source): Version identifies the collection (e.g. MODIS Collection 6) and source of data processing: Near Real-Time (NRT suffix added to collection) or Standard Processing (collection only). "6.0NRT" - Collection 6 NRT processing. "6.0" - Collection 6 Standard processing. Find out more on collections and on the differences between FIRMS data sourced from LANCE FIRMS and University of Maryland.

* Brightness temperature 31 (Kelvin): Channel 31 brightness temperature of the fire pixel measured in Kelvin.

* Fire Radiative Power: Depicts the pixel-integrated fire radiative power in MW (megawatts).

* Day / Night: D = Daytime, N = Nighttime
