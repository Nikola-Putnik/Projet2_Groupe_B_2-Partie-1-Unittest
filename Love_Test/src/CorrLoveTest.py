#!/usr/bin/python3
# -*- coding: utf-8 -*-


def love_test(jul, candidates):
    """
    @pre <à compléter>
    @post <à compléter>
    """
    best_candidates = []
    best_pourcentage = 0
    for candidate in candidates:
        nbr_caract = len(jul)-1
        caract_communes = 0
        #Age
        if candidate[1] == jul[1]:
            caract_communes += 1
        #Couleur
        if candidate[2] == jul[2]:
            caract_communes += 1
        #Chien/Chat
        if candidate[3] == jul[3]:
            caract_communes += 1
        #Série
        if candidate[4] == jul[4]:
            caract_communes += 1
        #PS/Fifa
        if candidate[5] == jul[5]:
            caract_communes += 1
        pourcentage = (caract_communes/nbr_caract)*100
        # print(candidate[0] + str(pourcentage))
        if caract_communes > 0:
            if len(best_candidates) == 0:
                best_candidates.append(candidate[0])
                best_pourcentage = pourcentage
            else:
                if pourcentage == best_pourcentage:
                    best_candidates.append(candidate[0])
                elif pourcentage > best_pourcentage:
                    best_pourcentage = pourcentage
                    best_candidates[:] = [candidate[0]]
    if best_pourcentage > 0:
        best_candidates.append(best_pourcentage)
    return best_candidates
