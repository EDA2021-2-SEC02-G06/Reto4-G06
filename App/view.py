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

airportfile = "airports_full.csv"
routesfile = "routes_full.csv"
citiesfile = "worldcities.csv"
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

            
            ciudades = cont["airport"]
            valor_ciudad_origen = None

            if mp.contains(ciudades, ciudad_origen):
                valor_ciudad_origen = mp.get(ciudades, ciudad_origen)["value"]

            print("Aeropuertos disponibles en ciudad origen: ")
            
            for elemento in lt.iterator(valor_ciudad_origen):

                print(elemento["IATA"])
                
            
            origen = input("\nEscoja y escriba el aeropuerto de partida: ")

            valor_ciudad_destino = None

            if mp.contains(ciudades, ciudad_destino):
                valor_ciudad_destino = mp.get(ciudades, ciudad_destino)["value"]

            print("-----------------------------------------------------------------")
            print("Aeropuertos disponibles en ciudad llegada: ")
            
            for elemento in lt.iterator(valor_ciudad_destino):

                print(elemento["IATA"])
                
            
            destino = input("\nEscoja y escriba el aeropuerto de llegada: ")

            
            camino = controller.CaminoCortoCiudades(origen, destino, graf_dir)
            if camino == None:
                print("No hay ruta que lo conecte")
            else:
                print(camino)


        elif int(inputs[0]) == 6:
            pass

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

