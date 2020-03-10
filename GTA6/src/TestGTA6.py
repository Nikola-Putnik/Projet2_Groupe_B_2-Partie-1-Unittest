#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import sys

import CorrGTA6 as correct
import GTA6 as student


"""
CONSIGNES:

Grâce à vos talents d'informaticien, vous avez été engagé pour programmer une partie de GTA 6.

*Le dernier jeu d'une suite figurant parmis les plus populaires dans le monde du jeux-video.
Le joueur y incarne un personnage dans une ville avec à priori une grande liberté d'action. Néanmoins, le personnage incarné se retrouve souvent encouragé à adopter un comportement criminel se traduisant ensuite par une poursuite de la police.
Une fois poursuivi par la police, le joueur possède un indice de recherche qui se traduit par un nombre d'étoiles allant de 1 à 6 selon la gravité de ses crimes.*

Votre mission est la suivante : vous devez attribuer le nombre d'étoiles que mérite le joueur pour ses péchés...

Vous devez créer une fonction gta(morts,policiers) qui retournera le nombre d'étoiles en fonction du nombre de morts et du nombre de policiers présents parmis ceux-ci...

Cependant vous devez respecter les consignes exigées par votre supérieur :
 1) Le nombre d'étoiles est limité à 6.

 2) Le joueur obtient une étoile supplémentaire à chaque fois qu'il tue 4 personnes.

 3) Le simple fait d'avoir un policier parmis ses victimes majore son nombre d'étoiles de 3.
    Le premier policier n'est donc pas comptabilisé parmis les autres personnes du fait qu'il majore déjà le nombre d'étoiles de 3.

 4) Par la suite, la mort d'un policier compte pour autant que la mort de 2 personnes.
"""


# TESTS UNITAIRES:
# - test ISNOTNONE (le classique)
# - test avec 0 mort -> gta(0,0)
# - test avec n morts et 0 policier tué
# - test avec n morts et 1 policier tué
# - test avec n morts et 2->n policiers tués
# - test avec n morts et m policiers tués TEL QUE les étoiles dépasseraient la limite de 6



class TestGTA6(unittest.TestCase):

    # vérifie que la fonction renvoi quelque chose
    def test0_None(self):
        args = [(6,6), (8,2), (50,0), (4,0), (14,3), (20,18)]
        rep = _("Votre fonction a retourné None pour {} comme argument. Cela implique probablement qu'il manque un return dans votre code.")
        for n in args:
            try:
                student_ans = student.gta(n[0],n[1])
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, n))
            self.assertIsNotNone(student_ans, rep.format(n))

    # vérifie ce que la fonction renvoi avec: 0 mort => elle devrait renvoyer 0
    def test1_GTA6_0(self):
        args = [(0,0)]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme arguments alors que la réponse attendue est {}")
        for n in args:
            try:
                student_ans = student.gta(n[0],n[1])
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, n))
            correct_ans = correct.gta(n[0],n[1])
            self.assertEqual(student_ans, correct_ans,
                             rep.format(student_ans, n, correct_ans))

    # vérifie ce que la fonction renvoi avec: n morts et 0 policier tué
    def test2_GTA6_0Policier(self):
        args = [(1,0), (2,0), (3,0), (4,0), (5,0), (7,1), (8,0), (9,0), (11,0), (12,0), (13,0), (14,0), (21,0), (55,0), (120,0)]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme arguments alors que la réponse attendue est {}")
        for n in args:
            try:
                student_ans = student.gta(n[0],n[1])
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, n))
            correct_ans = correct.gta(n[0],n[1])
            self.assertEqual(student_ans, correct_ans,
                             rep.format(student_ans, n, correct_ans))

    # vérifie ce que la fonction renvoi avec: n morts et 1 policier tué
    def test3_GTA6_1Policier(self):
        args = [(1,1), (2,1), (3,1), (4,1), (5,1), (7,1), (8,1), (9,1), (11,1), (12,1), (13,1), (14,1), (21,1)]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme arguments alors que la réponse attendue est {}")
        for n in args:
            try:
                student_ans = student.gta(n[0],n[1])
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, n))
            correct_ans = correct.gta(n[0],n[1])
            self.assertEqual(student_ans, correct_ans,
                             rep.format(student_ans, n, correct_ans))

    # vérifie ce que la fonction renvoi avec: n morts et n policier tué (n>=2)
    def test4_GTA6_nPoliciers(self):
        args = [(1,2), (2,4), (3,5), (4,1), (5,2), (9,3), (14,2), (2,2), (3,3)]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme arguments alors que la réponse attendue est {}")
        for n in args:
            try:
                student_ans = student.gta(n[0],n[1])
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, n))
            correct_ans = correct.gta(n[0],n[1])
            self.assertEqual(student_ans, correct_ans,
                             rep.format(student_ans, n, correct_ans))

    # vérifie ce que la fonction renvoi avec: n morts et m policiers tués TEL QUE les étoiles dépasseraient la limite de 6 => elle devrait renvoyer 6
    def test5_GTA6_6stars(self):
        args = [(50,2), (20,4), (30,5), (40,1), (25,2), (90,3), (140,2), (20,2), (30,0), (40,40)] 
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme arguments alors que la réponse attendue est {}")
        for n in args:
            try:
                student_ans = student.gta(n[0],n[1])
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, n))
            correct_ans = correct.gta(n[0],n[1])
            self.assertEqual(student_ans, correct_ans,
                             rep.format(student_ans, n, correct_ans))

if __name__ == '__main__':
    unittest.main()
