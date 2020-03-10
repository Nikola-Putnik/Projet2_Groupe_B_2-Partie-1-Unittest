#!/usr/bin/python3
# -*- coding: utf-8 -*-


def gta(morts,policiers):
    """
    @pre:  2 entiers en arguments: un nombre de morts et un nombre de policiers parmis ceux-ci
    @post: 1 entier correspondant au nombre d'étoiles du joueur
    """
    etoiles = 0
    policier_nbre = 0
    totalIndice = 0
    if policiers >= 1:
        etoiles += 3
        policier_nbre = (policiers-1)
        morts = morts-1
        totalIndice = morts+policier_nbre
        etoiles += (totalIndice//4)
        if etoiles <= 6:
            return etoiles
        else:
            return 6
    else:
        totalIndice = morts
        etoiles = (totalIndice // 4)
        if etoiles <= 6:
            return etoiles
        else:
            return 6
