#!/usr/bin/python3
# -*- coding: utf-8 -*-


def love_test(intéressé, candidates):
    """
    @pre <à compléter>
    @post <à compléter>
    """
    best_femme = []
    best_pourcentage = 0
    for femme in candidates:
        nbr_caract = len(candidat)-1
        caract_communes = 0
        #Age
        if femme[1] == candidat[1]:
            caract_communes += 1
        #Couleur
        if femme[2] == candidat[2]:
            caract_communes += 1
        #Chien/Chat
        if femme[3] == candidat[3]:
            caract_communes += 1
        #Série
        if femme[4] == candidat[4]:
            caract_communes += 1
        #PS/Fifa
        if femme[5] == candidat[5]:
            caract_communes += 1
        pourcentage = (caract_communes/nbr_caract)*100
        print(femme[0] + str(pourcentage))
        if len(best_femme) == 0:
            best_femme.append(femme[0])
            best_pourcentage = pourcentage
        else:
            if pourcentage == best_pourcentage:
                best_femme.append(femme[0])
            elif pourcentage > best_pourcentage:
                best_pourcentage = pourcentage
                best_femme[:] = [femme[0]]
    best_femme.append(best_pourcentage)
    return best_femme

