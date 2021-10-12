#!/usr/bin/python
# Authors: Jordi Sola, Alan Hergenreder
# Last update: 12/10/2021

"""
Espacio para explicar como hicimos todo :D

Preguntas para Guimpel:
¿Los argumentos que se pasan como script al programa cuentan como variables globales?

En caso de que se de un enfrentamiento entre jugadores de diferentes regiones,
¿deberia haber preferencia por distancia objetiva (general) entre todos los jugadores?

¿Como se hace para que el programa ejecute el main directamente sin llamarlo?

¿Esta bien abusar del hecho de que en el estilo imperativo podemos devolver muchas cosas
con una sola funcion?

¿Como es la signatura de las excepciones? (clases, buscar: ErrorParametros)
¿Como es la signatura de los diccionarios?
¿Como es la signatura de los archivos abiertos?

¿Deberiamos haber separado las funciones en distintos archivos como haciamos en C?
Me refiero a usar un archivo para la signatura, otro para la definicion, y otro para usar todo.

¿Se puede modificar la forma en que un lenguaje esta hecho? 
Me refiero a romper las reglas de sintaxis que son evaluadas, o definir otras nuevas.

¿Esta al tanto de que tranquilamente deberia haber googleado todas estas preguntas
pero decidi dejarlas para que me responda?

¿Alguna vez jugo este mismo juego en la vida real?

¿Me recomienda algun libro para leer? (me quede sin preguntas jaja)

#-----------------------------------#
# Representacion de la informacion: #
#-----------------------------------#

Representamos las distancias entre regiones con una tupla (o tripla) de la siguiente forma:

Distancia == (String, String, Float)

Donde:
La primera componente representa el nombre de una region.
La segunda componente representa el nombre de una region.
La tercera componente representa la distancia entre ambas regiones. 
(¿Unidad? Kilometros, milimetros, codos)

Para facilitar el acceso a las distancias entre regiones
creamos un diccionario anidado de la siguiente forma:

DiccionarioDistancias == {String: {String: Float}}

Donde:
La clave del primer diccionario representa una region.
El valor que corresponde a dicha clave es un segundo diccionario.
La clave del segundo diccionario representa una region.
El valor asociado a este segundo diccionario es la distancia entre
la primera y segunda region.


Representamos a cada jugador con una tupla (o tripla) de la siguiente forma:

Jugador == (String,Int,String)

Donde:
La primera componente representa el nombre del jugador.
La segunda componente representa la edad del jugador.
La tercera componente representa la region del jugador.


Representamos una pareja de jugadores con una tupla (o dupla) de la siguiente forma:

Pareja == (Jugador, Jugador)

Donde:
Ya sabemos que representa jajaja.


#---------#
# Errores #
#---------#

Si, si lo se, no hay ni un solo test, esta mal, esta horrible y seguro nos va a dar con un caño
cuando vea que no testeamos ni una sola de las funciones, pero con algo de esfuerzo
quiza llegue a testear todo mañana en la mañana antes de la consulta.

Hay un error por el cual si el N ingresado es muy alto (1000) los enfrentamientos
continuan hasta que no hay jugadores. El ulitmo jugador se enfrenta a si mismo y se suicida.

Hay que corregir la signatura de los archivo_resultado, no son string, no se que son.

Decidimos esto y aquello, tambien esta otra cosa.


blablabla
blabla
blabla bla bla

blablablabla


#----------#
# Opcional #
#----------#

Agregar una ruleta rusa aleatoria para generar muertes de diferentes tipos entre los participantes.
Si te la queres re volar, permiti que se ingrese un tercer archivo que sea armas.txt o muertes.txt
para que se seleccione aleatoriamente desde esa fuente.

Agregar una mencion honorifica para el jugador que mate a Guimpel, o un
rastro de las victimas de Guimpel, o un festejo si Guimpel gana el juego.

"""




#----------#
# Modulos: #
#----------#

import sys
import random

def main():

	#------------------#
	# Datos de entrada #
	#------------------#

	# Validamos los archivos que se toman como parametro
	validarDatos()
	archivo_jugadores = sys.argv[1]
	archivo_distancias = sys.argv[2]

	# Pedimos el parametro n para saber la maxima distancia a la que se da un enfrentamiento.
	n = parametroN()


	#------------#
	# Distancias #
	#------------#


	# Creamos una lista con las distancias entre cada region.
	lista_distancias = crearListaDistancias(archivo_distancias)

	# Creamos un diccionario de diccionarios con las distancias entre cada provincia.
	diccionario_distancias = crearDiccionarioDistancias(lista_distancias)


	#-----------#
	# Jugadores #
	#-----------#

	# Creamos una lista con todos los jugadores.
	lista_jugadores_total = crearListaJugadores(archivo_jugadores)

    # Dividimos la lista en dos, mayores por un lado y menores por el otro.
	listas_separadas_edad = separarListaEdad(lista_jugadores_total)

	lista_jugadores_mayores = listas_separadas_edad[0]

	lista_jugadores_menores = listas_separadas_edad[1]

	# Dividimos las listas de jugadores en sublistas por region
	lista_jugadores_mayores_region = dividirPorRegion(lista_jugadores_mayores)

	lista_jugadores_menores_region = dividirPorRegion(lista_jugadores_menores)


	#----------------------#
	# Desarrollo del juego #
	#----------------------#

	print("El juego se esta llevando acabo, por favor espere...")

	# Creamos el archivo resultado del juego.
	archivo_resultado = open("juego_del_asesino.txt","w")

	# Juego de los mayores.
	archivo_resultado.write("Mayores de edad\n\n")
	lista_ganadores_mayores = juegoDelAsesino(lista_jugadores_mayores_region, diccionario_distancias, n, archivo_resultado)
	mencionGanadores(lista_ganadores_mayores, archivo_resultado)

	# Juego de los menoes.
	archivo_resultado.write("\n\nMenores de edad\n\n")
	lista_ganadores_menores = juegoDelAsesino(lista_jugadores_menores_region, diccionario_distancias, n, archivo_resultado)
	mencionGanadores(lista_ganadores_menores, archivo_resultado)


	# Una vez que el juego termina, cerramos el archivo.
	archivo_resultado.close()

	# Avisamos que el archivo resultado fue escrito.
	print("Se creo el archivo juego_del_asesino.txt")

	# Arbitrario
	return 0


#-------------#
# Excepciones #
#-------------#

# No se como se hace la signatura de este tipo de cosas.

class ErrorParametros(Exception):
    # Error al pasar una cantidad de parametros diferente de la esperada.
    def __init__(self, message="Los parametros esperados son: <archivo_jugadores> <archivo_distancias>"):
        self.message = message
        super().__init__(self.message)


#-----------#
# Funciones #
#-----------#


# validarDatos: None -> None
# Evalua si la cantidad de argumentos pasados al programa son correctos.
# En caso de que no lo sean, genera una excepcion.
def validarDatos():
    if len(sys.argv) != 3:
        raise ErrorParametros


# parametroN: None -> Int
# DEVUELVE un entero ingresado por teclado que representa
# la maxima distancia a la que puede realizarse un enfrentamiento entre regiones.
def parametroN():
	desicion = ""
	while desicion != "1":
		n = int(input("Ingrese la distancia maxima a la que puede producirse un enfrentamiento: "))
		desicion = input("El numero ingresado sera: " + str(n) + " ¿Esta seguro?\n[1] Si.\n[2] No.\n" )
	return n


# dividirPorRegion: List[Jugador] -> List[List[Jugador]]
# TOMA una lista de jugadores.
# DEVUELVE una lista de listas de jugadores donde cada sublista contiene
# jugadores de la misma region.
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


# crearListaDistancias: String -> List[Distancias]
# TOMA un string que representa el nombre del archivo de distancias.
# DEVUELVE una lista de tuplas que indican la distancia
def crearListaDistancias(archivo_distancias):
	
	lista_distancias = []
	archivo = open(archivo_distancias, "r+")
	for linea in archivo:
		
		# Separamos los datos
		datos = linea.split(", ")

		# Eliminamos el \n
		datos[2] = datos[2][:-1]
		
		lista_distancias += [(datos[0],datos[1],float(datos[2]))]
	
	# Cerramos el archivo porque no lo necesitamos mas.
	archivo.close()

	# Devolvemos la lista de distancias.
	return lista_distancias


# crearDiccionarioDistancias: List[Distancia] -> DiccionarioDistancias
# TOMA una lista de distancias
# DEVUELVE un diccionario anidado con las distancias entre regiones.
def crearDiccionarioDistancias(lista_distancias):
	
	lista_diccionarios = []
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


# juegoDelAsesino: Lista[Jugador] DiccionarioDistancias Int String -> List[Jugador]
# TOMA una lista de jugadores, un diccionario de distancias, una maxima distancia y
# el nombre del archivo resultante.
# DEVUELVE una lista que representa los ganadores del juego. 
def juegoDelAsesino(Lista_de_jugadores,Diccionario_de_distancias,n,archivo):

	final = True
	iterador = 0
	while (final):
		Turno_parte_1 = emparejamientoPorRegion(Lista_de_jugadores)
		lista_de_parejas = Turno_parte_1[0]
		Turno_parte_2 = emparejamientoSobrantes(Turno_parte_1[1],Diccionario_de_distancias,n)
		lista_de_parejas += Turno_parte_2[0]
		if lista_de_parejas == []:
			final = False
		lista_sobrevivientes = combate(lista_de_parejas,archivo)
		lista_sobrevivientes += Turno_parte_2[1]
		Lista_de_jugadores = dividirPorRegion(lista_sobrevivientes)
		iterador += 1
	return lista_sobrevivientes


# combate: List[Pareja] String -> List[Jugadores]
# TOMA una lista de parejas de jugadores y el nombre del archivo donde se anotaran las jugadas.
# DEVUELVE la lista de los jugadores que ganaron en dicha ronda.
def combate(lista_parejas, archivo_resultado):
    lista_ganadores = []
    for pareja in lista_parejas:
        
        # Decidimos aleatoriamente quien gana y consecuentemente quien pierde.
        ganador = random.randrange(2)
        perdedor = 1 - ganador
        lista_ganadores += [pareja[ganador]]

        archivo_resultado.write(pareja[ganador][0] + " elimino a " + pareja[perdedor][0] + "\n")
    return lista_ganadores        


# emparejamientoPorRegion: List[List[Jugadores]] -> (List[Pareja], List[Jugador])
# TOMA una lista de listas jugadores.
# DEVUELVE una tupla con una lista de parejas, y una lista de jugadores que quedaron sin pareja.
def emparejamientoPorRegion(lista_jugadores):

	lista_de_parejas = []
	jugadores_sobrantes = []
	for ciudad in lista_jugadores:
		while (len(ciudad) > 1):
			jugador_1 = ciudad[random.randrange(len(ciudad))]
			ciudad.remove(jugador_1)
			jugador_2 = ciudad[random.randrange(len(ciudad))]
			ciudad.remove(jugador_2)
			lista_de_parejas += [(jugador_1,jugador_2)]
		if(len(ciudad) == 1):
			jugadores_sobrantes += ciudad

	return (lista_de_parejas,jugadores_sobrantes)


# emparejamientoSobrantes: List[Jugador] DiccionarioDistancias Int -> (List[Pareja], List[Jugador])
# TOMA una lista de jugadores.
# DEVUELVE una tupla con una lista de parejas, y una lista de jugadores que quedaron sin pareja.
def emparejamientoSobrantes(lista_jugadores_sobrantes, diccionario_distancias, n):

	lista_parejas = []
	sobrantes_de_las_sobras = []
	cantidad_jugadores = len(lista_jugadores_sobrantes)  
	while cantidad_jugadores > 1:
		
		# Elegimos uno y lo sacamos
		eleccion_1 = lista_jugadores_sobrantes[random.randrange(cantidad_jugadores)]
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

	return (lista_parejas, sobrantes_de_las_sobras)


# preferenciaDistancias: Jugador List[Jugador] DiccionarioDistancias
# Toma un jugador objetivo, una lista de jugadores y un diccionario de distancias.
# Devuelve una lista con las distancias de cada jugador al objetivo.
def preferenciaDistancias(objetivo, lista_jugadores, diccionario_distancias):

	lista_distancias = []

	for jugador in lista_jugadores:
		
		if objetivo[2] in diccionario_distancias:
			if jugador[2] in diccionario_distancias[objetivo[2]]:
				lista_distancias += [diccionario_distancias[objetivo[2]][jugador[2]]]
			else:
				lista_distancias += [diccionario_distancias[jugador[2]][objetivo[2]]]
		else:
			lista_distancias += [diccionario_distancias[jugador[2]][objetivo[2]]]

	return lista_distancias		


# jugadorMasCercano: List[Jugador] List[Int] Int -> Int || Jugador
# TOMA una lista de jugadores, una lista de enteros que representan distancias
# y una distancia maxima posible.
# EVALUA si la menor distancia de la lista es menor o igual que la maxima distancia posible.
# Si esto ocurre, devuelve el jugador correspondiente a dicha distancia.
# Si no, devuelve un entero (0), representando que no tiene candidato.
def jugadorMasCercano(lista_jugadores, lista_distancias, n):
	
	candidato = 0
	menor_distancia = min(lista_distancias)
	indice_menor_distancia = lista_distancias.index(menor_distancia)
	jugador_mas_cercano = lista_jugadores[indice_menor_distancia]
	if menor_distancia <= n:
		candidato = jugador_mas_cercano
	return candidato



# separarListaEdad: Lista[Jugadores] -> (Lista[Jugadores],Lista[Jugadores])
# TOMA una lista de jugadores.
# DEVUELVE una tupla con una lista de jugadores mayores de edad, y otra lista
# con jugadores menores de edad.
def separarListaEdad(lista):
	listas_separadas = ([],[])
	for jugador in lista:
		if jugador[1] >= 18:
			listas_separadas[0].append(jugador)
		else:
			listas_separadas[1].append(jugador)
	return listas_separadas


# crearListaJugadores: String -> Lista[Jugadores]
# TOMA un string que representa el nombre del archivo 
# que contiene la informacion sobre los jugadores.
# DEVUEVLE una lista de jugadores.
def crearListaJugadores(archivo_jugadores):
    
	# Abrimos el archivo.
    archivo = open(archivo_jugadores,"r+")
    # Creamos la lista que vamos a devolver.
    lista_jugadores = []

    # Recorremos el archivo por lineas.
    for linea in archivo:
        
        # Los datos del jugador estan separados por comas.
        jugador = linea.split(",")
        
        # Guardamos el nombre.
        nombre = jugador[0]
        
        # Guardamos la edad.
        edad = int(jugador[1])
        
        # Guardamos la ciudad sin el ultimo caracter que es una nueva linea '\n'
        ciudad = jugador[2][:-1]
        
        # Creamos una tupla que contiene los datos de cada jugador y la almacenamos en la lista.
        lista_jugadores += [(nombre,edad,ciudad)]
    
    # Cerramos el archivo.
    archivo.close()

	# Devolvemos la lista de jugadores.
    return lista_jugadores


# mencionGanadores: List[Jugador] -> None
# TOMA una lista de jugadores y un archivo donde se escribira su mencion.
def mencionGanadores(lista_jugadores, archivo_resultado):
	archivo_resultado.write("\n\nLos siguientes jugadores ganaron en su region:\n\n")
	for jugador in lista_jugadores:
		archivo_resultado.write(jugador[0] + ", ")

main()