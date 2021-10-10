#!/usr/bin/python
# Authors: Jordi Sola, Alan Hergenreder
# Last update: 09/10/2021


# Modulos:
import sys


# Excepciones
class ErrorParametros(Exception):
    # Error al pasar una cantidad de parametros diferente de la esperada.
    def __init__(self, message="Los parametros esperados son: <archivo_jugadores> <archivo_distancias>"):
        self.message = message
        super().__init__(self.message)

def main():

	# Validamos los archivos que se toman como parametro
	validarDatos()
	archivo_jugadores = sys.argv[1]
	archivo_distancias = sys.argv[2]

	n = parametroN()

	# Creamos una lista con todos los jugadores.
	lista_jugadores_total = crearListaJugadores(archivo_jugadores)

	# Creamos un diccionario de diccionarios con las distancias entre cada provincia.
	diccionario_distancias = crearDiccionarioDistancias(archivo_distancias)
	
	# Ejemplo de como funciona este diccionario.
	# Calculando la distancia entre Buenos Aires y Rosario:
	print(diccionario_distancias["CABA"]["Rosario"])


    # Dividimos la lista en dos, mayores por un lado y menores por el otro.

	listas_separadas_edad = separarListaEdad(lista_jugadores_total)

	lista_jugadores_mayores = listas_separadas_edad[0]

	lista_jugadores_menores = listas_separadas_edad[1]

	# Ahora ya tenemos lo necesario para empezar un torneo, creo.

	# Salida
	return 0

def validarDatos():
    if not parametrosArchivos():
        raise ErrorParametros


def parametroN():
	desicion = ""
	while desicion != "1":
		n = int(input("Ingrese la distancia maxima a la que puede producirse un enfrentamiento: "))
		desicion = input("El numero ingresado sera: " + str(n) + " ¿Esta seguro?\n[1] Si.\n[2] No.\n" )
	return n


def parametrosArchivos():
    argumentos_evaluados = True
    if len(sys.argv) != 3:
        argumentos_evaluados = False
    return argumentos_evaluados


def crearDiccionarioDistancias(archivo_distancias):
	lista_distancias = []
	lista_diccionarios = []
	archivo = open(archivo_distancias, "r+")
	for linea in archivo:
		
		# Separamos los datos
		datos = linea.split(", ")

		# Eliminamos el \n
		datos[2] = datos[2][:-1]
		
		lista_distancias += [(datos[0],datos[1],float(datos[2]))]
	
	# Cerramos el archivo porque no lo necesitamos mas.
	archivo.close()

	provincia = ""
	# Empieza en -1 ya que la primera vez que se ejecute sera siempre nuevo y seteara a 0.
	iterador = -1
	
	for distancia in lista_distancias:
		
		# Si la region no esta en la lista la agrega y crea su diccionario. 
		if provincia != distancia[0]:
			lista_diccionarios += [(distancia[0], dict([(distancia[1],distancia[2])]))]
			provincia = distancia[0]
			iterador += 1

		# Si la region ya esta en la lista, actualiza su diccionario con el nuevo valor. 
		else:
			lista_diccionarios[iterador][1].update([(distancia[1],distancia[2])])
	
	# Creamos un diccionario con los diccionarios de cada region.
	return dict(lista_diccionarios)



"""
Habría que renombrar esta funcion.
Creo que hay muchas llamadas a funciones aca, tal vez podriamos dividir las 
funciones y hacer mas cosas llamando desde el main.

Che se me fue la mano con esta funcion y queriendo sacarle un par de llamadas 
la deje vacia...

"""

def Assassin():
    #No olvidar Cameo de Guimpel

    #Leer archivo de jugadores, guardarlos en una lista de tuplas: Lista_Jugadores[]
    #Cada Jugador es una tupla de forma (NOMBRE,EDAD,CIUDAD)

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
	return 0

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


def separarListaEdad(lista):
    listas_separadas = ([],[])
    for jugador in lista:
        if jugador[1] >= 18:
            listas_separadas[0].append(jugador)
        else:
            listas_separadas[1].append(jugador)
    return listas_separadas



def crearListaJugadores(archivo_jugadores):
    # Abrimos el archivo
    archivo = open(archivo_jugadores,"r+")
    # Creamos la lista que vamos a devolver
    lista_jugadores = []

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
        lista_jugadores += [(nombre,edad,ciudad)]
    
    # Cerramos el archivo
    archivo.close()
    return lista_jugadores


"""
Comentarios sobre el codigo que solo estan para hacer presencia xdXdxD UwU

La forma que yo note mezclando la manera en la que codeamos, es:
las variables como
nombre_variable

y las funciones como
nombreFuncion()

Creo que es bastante legible, ¿que te parece?


Pregunta:
¿Deberiamos abrir el archivo resultante de texto una y otra vez a medida de que las rondas avanzan?
¿O podriamos guardar una lista con todas las jugadas y luego hacer una sola escritura?

Respuesta acordada:
Guardar un registro de las muertes con tuplas de dos elementos, la funcion torneo entonces
debe devolver dos valores, los ganadores y el registro.
Abrir una sola vez el archivo resultante y escribir todo.


Me tengo que poner a hacer la signatura de las funciones que estoy re vago.
"""


main()