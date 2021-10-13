#!/usr/bin/python
# Authors: Jordi Sola, Alan Hergenreder
# Last update: 12/10/2021

from src.asesino import *


# Variables para testear

juan = ("Juan",20,"Egipto")
pablo = ("Pablo",15,"Chile")
pedro = ("Pedro",17,"Egipto")
delmira = ("Delmira",51,"Argentina")
maria = ("Maria",23,"Chile")

lista_mixta =   [juan,
                pablo,
                pedro,
                delmira,
                maria,]
    
lista_menores = [pablo
                ,pedro]

lista_mayores = [juan
                ,delmira
                ,maria]


def test_separarListaEdad():
    assert separarListaEdad([]) == ([],[])
    assert separarListaEdad(lista_mayores) == (lista_mayores,[])
    assert separarListaEdad(lista_menores) == ([],lista_menores)
    assert separarListaEdad(lista_mixta) == (lista_mayores,lista_menores)


def test_dividirPorRegion():
    assert dividirPorRegion([]) == []
    assert dividirPorRegion(lista_mixta) == [[juan,pedro]
                                            ,[pablo,maria]
                                            ,[delmira]]


def test_jugadorMasCercano():
    assert jugadorMasCercano(lista_mixta, [1,4,5,2,6], 0) == ("",0,"")
    assert jugadorMasCercano(lista_mixta, [1,4,0,2,6], 10) == lista_mixta[2]
    assert jugadorMasCercano(lista_mixta, [1,1,5,2,6], 10) == lista_mixta[0]

def test_emparejamientoPorRegion():
    assert emparejamientoPorRegion([]) == ([],[])
    resultado = emparejamientoPorRegion([[juan,pedro]])
    assert resultado == ([(juan,pedro)],[]) or resultado == ([(pedro,juan)],[])


# Las demas funciones son poco eficientes de testear ya que, o bien manipulan
# archivos, o los escriben. 
