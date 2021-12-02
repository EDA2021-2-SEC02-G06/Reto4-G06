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
 """

import config as cf
from App import model
import csv
from DISClib.ADT import map as mp

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def init():

    analyzer = model.newAnalyzer()
    return analyzer

# Funciones para la carga de datos

def loadServices(cont, routesfile,citiesfile):

    routesfile = cf.data_dir + routesfile
    input_file = csv.DictReader(open(routesfile, encoding = "utf-8"),
                                    delimiter=",")
    
    citiesfile = cf.data_dir + citiesfile
    file_cities = csv.DictReader(open(citiesfile, encoding = "utf-8"),
                                    delimiter=",")
    
    for citie in file_cities:

        if citie is not None:
            diccionario = {"nombre":citie["city_ascii"],
                            "latitud":citie["lat"],
                            "longitud":citie["lng"],
                            "pais":citie["country"],
                            "iso2":citie["iso2"],
                            "iso3":citie["iso3"],
                            "admin":citie["admin_name"],
                            "capital":citie["capital"],
                            "population":citie["population"],
                            "id":citie["id"]
            }
            
            mp.put(cont["ciudades"],citie["id"],diccionario)



    for route in input_file:

        if route is not None:

            departure = route["Departure"]
            destination = route["Destination"]
            distance = route["distance_km"]
            sameroute = departure == destination

            if not sameroute:

                model.addStopConnection(cont, departure, destination, distance)

    return cont


# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
