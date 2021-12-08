"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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

#from DISClib.ADT.indexminpq import contains
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from App import controller
assert cf
import threading
from DISClib.ADT import stack
from DISClib.ADT.graph import gr
from DISClib.ADT import map as mp
from geopy import distance 


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("\n")
    print("***********************************************************************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar informacion de los aeropuertos e imprimir los vertices")
    print("3- REQ1: Encontrar puntos de interconexión aerea")
    print("4- REQ2: Encontrar clusteres de trafico aereo")
    print("5- REQ3: Encontrar la ruta más corta entre ciudades")
    print("6- REQ4: Utilizar las millas de viajero")
    print("7- REQ5: Cuantificar el efectod e un aeropuerto cerrado")
    print("8- REQ6 (Bono): Comparar con servicio WEB externo")
    print("0- Fin del programa")

airportfile = "airports-utf8-small.csv"
routesfile = "routes-utf8-small.csv"
citiesfile = "worldcities-utf8.csv"
initial = None

"""
Menu principal
"""
def thread_cycle():
    while True:
        printMenu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs[0]) == 1:
            print("\nInicializando. . . . .")
            cont = controller.init()


        elif int(inputs[0]) == 2:
            print("\nCargando información del transporte aereo. . . . .")
            trey = controller.loadServicesDir(cont, routesfile,citiesfile, airportfile)
            treo = controller.loadServicesNoDir(cont, routesfile)
            graf_dir = treo["conexiones_dir"]
            graf_nodir = trey["conexiones_nodir"]
            tamaño_dir = gr.numVertices(graf_dir)
            tamaño_nodir = gr.numVertices(graf_nodir)
            lista_dir = graf_dir["vertices"]
            lista_nodir = graf_nodir["vertices"]
            print("---------------------------------------------------------------")
            print("Información del digrafo:")
            print("El numero de aeropuertos en el grafo dirigido es de: " + str(tamaño_dir))
            print("El numero total de rutas aereas son: " + str(gr.numEdges(graf_dir)))
            print("primer aeropuerto cargado")
            print("----------------------------------------------------------------")
            print("Información del grafo no dirigido:")
            print("El numero de aeropuertos en el grafo no dirigido es de: " + str(tamaño_nodir))
            print("El numero de rutas aereas son: " + str(gr.numEdges(graf_nodir)))
            print("primer aeropuerto cargado")
            print("-----------------------------------------------------------------")
            print("Información ciudades:")
            print("total ciudades")
            print("ultimaciudad")

        
        elif int(inputs[0]) == 3:
            pass

        elif int(inputs[0]) == 4:
            pass

        elif int(inputs[0]) == 5:
            ciudad_origen = input("Ingrese la ciudad de origen: ")
            ciudad_destino = input("Ingrese la ciudad de destino: ")

            
            ciudades = cont["ciudades"]
            valor_ciudad_origen = None

            if mp.contains(ciudades, ciudad_origen):
                valor_ciudad_origen = mp.get(ciudades, ciudad_origen)["value"]

            print("Las ciudades disponibles son: ")
            
            s = 1
            lista_city = lt.newList("ARRAY_LIST")
            for elemento in lt.iterator(valor_ciudad_origen):

                print(str(s) + " -- " + elemento["nombre"] + " " + elemento["pais"] + " " + elemento["admin"] + " " + " latitud: " +  elemento["latitud"] + " " + "longitud: " + elemento["longitud"])
                dic = {"nom": elemento["nombre"], "lat": elemento["latitud"], "long": elemento["longitud"]}
                lt.addLast(lista_city, dic)
                s += 1
            
            origen = int(input("\nEscoja y escriba el numero de la ciudad de partida: "))
            origen = origen - 1

            k = 0
            for city in lt.iterator(lista_city):
                if k == origen:
                    origen_final = city
                
                k += 1

            
            valor_ciudad_destino = None

            if mp.contains(ciudades, ciudad_destino):
                valor_ciudad_destino = mp.get(ciudades, ciudad_destino)["value"]

            print("-----------------------------------------------------------------")
            print("Ciudades de llegada disponibles: ")
            
            ss = 1
            lista_city2 = lt.newList("ARRAY_LIST")
            for elemento in lt.iterator(valor_ciudad_destino):

                print(str(ss) + " -- " + elemento["nombre"] + " " + elemento["pais"] + " " + elemento["admin"] + " " + " latitud: " +  elemento["latitud"] + " " + "longitud: " + elemento["longitud"])
                dic = {"nom": elemento["nombre"], "lat": elemento["latitud"], "long": elemento["longitud"]}
                lt.addLast(lista_city2, dic)
                ss += 1
            
            destino = int(input("\nEscoja y escriba el numero de la ciudad de partida: "))

            destino = destino - 1

            kk = 0
            for city in lt.iterator(lista_city2):
                if kk == destino:
                    destino_final = city
                
                kk += 1 

            hash_aero = cont["airport"]

            aeropuerto_ida = controller.EncontrarAeropuertoIda(origen_final, hash_aero)
            aeropuerto_reg = controller.EncontrarAeropuertoReg(destino_final, hash_aero)
            print(aeropuerto_ida)
            print(aeropuerto_reg)

            camino = controller.CaminoCortoCiudades(aeropuerto_ida, aeropuerto_reg, graf_dir)
            if camino == None:
                print("No hay ruta que lo conecte")
            else:
                print("El aeropuerto de salida es: " + aeropuerto_ida)
                print("El aeropuerto de llegada es: " + aeropuerto_reg)
                print("")
                print("********************************************")
                print("")
                print("La ruta es: ")
                for ruta in lt.iterator(camino):

                    print("Air Salida: " + ruta["vertexA"] + "  --->  " + "Air Llegada: " + ruta["vertexB"] + " Distancia: " + str(ruta["weight"]))
                    print("--------------------------------------------------------------------------------------")
                print("")
                print("********************************************")
                print("")
                print("La distancia total es: ")
                hash_city = cont["ciudades"]
                distancia_t = controller.DistanciaHaverse(aeropuerto_ida, aeropuerto_reg, destino_final, origen_final, hash_aero)
                distancia_a = 0
                for ruta in lt.iterator(camino):
                    distancia_a += ruta["weight"]
                distancia_fin = distancia_a + distancia_t
                print("La distancia total de la ruta entre " + ciudad_origen + " y " + ciudad_destino + " es de: " + str(distancia_fin))

        elif int(inputs[0]) == 6:
            
            ciudad_org = input("Cual es la ciudad de origen: ")
            millas = int(input("Cuantas millas posee: "))

            distancia_millas = millas * 1.6

            mst = controller.MstPrim(graf_dir, ciudad_org)

        elif int(inputs[0]) == 7:
            pass

        elif int(inputs[0]) == 8:
            pass

        elif int(inputs[0]) == 0:
            pass

        else:
            sys.exit(0)
    sys.exit(0)


if __name__ == "__main__":
    threading.stack_size(67108864)  # 64MB stack
    sys.setrecursionlimit(2 ** 20)
    thread = threading.Thread(target=thread_cycle)
    thread.start()

