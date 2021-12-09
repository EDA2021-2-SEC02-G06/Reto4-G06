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
from DISClib.ADT import list as lt
from DISClib.DataStructures import mapentry as me
"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def init():

    analyzer = model.newAnalyzer()
    return analyzer

# Funciones para la carga de datos

def loadServicesDir(cont, routesfile,citiesfile, airportfile):

    routesfile = cf.data_dir + routesfile
    input_file1 = csv.DictReader(open(routesfile, encoding = "utf-8"),
                                    delimiter=",")
    
    airportfile = cf.data_dir + airportfile
    input_file2 = csv.DictReader(open(airportfile, encoding = "utf-8"),
                                    delimiter=",")
    
    citiesfile = cf.data_dir + citiesfile
    file_cities = csv.DictReader(open(citiesfile, encoding = "utf-8"),
                                    delimiter=",")

    input_file3 = csv.DictReader(open(airportfile, encoding = "utf-8"),
                                    delimiter=",")
    
    input_file4 = csv.DictReader(open(airportfile, encoding = "utf-8"),
                                    delimiter=",")
    
    for airport in input_file3:

        if airport is not None and not(mp.contains(cont["airport"],airport["City"])):

            lista = lt.newList(datastructure="ARRAY_LIST")
            diccionario = {"nombre":airport["City"],
                            "ciudad":airport["City"],
                            "pais":airport["Country"],
                            "IATA":airport["IATA"],
                            "latitud":airport["Latitude"],
                            "longitud":airport["Longitude"],
                        }
            lt.addLast(lista, diccionario)            
            mp.put(cont["airport"],airport["City"],lista)
        else:

            a = mp.get(cont["airport"],airport["City"])
            lista1 = me.getValue(a)
            diccionario = {"nombre":airport["Name"],
                            "ciudad":airport["City"],
                            "pais":airport["Country"],
                            "IATA":airport["IATA"],
                            "latitud":airport["Latitude"],
                            "longitud":airport["Longitude"],
                        }
            lt.addLast(lista1, diccionario)
            mp.put(cont["airport"],airport["City"], lista1)

    for airport in input_file4:

        if airport is not None and not(mp.contains(cont["Iata"],airport["IATA"])):

            
            diccionario = {"nombre":airport["City"],
                            "ciudad":airport["City"],
                            "pais":airport["Country"],
                            "IATA":airport["IATA"],
                            "latitud":airport["Latitude"],
                            "longitud":airport["Longitude"],
                        }
          
            mp.put(cont["Iata"],airport["IATA"], diccionario)
            """
        else:

            a = mp.get(cont["Iata"],airport["IATA"])
            lista1 = me.getValue(a)
            diccionario = {"nombre":airport["Name"],
                            "ciudad":airport["City"],
                            "pais":airport["Country"],
                            "IATA":airport["IATA"],
                            "latitud":airport["Latitude"],
                            "longitud":airport["Longitude"],
                        }
            lt.addLast(lista1, diccionario)
            mp.put(cont["Iata"],airport["IATA"], lista1)
    """
    for citie in file_cities:

        if citie is not None and not(mp.contains(cont["ciudades"], citie["city_ascii"])):

            lista = lt.newList(datastructure="ARRAY_LIST")
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
            lt.addLast(lista,diccionario)            
            mp.put(cont["ciudades"],citie["city_ascii"],lista)
        else:

            a = mp.get(cont["ciudades"],citie["city_ascii"])
            lista1 = me.getValue(a)
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
            lt.addLast(lista1, diccionario)
            mp.put(cont["ciudades"],citie["city_ascii"],lista1)
            


    for air in input_file2:

        if air is not None:

            airport = air["IATA"]

            model.addStopDir(cont, airport)


    for route in input_file1:

        if route is not None:

            departure = route["Departure"]
            destination = route["Destination"]
            distance = float(route["distance_km"])
            sameroute = departure == destination

            if not sameroute:

                model.addConnectionDir(cont, departure, destination, distance)

    

    return cont

def loadServicesNoDir(cont, routesfile):

    routesfile = cf.data_dir + routesfile
    input_file = csv.DictReader(open(routesfile, encoding = "utf-8"),
                                    delimiter=",")

    for route in input_file:

        if route is not None:

            departure = route["Departure"]
            destination = route["Destination"]
            distance = float(route["distance_km"])
            sameroute = departure == destination

            if not sameroute:

                model.loadServicesNoDir(cont, departure, destination, distance)

    return cont     



    """
    routesfile = cf.data_dir + routesfile
    input_file = csv.DictReader(open(routesfile, encoding = "utf-8"),
                                    delimiter=",")


    for route in input_file:

        if route is not None:

            departure = route["Departure"]
            destination = route["Destination"]
            distance = route["distance_km"]
            sameroute = departure == destination


            for route1 in input_file:

                departure1 = route1["Departure"]
                destination1 = route1["Destination"]
                distance1 = route1["distance_km"]
                sameroute1 = departure1 == destination1    


                if departure == destination1:
                    print(departure)
                    if destination == departure1:
                        print(destination)

                        model.addStopConnection(cont, departure, destination, distance)

    return cont
"""
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo








































































































































































































def CuantasConexionesTiene(graf_dir):

    return model.CuantasConexionesTiene(graf_dir)


def CaminoCortoCiudades(origen, destino, graf_dir):

    return model.CaminoCortoCiudades(origen, destino, graf_dir)


def EncontrarAeropuertoIda(origen_final, hash_aero):

    return model.EncontrarAeropuertoIda(origen_final, hash_aero)

def EncontrarAeropuertoReg(destino_final, hash_aero):

    return model.EncontrarAeropuertoReg(destino_final, hash_aero)

def MstPrim(graf_nodir, ciudad_org, hash_ae):

    return model.MstPrim(graf_nodir, ciudad_org, hash_ae)

def DistanciaHaverse(aeropuerto_ida, aeropuerto_reg, destino_final, origen_final, hash_aero):

    return model.DistanciaHaverse(aeropuerto_ida, aeropuerto_reg, destino_final, origen_final, hash_aero)

def SaberConectados(graf_dir, inicio):

    return model.SaberConectados(graf_dir, inicio)

def CuantosAfectados(graf_dir, inicio):

    return model.CuantosAfectados(graf_dir, inicio)

def RecorridoReq4(lista_recorrido, graf_dir):

    return model.RecorridoReq4(lista_recorrido, graf_dir)
