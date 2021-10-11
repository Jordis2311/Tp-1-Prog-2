#!/usr/bin/python
# Authors: Jordi Sola, Alan Hergenreder
# Last update: 10/10/2021


# Modulos:
import sys
from random import *

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
	print("diccionario_distancias['CABA']['Rosario'] == ",diccionario_distancias["CABA"]["Rosario"])


    # Dividimos la lista en dos, mayores por un lado y menores por el otro.

	listas_separadas_edad = separarListaEdad(lista_jugadores_total)

	lista_jugadores_mayores = listas_separadas_edad[0]

	lista_jugadores_menores = listas_separadas_edad[1]

	# Dividimos las listas de jugadores en sublistas por region
	lista_jugadores_mayores_region = dividirPorRegion(lista_jugadores_mayores)

	lista_jugadores_menores_region = dividirPorRegion(lista_jugadores_menores)

	# Ejemplo de que las listas estan divididas por region:
	# Los primeros cuatro elementos de la primera lista, y los dos primeros de la segunda.
	print("Lo que hay en la primera lista de listas\n",lista_jugadores_mayores_region[0][:4])
	print("Lo que hay en la segunda\n", lista_jugadores_mayores_region[1][:2])


	Lista_ganadores_mayores = JuegoDelAsesino(lista_jugadores_mayores,diccionario_distancias)

	# Salida
	return 0

#validarDatos crea una excepcion para aquellos casos en donde los datos ingresados no son los correctos
def validarDatos():
    if not parametrosArchivos():
        raise ErrorParametros

#parametroN: None -> int
#parametroN nos permite el ingreso de el numero N que sera utilizado como maxima distancia para el juego, el jugador puede cabiar el numero si se arrepintio de su decision
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

#dividirPorRegion 
#dividirPorRegion toma una lista de jugadores y devuelve una lista de tuplas del tipo (Ciudad,Lista[Jugadores]) 
# en donde se encuentran todos los jugadores ingresados separados por ciudades
def dividirPorRegion(lista_jugadores):
	lista_jugadores_region = []
	iterador = 0
	regiones = {}
	for jugador in lista_jugadores:
		
		# Si ya existe una lista de dicha region, la actualiza.
		if jugador[2] in regiones:
			lista_jugadores_region[regiones[jugador[2]]].append(jugador)
		# Si no existe una lista de dicha region, la crea.
		else:
			lista_jugadores_region += [[jugador]]
			regiones.update([(jugador[2], iterador)])
			iterador += 1

	return lista_jugadores_region



"""
Esta funcion tiene dos fors, creo que es mucho,
podriamos dividirla en dos funciones que cada una tenga un solo for.

Podriamos hacer un corte donde se cierra el archivo y retornar dicha lista.
"""
#crearDiccionarioDistancias: file -> {String:{String:int}}
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


	region = ""
	# Empieza en -1 ya que la primera vez que se ejecute sera siempre nuevo y seteara a 0.
	iterador = -1
	
	for distancia in lista_distancias:
		
		# Si la region no esta en la lista la agrega y crea su diccionario. 
		if region != distancia[0]:
			lista_diccionarios += [(distancia[0], dict([(distancia[1],distancia[2])]))]
			region = distancia[0]
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
J- por lo que lei moviste todo al main asi que quedo medio inutil la funcion assassin

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

def JuegoDelAsesino(Lista_de_jugadores,Diccionario_de_distancias):
	print("UwU")
	#Crear El emparejamiento por ciudad
	#Emparejamiento = parejasPorCiudad(Lista_de_jugadores)
	#A la lista de los emparejamientos anterior unirle el resto de emparejamientos de aquellos que puedan
	#Emparejamiento += parejasSobrantes(Lista_de_jugadores)
	
def parejas_por_ciudad(Jugadores_Totales):
	lista_de_parejas = []
	jugadores_sobrantes = []
	for ciudad in Jugadores_Totales:
		while (len(ciudad) > 1):
			jugador_1 = ciudad[random.randrange(len(ciudad))]
			ciudad.remove(jugador_1)
			jugador_2 = ciudad[random.randrange(len(ciudad))]
			ciudad.remove(jugador_2)
			lista_de_parejas += [(jugador_1,jugador_2)]
		if(len(ciudad) == 1):
			jugadores_sobrantes += ciudad[0]
	return (lista_de_parejas,jugadores_sobrantes)


# volver a meter a los jugadores en su sublista   
def emparejamientosSobrantes(lista_jugadores_sobrantes, diccionario_distancias, n):
	lista_parejas = []
	sobrantes_de_las_sobras = []
	cantidad_jugadores = len(lista_jugadores_sobrantes)  
	iterador = 0 
	while cantidad_jugadores > 1:
		
		# Elegimos uno y lo sacamos
		eleccion_1 = random.randrange(cantidad_jugadores)
		cantidad_jugadores -= 1
		lista_jugadores_sobrantes.remove(eleccion_1)

		# Calculamos la distancia al resto de los jugadores.
		lista_cercanias = preferenciaDistancias(eleccion_1, lista_jugadores_sobrantes, diccionario_distancias)

		# Elegimos el candidato con la menor distancia.
		eleccion_2 = jugadorMasCercano(lista_jugadores_sobrantes, lista_cercanias, n)

		# Si el candidato es valido, lo empareja.
		if eleccion_2 != 0:
			lista_parejas += [(eleccion_1, eleccion_2)]
		
		# Sino, lo descarta.
		else:
			sobrantes_de_las_sobras += [eleccion_1]
			lista_jugadores_sobrantes.remove(eleccion_1)


		return (lista_parejas, sobrantes_de_las_sobras)


def preferenciaDistancias(objetivo, lista_jugadores, diccionario_distancias):
	lista_distancias = []
	for jugador in lista_jugadores:
		lista_distancias += [diccionario_distancias[objetivo][jugador[2]]]
	return lista_distancias		


def jugadorMasCercano(lista_jugadores, lista_distancias, n):
	candidato = 0
	menor_distancia = min(lista_distancias)
	indice_menor_distancia = lista_distancias.index(menor_distancia)
	jugador_mas_cercano = lista_jugadores.index(indice_menor_distancia)
	if menor_distancia <= n:
		candidato = jugador_mas_cercano
	return candidato



#separarListaEdad: Lista[Jugadores] -> (Lista[Jugadores],Lista[Jugadores])
# toma la lista de jugadores totales y retorna una tupla de los jugadores separados por edad
def separarListaEdad(lista):
    listas_separadas = ([],[])
    for jugador in lista:
        if jugador[1] >= 18:
            listas_separadas[0].append(jugador)
        else:
            listas_separadas[1].append(jugador)
    return listas_separadas


#crearListaJugadores: file -> Lista[Jugadores]
#Recibe el archivo que contiene a todos los jugadores y devuelve una lista de tuplas que representan a cada jugador
#Las tuplas son del formato (nombre: string,Edad: int,Ciudad: string)
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
J- Se entiende perfectamente

Pregunta:
¿Deberiamos abrir el archivo resultante de texto una y otra vez a medida de que las rondas avanzan?
J- Creo que podemos durante la funcion que determina con la lista de enfrentamientos quien gana y quien pierde, abrir el archivo al inicio de esa funcion 
y cuando se calcula cada resultado escribir quien mato a quien y al final de esa funcion cerrarlo devuelta, asi solo lo abririamos y cerrariamos 6 veces
1- para escribir juego de mayores
2- para escribir las acciones (solo necesitariamos abrila 1 vez)
3- para escribir ganadores de mayores
4- escribir juego de menores
5- escribir acciones
6- escribir ganadores

¿O podriamos guardar una lista con todas las jugadas y luego hacer una sola escritura?

Respuesta acordada:
Guardar un registro de las muertes con tuplas de dos elementos, la funcion torneo entonces
debe devolver dos valores, los ganadores y el registro.
Abrir una sola vez el archivo resultante y escribir todo.


Me tengo que poner a hacer la signatura de las funciones que estoy re vago.
"""


main()