#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import sys

import CorrLoveTest as correct
import LoveTest as student


"""
CONSIGNES:

Ton ami Jul cherche désespérement son âme soeur.
Tu aimrerais l'aider en lui proposant un programme qui lui trouverait la femme idéale.

Pour cela, tu pourras compter sur ton ami Bernard travaillant pour site de rencontre qui t'enverra quotidiennement une **liste de candidates** habitant dans la ville de Jul.

Dans les listes qu'il t'enverra, chaque candidate sera représentée par une sous-liste, qui comprendra (dans cet ordre): son **nom** et **5 caractéristiques**: son âge, sa couleur préférée,
sa préférence entre chien ou chat, sa préférérence entre Pes ou Fifa, et enfin, sa série préférée.
exemple de liste de candidates: 
candidates = [["Jeanine", 20, "bleu", "chien", "Pes", "Game of Thrones"],
              ["Claudine", 30, "rouge", "chien", "Fifa", "Walking Dead"],
              ["Monika", 40, "rouge", "chat", "Fifa", "Game of Thrones"]]

Tu recevras également une **liste de Jul** dans laquelle il te donnera ses caractéristiques sous la même forme que les candidates.
exemple de liste reçue de Jul:
jul = ["Jul", 20, "bleu", "chien", "Fifa", "Game of Thrones"]

Sur base de la liste de Jul et de la liste de candidates, ton but est de renvoyer à Jul la (ou les) candidate(s) **gagnante(s)** avec qui Jul a **le plus de points communs**.
Chacune des 5 caractéristiques (age, "couleur", "chien/chat", "Pes/Fifa", "Série") est susceptible d'être un point commun si elle est identique pour Jul et la candidate.

Tu écris une fonction love_test(jul, candidates) qui renverra dans une liste, le (ou les) nom(s) de la (ou des) candidate(s) gagnante(s).
Enfin, tu compléteras cette liste en donnant le pourcentage de points communs avec la/les candidate(s) gagnante(s).
ex: si 4 caractéristiques communes sur 5, le pourcentage est de 80.0

À noter:
- Le nombre de candidates présentes dans la liste de Bernard peut varier d'un jour à l'autre, la liste que vous recevrez peut-être très remplie tout comme entièrement vide.
- Pour être *gagnante*, une candidate doit avoir un pourcentage de points communs supérieur à 0%.
- S'il n'y a aucune candidate gagnante pour le profil de Jul, votre fonction renvoi une liste vide.
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


# TESTS UNITAIRES:
# - test None
# - test avec liste des candidates vide => renvoi liste vide => il faut peut être le mentionner dans l'énoncé dans ce cas
# - test avec une liste ne contenant qu'1 seule candidate
#   -> test avec l'unique candidate étant gagnante (>0%) -> ex: [GAGNANTE]
#   -> test avec l'unique candidate étant perdante (=0%) -> ex: [perdante]
# - test avec aucune gagnante (0% pour toutes les candidates) -> ex: [perdante, perdante, perdante, perdante, perdante]
# - test avec plusieurs candidates dont 1 seule gagnante
#   -> test avec la gagnante au début de la liste -> ex: [GAGNANTE, perdante, perdante, perdante, perdante]
#   -> test avec la gagnante au milieu de la liste -> ex: [perdante, perdante, GAGNANTE, perdante, perdante]
#   -> test avec la gagnante à la fin de la liste -> ex: [perdante, perdante, perdante, perdante, GAGNANTE]
# - test avec plusieurs gagnantes (2, 3, ...)
#   -> test avec les gagnantes qui se suivent dans la liste -> ex: [perdante, perdante, GAGNANTE, GAGNANTE, perdante]
#   -> test avec les gagnantes qui ne se suivent pas dans la liste -> ex: [GAGNANTE, perdante, perdante, GAGNANTE, perdante]
# - test avec aucune perdante -> ex: [GAGNANTE, GAGNANTE, GAGNANTE, GAGNANTE, GAGNANTE]


# listes de Jul
j1 = ["Jul",20,"bleu","chien","Fifa","Game of Thrones"]
j2 = ["Jul",30,"vert","chat","Pes","Walking Dead"]
j3 = ["Jul",20,"rouge","chien","Pes","Gossip girl"]


# listes de candidates

# liste de candidates vide
c0 = []

# 1 candidate, perdante avec j1
c1_0 = ["Jacqueline",40,"rouge","chat","Pes","Gossip girl"]

# 1 candidate, gagnante avec j1
c1_1 = ["Henriette",20,"bleu","chat","Pes","Game of Thrones"] 

# 0 gagnante avec j1, 1 seule gagnante avec j2, 1 seule gagnante avec j3
c2 = [["Géraldine",30,"vert","chat","Pes","Walking Dead"], # seule gagnante avec j2
      ["Amandine",40,"rouge","chat","Pes","Walking Dead"],
      ["Claudette",50,"rouge","chat","Pes","Walking Dead"],
      ["Bernadette",30,"rouge","chat","Pes","Gossip girl"]] # seule gagnante avec j3

# 1 seule gagnante avec j1, 2 gagnantes avec j2, 3 gagnantes avec j3
c3 = [["Morgane",20,"rouge","chien","Fifa","Walking Dead"], # gagnante avec j3
      ["Monika",30,"rouge","chat","Fifa","Game of Thrones"],
      ["Alice",20,"bleu","chien","Pes","Game of Thrones"],  # gagnante avec j3 ; seule gagnante avec j1
      ["Charlotte",40,"bleu","chat","Fifa","Gossip girl"],
      ["Alix",20,"vert","chien","Pes","Game of Thrones"]] # gagnante avec j3

# 2 gagnantes à la suite avec j1
c4 = [["Jeanne",20,"vert","chat","Fifa","Walking Dead"], # seule gagnante avec j2
      ["Thérèse",20,"bleu","chien","Fifa","Game of Thrones"], # gagnante avec j1
      ["Lydia",20,"bleu","chien","Fifa","Game of Thrones"], # gagnante avec j1
      ["Antoinette",40,"bleu","chat","Fifa","Walking Dead"],
      ["Gertrude",50,"rouge","chien","Pes","Gossip girl"]] # seule gagnante avec j3

# 4 candidates toutes gagnantes à 100% avec j1
c5 = [["Magalie",20,"bleu","chien","Fifa","Game of Thrones"],
      ["Charlotte aux fraises",20,"bleu","chien","Fifa","Game of Thrones"],
      ["Natalie Portman",20,"bleu","chien","Fifa","Game of Thrones"],
      ["Claudine",20,"bleu","chien","Fifa","Game of Thrones"]]

# 4 candidates toutes gagnantes à 20% avec j2    
c6 = [["Isabelle",20,"vert","chien","Fifa","Game of Thrones"],
      ["Dora",50,"rouge","chat","Fifa","Game of Thrones"],
      ["Huguette",40,"bleu","chien","Pes","Game of Thrones"]]



class TestLoveTest(unittest.TestCase):

    # vérifie que la fonction renvoi quelque chose
    def test0_None(self):
        args = [(j1,c1), (j2,c1)]
        rep = _("Votre fonction a retourné None pour {} comme argument. Cela implique probablement qu'il manque un return dans votre code.")
        for n in args:
            try:
                student_ans = student.love_test(n[0],n[1])
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, n))
            self.assertIsNotNone(student_ans, rep.format(n))

    # vérifie ce que la fonction renvoi quand la liste des candidates est vide => elle devrait renvoyer une liste vide
    def test1_LoveTest_empty(self):
        args = [(j1,c0)]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec une liste de candidates vide : {} alors que la réponse attendue est {}")
        for n in args:
            try:
                student_ans = student.love_test(n[0],n[1])
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, n))
            correct_ans = correct.love_test(n[0],n[1])
            self.assertEqual(student_ans, correct_ans,
                             rep.format(student_ans, n, correct_ans))

    # liste des candidates ne contenant qu'une seule candidate, perdante => elle devrait renvoyer une liste vide
    def test2_LoveTest_1_1Fail(self):
        args = [(j1,c1_0)]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec une liste ne contenant qu'une seule candidate : {} alors que la réponse attendue est {}")
        for n in args:
            try:
                student_ans = student.love_test(n[0],n[1])
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, n))
            correct_ans = correct.love_test(n[0],n[1])
            self.assertEqual(student_ans, correct_ans,
                             rep.format(student_ans, n, correct_ans))

    # liste des candidates ne contenant qu'une seule candidate, gagnante
    def test2_LoveTest_1_1Win(self):
        args = [(j1,c1_1)]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec une liste ne contenant qu'une seule candidate : {} alors que la réponse attendue est {}")
        for n in args:
            try:
                student_ans = student.love_test(n[0],n[1])
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, n))
            correct_ans = correct.love_test(n[0],n[1])
            self.assertEqual(student_ans, correct_ans,
                             rep.format(student_ans, n, correct_ans))

    # plusieurs candidates mais aucune gagnante => elle devrait renvoyer une liste vide
    def test3_LoveTest_n_nFail(self):
        args = [(j1,c2)]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec une liste ne contenant aucune candidate gagnante : {} alors que la réponse attendue est {}")
        for n in args:
            try:
                student_ans = student.love_test(n[0],n[1])
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, n))
            correct_ans = correct.love_test(n[0],n[1])
            self.assertEqual(student_ans, correct_ans,
                             rep.format(student_ans, n, correct_ans))

    # plusieurs candidates dont 1 seule gagnante (en début de liste: (j2,c2), en milieu de liste: (j1,c3), en fin de liste: (j3,c2))
    def test3_LoveTest_n_1Win(self):
        args = [(j2,c2), (j1,c3), (j3,c2)]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec une liste contenant plusieurs candidates : {} alors que la réponse attendue est {}")
        for n in args:
            try:
                student_ans = student.love_test(n[0],n[1])
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, n))
            correct_ans = correct.love_test(n[0],n[1])
            self.assertEqual(student_ans, correct_ans,
                             rep.format(student_ans, n, correct_ans))

    # plusieurs candidates gagnantes (à la suite: (j1,c4) ou espacées: (j2,c3), (j3,c3))
    def test3_LoveTest_n_mWin(self):
        args = [(j1,c4), (j2,c3), (j3,c3)]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec une liste contenant plusieurs candidates : {} alors que la réponse attendue est {}")
        for n in args:
            try:
                student_ans = student.love_test(n[0],n[1])
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, n))
            correct_ans = correct.love_test(n[0],n[1])
            self.assertEqual(student_ans, correct_ans,
                             rep.format(student_ans, n, correct_ans))

    # liste des candidates avec toutes les candidates gagnantes
    def test4_LoveTest_n_nWin(self):
        args = [(c5,j1), (j2,c6)]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec une liste contenant plusieurs candidates : {} alors que la réponse attendue est {}")
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
