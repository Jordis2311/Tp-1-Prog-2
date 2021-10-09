#!/usr/bin/python
# Authors: Jordi Sola, Alan Hergenreder
# Last update: 09/10/2021


# Modulos:
import sys


# Excepciones
class ErrorParametros(Exception):
    #Error al pasar una cantidad de parametros diferente de la esperada.
    def __init__(self, message="Los parametros esperados son: <archivo_jugadores> <archivo_distancias>"):
        self.message = message
        super().__init__(self.message)

def main():

	# Entrada
	validarDatos()
	archivo_jugadores = sys.argv[1]
	archivo_distancias = sys.argv[2]

	# Procesamiento datos
	Assassin(archivo_jugadores, archivo_distancias)


	# Salida

	return 0
                


def validarDatos():
    if not parametrosArchivos():
        raise ErrorParametros
        

def parametrosArchivos():
    argumentos_evaluados = True
    if len(sys.argv) != 3:
        argumentos_evaluados = False
    return argumentos_evaluados


"""
Habría que renombrar esta funcion.
"""

def Assassin(archivo_jugadores, archivo_distancias):
        #No olvidar Cameo de Guimpel

        #Leer archivo de jugadores, guardarlos en una lista de tuplas: Lista_Jugadores[]
        #Cada Jugador es una tupla de forma (NOMBRE,EDAD,CIUDAD)
        lista_jugadores_total = crear_lista_jugadores(archivo_jugadores)

        print(lista_jugadores_total[:3])

        #Leer archivo de Distancias, guardalas en listas: Lista_distancias[]
        #lista_ciudades_distancia = crear_lista_ciudades()
        
        #Cada distancia es una tupla de forma (CIUDAD 1, CIUDAD 2, Distancia)
        
        #Tomar N (distancia en la que se puede asesinar)

        #Lista_J_Mayores = crear_lista_mayores(lista_jugadores_total)

        #Lista_J_Menores = crear_lista_menores(lista_jugadores_total)

        #Quedarian 2 Listas de jugadores, Lista_J_Mayores, Lista_J_Menores



        #Comienza el torneo con la lista de mayores 
        #Torneo(Lista_J_Mayores, Lista_Distancias)
        
        #Se muestra la lista de ganadores

        #Torneo de menores
        #Torneo(Lista_J_Menores, Lista_Distancias)

        #Se muestra la lista de ganadores


def Torneo(Lista_jugadores,Lista_distancias):
        #Hacer Una lista tuplas del tipo  (Ciudad,Lista de jugadores de esa ciudad) y separar a la lista_jugadores por ciudad
        print("UwU")
        #Armar una lista de tuplas de jugadores enfrentamientos por ciudad del tipo (Jugador1,Jugador2)
        #Cuando un jugador es elegido para enfrentamiento se elimina de la lista

        #Armar enfrentamientos por jugadores cercanos y añadirlos a la lista de enfrentamientos

        #Se realizan los enfrentamiento, se escribe en el archivo quien elimino a quien
        #Se vuelven a añadir los ganadores a la lista de ciudades

        #Se repite hasta que no sean posibles mas enfrentamientos

        #Devuelve la lista de ganadores
    

"""
crear_lista_mayores y crear_lista_menores difieren en una condicion, se puede colapsar en
una sola funcion, comentar y evaluar si es legible hacerlo.
"""


def crear_lista_mayores(lista):
        i = 0
        lista_res = []
        for x in lista:
                if (x[1] >= 18):
                    lista_res[i] = x
                    i+=1
        return lista_res
            
def crear_lista_menores(lista):
        i = 0
        lista_res = []
        for x in lista:
                if (x[1] < 18):
                    lista_res[i] = x
                    i+=1
        return lista_res



"""
crear_lista_jugadores y crear_lista_ciudades hace lo mismo, se puede colapsar en
una sola funcion, comentar y evaluar si es legible hacerlo.
"""

def crear_lista_jugadores(archivo_jugadores):
    # Abrimos el archivo
    archivo = open(archivo_jugadores,"r+")
    # Creamos la lista que vamos a devolver
    lista_res = []

    # Recorremos el archivo por lineas
    for linea in archivo:
        
        # Los datos del jugador estan separados por comas
        jugador = linea.split(",")
        
        # Guardamos el nombre
        nombre = jugador[0]
        
        # Guardamos la edad
        edad = int(jugador[1])
        
        # Guardamos la ciudad sin el ultimo caracter que es una nueva linea '\n'
        ciudad = jugador[2][:-1]
        
        # Creamos una tupla que contiene los datos de cada jugador y la almacenamos en la lista
        lista_res += [(nombre,edad,ciudad)]
    
    # Cerramos el archivo
    archivo.close()
    return lista_res


def crear_lista_ciudades(archivo_distancias):
    archivo = open(archivo_distancias,"r+")
    lista_res = []
    for linea in archivo.readline():
        datos = linea.split(",")
        ciudad1 = datos[0]
        ciudad2 = datos[1]
        distancia = int(datos[2])
        lista_res += [(ciudad1,ciudad2,distancia)]
    archivo.close()
    return lista_res


main()