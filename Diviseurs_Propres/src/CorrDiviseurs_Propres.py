#!/usr/bin/python3
# -*- coding: utf-8 -*-


def diviseurs_propres(entier):
    """
    @pre entier est un nombre entier
    @post retourne une liste contenant les diviseurs propres x,
          triés par ordre décroissant et complétée par le nombre de diviseurs propres
    """
    liste = []
    nombre = 0
    for i in range(2, entier):
        if entier%i == 0:
            liste.append(i)
            nombre += 1
    liste.sort()
    liste.reverse()
    liste.append(nombre)
    return liste

