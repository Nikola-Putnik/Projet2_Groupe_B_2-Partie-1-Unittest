#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import sys

import CorrLoveTest as correct
import LoveTest as student

i1 = ["Jul",20,"Bleu","Chien","Fifa","Got"]

l1 = [["Alice",20,"Bleu","Chien","Pes","Got"],
      ["Morgane",20,"Rouge","Chien","Fifa","Walking Dead"],
      ["Monika",30,"Rouge","Chat","Fifa","Got"],
      ["Charlotte",40,"Bleu","Chat","Fifa","Gossip girl"],
      ["Alix",20,"Vert","Chien","Pes","Got"]]

"""
CONSIGNES:

Ton ami Jul cherche désespérement son âme soeur.
Tu aimrerais l'aider en lui proposant un programme qui lui trouverait la femme idéale.

Pour cela, tu pourras compter sur ton ami Bernard travaillant pour site de rencontre qui t'enverra quotidiennement une liste de candidates habitant dans la ville de Jul.

Dans les listes qu'il t'enverra, chaque candidate sera représentée par une sous-liste, qui comprendra (dans cet ordre): son nom et 5 caractéristiques: son âge, sa couleur préférée,
sa préférence entre chien ou chat, sa préférérence entre Pes ou Fifa, et enfin, sa série préférée.
exemple de liste de candidates reçue de Bernard: 
candidates = [["Jeanine", 20, "bleu", "chien", "Pes", "Game of Thrones"],
              ["Claudine", 30, "rouge", "chien", "Fifa", "Walking Dead"],
              ["Monika", 40, "rouge", "chat", "Fifa", "Game of Thrones"]]

Tu recevras également une liste de Jul dans laquelle il te donnera ses caractéristiques sous la même forme que les candidates.
exemple de liste reçue de Jul:
jul = ["Jul", 20, "bleu", "chien", "Fifa", "Game of Thrones"]

Sur base de la liste de Jul et de la liste de candidates, ton but est de renvoyer à Jul la (ou les) candidate(s) **gagnante(s)** avec qui Jul a le plus de **points communs**.
Chacune des 5 caractéristiques (age, "couleur", "chien/chat", "Pes/Fifa", "Série") est susceptible d'être un point commun si elle est identique pour Jul et la candidate.

Tu écris une fonction love_test(jul, candidates) qui renverra dans une liste, le (ou les) nom(s) de la (ou des) candidate(s) gagnante(s).
Enfin, tu compléteras cette liste en donnant le pourcentage de points communs avec la/les candidate(s) gagnante(s)
ex: si 4 caractéristiques communes sur 5, le pourcentage est de 80.0

À noter:
- Le nombre de candidates présentes dans la liste de Bernard peut varier d'un jour à l'autre, la liste que vous recevrez peut-être très remplie tout comme entièrement vide.
- Pour être *gagnante*, une candidate doit avoir un pourcentage de points communs supérieur à 0%
- Pour l'âge, seules les décennies sont prises en compte, vous ne recevrez donc que des entiers arrondis à la dizaine près: 20, 30, 40, 50, ...


EXEMPLE:
Pour candidates = [["Alice",20,"bleu","chien","Pes","Game of Thrones"],
                   ["Morgane",20,"rouge","chien","Fifa","Walking Dead"],
                   ["Monika",30,"rouge","chat","Fifa","Game of Thrones"],
                   ["Charlotte",40,"bleu","chat","Fifa","Gossip girl"],
                   ["Géraldine",20,"bleu","chien","Fifa","Walking Dead"],
                   ["Alix",20,"vert","chien","Pes","Game of Thrones"]]

et jul = ["Jul",20,"bleu","chien","Fifa","Game of Thrones"]

la fonction retourne
['Alice', 'Géraldine', 80.0]
"""

# IDEES TESTS UNITAIRES:
# - test avec 1 seule gagnante
#   -> test avec la gagnante au début de la liste -> ex: [GAGNANTE, perdante, perdante, perdante, perdante]
#   -> test avec la gagnante au milieu de la liste -> ex: [perdante, perdante, GAGNANTE, perdante, perdante]
#   -> test avec la gagnante à la fin de la liste -> ex: [perdante, perdante, perdante, perdante, GAGNANTE]
# - test avec plusieurs gagnantes (2, 3, ...)
#   -> test avec les gagnantes qui se suivent dans la liste -> ex: [perdante, perdante, GAGNANTE, GAGNANTE, perdante]
#   -> test avec les gagnantes qui ne se suivent pas dans la liste -> ex: [GAGNANTE, perdante, perdante, GAGNANTE, perdante]
# - test avec aucune perdante -> ex: [GAGNANTE, GAGNANTE, GAGNANTE, GAGNANTE, GAGNANTE]
# - test avec aucune gagnante (0% pour toutes les candidates) -> ex: [perdante, perdante, perdante, perdante, perdante]
# - test avec une liste ne contenant qu'1 seule candidate
#   -> test avec l'unique candidate étant gagnante (>0%) -> ex: [GAGNANTE]
#   -> test avec l'unique candidate étant perdante (=0%) -> ex: [perdante]
# - test avec liste des candidates vide => renvoi liste vide => il faut peut être le mentionner dans l'énoncé dans ce cas

class TestLoveTest(unittest.TestCase):

    def test0_None(self): # vérifie que la fonction renvoi quelque chose
        args = [(j1,c1), (j2,c1)]
        rep = _("Votre fonction a retourné None pour {} comme argument. Cela implique probablement qu'il manque un return dans votre code.")
        for n in args:
            try:
                student_ans = student.love_test(n[0],n[1])
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, n))
            self.assertIsNotNone(student_ans, rep.format(n))

    def test1_LoveTest_empty(self): # vérifie ce que la fonction renvoi si la liste des candidates est vide => elle devrait renvoyer une liste vide
        args = [(j1,c0)]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument positif alors que la réponse attendue est {}")
        for n in args:
            try:
                student_ans = student.love_test(n[0],n[1])
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, n))
            correct_ans = correct.love_test(n[0],n[1])
            self.assertEqual(student_ans, correct_ans,
                             rep.format(student_ans, n, correct_ans))


if __name__ == '__main__':
    unittest.main()
