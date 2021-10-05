def Assassin():
    {
        #No olvidar Cameo de Guimpel

        #Leer archivo de jugadores, guardarlos en una lista de tuplas: Lista_Jugadores[]
        #Cada Jugador es una tupla de forma (NOMBRE,EDAD,CIUDAD)

        #Leer archivo de Distancias, guardalas en listas: Lista_distancias[]
        #Cada distancia es una tupla de forma (CIUDAD 1, CIUDAD 2, Distancia)
        
        #Tomar N (distancia en la que se puede asesinar)

        #Separar a los jugadores por edad
        #Quedarian 2 Listas de jugadores, Lista_J_Mayores, Lista_J_Menores

        #Comienza el torneo con la lista de mayores 
        #Torneo(Lista_J_Mayores, Lista_Distancias)
        
        #Se muestra la lista de ganadores

        #Torneo de menores
        #Torneo(Lista_J_Menores, Lista_Distancias)

        #Se muestra la lista de ganadores

    }

def Torneo(Lista_jugadores,Lista_distancias):
    {
        #Hacer Una lista tuplas del tipo  (Ciudad,Lista de jugadores de esa ciudad) y separar a la lista_jugadores por ciudad

        #Armar una lista de tuplas de jugadores enfrentamientos por ciudad del tipo (Jugador1,Jugador2)
        #Cuando un jugador es elegido para enfrentamiento se elimina de la lista

        #Armar enfrentamientos por jugadores cercanos y añadirlos a la lista de enfrentamientos

        #Se realizan los enfrentamiento, se escribe en el archivo quien elimino a quien
        #Se vuelven a añadir los ganadores a la lista de ciudades

        #Se repite hasta que no sean posibles mas enfrentamientos

        #Devuelve la lista de ganadores
    }