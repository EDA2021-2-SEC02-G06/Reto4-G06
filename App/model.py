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


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT.graph import gr
from DISClib.Utils import error
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
                    "componentes": None,
                    "caminos": None
                    }
        
        analyzer["paradas"] = mp.newMap(numelements = 14000,
                                        maptype = "PROBING",
                                        comparefunction = compareStopIds)
        
        analyzer["conexiones"] = gr.newGraph(datastructure = "ADJ_LIST",
                                            directed = True,
                                            size = 14000,
                                            comparefunction = compareStopIds)
        
        return analyzer
    
    except Exception as exp:

        error.rearise(exp, "model:newAnalyzer")

# Funciones para agregar informacion al catalogo

def addStopConnection(cont, departure, destination, distance):

    try:
        origin = formatVertex(departure)
        destiny = formatVertex(destination)
        addStop(cont, origin)
        addStop(cont, destiny)
        addConnection(cont, origin, destiny, distance)
        return cont
    
    except Exception as exp:
        error.rearise(exp, "model.addStopConnection") 



# Funciones para creacion de datos

def addConnection(cont, origin, destiny, distance):

    edge = gr.getEdge(cont["conexiones"], origin, destiny)
    if edge is None:
        gr.addEdge(cont["conexiones"], origin, destiny, distance)
    return cont

def addStop(cont, stopid):

    try: 
        if not gr.containsVertex(cont["conexiones"], stopid):
            gr.insertVertex(cont["conexiones"], stopid)
        
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
