def Assassin():
        #No olvidar Cameo de Guimpel

        #Leer archivo de jugadores, guardarlos en una lista de tuplas: Lista_Jugadores[]
        #Cada Jugador es una tupla de forma (NOMBRE,EDAD,CIUDAD)
        lista_jugadores_total = crear_lista_jugadores()

        #Leer archivo de Distancias, guardalas en listas: Lista_distancias[]
        lista_ciudades_distancia = crear_lista_ciudades()
        
        #Cada distancia es una tupla de forma (CIUDAD 1, CIUDAD 2, Distancia)
        
        #Tomar N (distancia en la que se puede asesinar)

        Lista_J_Mayores = crear_lista_mayores(lista_jugadores_total)

        Lista_J_Menores = crear_lista_menores(lista_jugadores_total)

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

def crear_lista_jugadores():
    f = open("jugadores.txt","r+")
    lista_res = []
    for x in f.readline():
        datos = x.split(",")
        nombre = datos[0]
        edad = int(datos[1])
        ciudad = datos[2]
        lista_res += [(nombre,edad,ciudad)]
    f.close()
    return lista_res

def crear_lista_ciudades():
    f = open("distancias.txt","r+")
    lista_res = []
    for x in f.readline():
        datos = x.split(",")
        ciudad1 = datos[0]
        ciudad2 = datos[1]
        distancia = int(datos[2])
        lista_res += [(ciudad1,ciudad2,distancia)]
    f.close()
    return lista_res
