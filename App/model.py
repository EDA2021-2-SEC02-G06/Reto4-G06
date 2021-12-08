"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

from DISClib.Algorithms.Graphs import dijsktra as dj
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT.graph import gr
from DISClib.Utils import error
from DISClib.Algorithms.Graphs import prim as pr 
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newAnalyzer():

    try:

        analyzer = {
                    "paradas": None,
                    "conexiones": None,
                    "conexiones_nodir": None
                    }
        
        analyzer["paradas"] = mp.newMap(numelements = 14000,
                                        maptype = "PROBING",
                                        comparefunction = compareStopIds)
        
        analyzer["conexiones_dir"] = gr.newGraph(datastructure = "ADJ_LIST",
                                            directed = True,
                                            size = 10000,
                                            comparefunction = compareStopIds)
        
        analyzer["conexiones_nodir"] = gr.newGraph(datastructure = "ADJ_LIST",
                                            directed = False,
                                            size = 500,
                                            comparefunction = compareStopIds)
        analyzer["ciudades"] = mp.newMap(41120,maptype="Probing",loadfactor=0.8,comparefunction=None)

        analyzer["airport"] = mp.newMap(41120,maptype="Probing",loadfactor=0.8,comparefunction=None)
        return analyzer
    
    except Exception as exp:

        error.rearise(exp, "model:newAnalyzer")

# Funciones para agregar informacion al catalogo

def addStopDir(cont, airport):

    try: 
        if not gr.containsVertex(cont["conexiones_dir"], airport):
            gr.insertVertex(cont["conexiones_dir"], airport)
        
        return cont
    
    except Exception as exp:
        error.rearise(exp, "model:AddStop")

def addConnectionDir(cont, departure, destination, distance):

    edge = gr.getEdge(cont["conexiones_dir"], departure, destination)
    if edge is None:
        gr.addEdge(cont["conexiones_dir"], departure, destination, distance)

    return cont

def addStopConnection(cont, departure, destination, distance):

    try:

        addStop(cont, departure)
        addStop(cont, destination)
        addConnection(cont, departure, destination, distance)
        return cont
    
    except Exception as exp:
        error.rearise(exp, "model.addStopConnection") 



# Funciones para creacion de datos

def loadServicesNoDir(cont, departure, destination, distance):

    edge = gr.getEdge(cont["conexiones_dir"], departure, destination)

    edge1 = gr.getEdge(cont["conexiones_dir"], destination, departure)  

    if edge is not None and edge1 is not None:

        if not gr.containsVertex(cont["conexiones_nodir"], departure):
            gr.insertVertex(cont["conexiones_nodir"], departure)

        if not gr.containsVertex(cont["conexiones_nodir"], destination):
            gr.insertVertex(cont["conexiones_nodir"], destination)

        
        gr.addEdge(cont["conexiones_nodir"], departure, destination, distance)

    return cont



def addConnection(cont, origin, destiny, distance):

    edge = gr.getEdge(cont["conexiones_nodir"], origin, destiny)
    if edge is None:
        gr.addEdge(cont["conexiones_nodir"], origin, destiny, distance)
    return cont

def addStop(cont, stopid):

    try: 
        if not gr.containsVertex(cont["conexiones_nodir"], stopid):
            gr.insertVertex(cont["conexiones_nodir"], stopid)
        
        return cont
    
    except Exception as exp:
        error.rearise(exp, "model:AddStop")

# Funciones de consulta

def formatVertex(service):

    name = service 
    return name
    

# Funciones utilizadas para comparar elementos dentro de una lista

def compareStopIds(stop, keyvaluestop):

    stopcode = keyvaluestop['key']
    if (stop == stopcode):
        return 0
    elif (stop > stopcode):
        return 1
    else:
        return -1

# Funciones de ordenamiento






































































































def CaminoCortoCiudades(origen, destino, graf_dir):

    search = dj.Dijkstra(graf_dir, origen)
    path = dj.pathTo(search, destino)

    return path

def EncontrarAeropuertoIda(origen_final, hash_aero):

    lista_for = mp.keySet(hash_aero)

    lim_min_lat = float(origen_final["lat"]) - 0.1
    lim_max_lat = float(origen_final["lat"]) + 0.1
    lim_max_long = float(origen_final["long"]) + 0.1
    lim_min_long = float(origen_final["long"]) - 0.1

    aeropuerto = ""

    while aeropuerto == "":

        for element in lt.iterator(lista_for):
                
            o = mp.get(hash_aero, element)["value"]
            for e in lt.iterator(o):

                if float(e["latitud"]) <= lim_max_lat and float(e["latitud"]) >= lim_min_lat and float(e["longitud"]) <= lim_max_long and float(e["longitud"]) >= lim_min_long:
                    print(1)
                    aeropuerto = e["IATA"] 

        lim_min_lat =  lim_min_lat - 0.1
        lim_max_lat = lim_max_lat + 0.1
        lim_max_long = lim_max_long + 0.1
        lim_min_long = lim_min_long - 0.1

    return aeropuerto

def EncontrarAeropuertoReg(destino_final, hash_aero):

    lista_for = mp.keySet(hash_aero)

    lim_min_lat = float(destino_final["lat"]) - 0.1
    lim_max_lat = float(destino_final["lat"]) + 0.1
    lim_max_long = float(destino_final["long"]) + 0.1
    lim_min_long = float(destino_final["long"]) - 0.1

    aeropuerto = ""

    while aeropuerto == "":

        for element in lt.iterator(lista_for):
                
            o = mp.get(hash_aero, element)["value"]
            for e in lt.iterator(o):

                if float(e["latitud"]) <= lim_max_lat and float(e["latitud"]) >= lim_min_lat and float(e["longitud"]) <= lim_max_long and float(e["longitud"]) >= lim_min_long:
                    print(1)
                    aeropuerto = e["IATA"] 

        lim_min_lat =  lim_min_lat - 0.1
        lim_max_lat = lim_max_lat + 0.1
        lim_max_long = lim_max_long + 0.1
        lim_min_long = lim_min_long - 0.1

    return aeropuerto

def DistanciaHaverse(aeropuerto_ida, aeropuerto_reg, destino_final, origen_final, hash_aero):

    lat_co = origen_final["lat"]
    long_co = origen_final["long"]
    lat_cd =  destino_final["lat"]
    long_cd =  destino_final["long"]

    o = mp.get(hash_aero, origen_final["nom"])["value"]
    
    lat_ao = 0
    long_ao = 0
    lat_ad =  0
    long_ad =  0

    for e in lt.iterator(o):

        if e["IATA"] == aeropuerto_ida:

            lat_ao = float(e["latitud"])
            long_ao = float(e["longitud"])
        
        elif e["IATA"] == aeropuerto_reg:

            lat_ao = float(e["latitud"])
            long_ao = float(e["longitud"])

    a = 0

def MstPrim(graf_dir, ciudad_org):

    pr.PrimMST
