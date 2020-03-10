#!/usr/bin/python3
# -*- coding: utf-8 -*-


def reverse_word(s):
    """
    @pre:  une chaine de caractère s
    @post: la chaine de caractère s, avec les premier et dernier mots intervertis
           et les espaces inutiles supprimés
    """
    if s == "":
        return ""
    else:
        L= s.split()
        n = len(L)
        premier = L[0]
        dernier = L[n-1]
        L[0]= dernier
        L[n-1]= premier
        s=" ".join(L)
        return s
