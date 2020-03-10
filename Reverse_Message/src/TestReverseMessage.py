#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import sys

import CorrReverseMessage as correct
import ReverseMessage as student


"""
CONSIGNES:

Votre ami est atteint d’une étrange maladie, il remplace systématiquement le premier et le dernier mot de ses phrases, et, comme si ce problème ne lui suffisait pas, il se trompe également souvent dans le nombre d'espaces qu'il écrit.

Pour l’aider et enfin comprendre ses messages, vous décidez d’implémenter sur son téléphone un programme qui corrige automatiquement son problème.

Il vous est demandé d'écrire une fonction reverse_word(s) qui reçoit une phrase en paramètre et qui renvoi cette même phrase mais en inversant le premier et le dernier mot de celle-ci, et en supprimant les espaces inutiles s'il y en a (ex: espaces doubles, espaces en début de phrase, etc).

Par exemple si votre ami vous écrit "va   ça salut  " le message sera automatiquement remplacé par "salut ça va"
"""


# TESTS UNITAIRES:
# - test None
# - test avec une chaine de caractère vide
# - test avec un seul mot
# - test avec plusieurs espaces entre les mots
# - test avec un ou plusieurs espaces au début
# - test avec un ou plusieurs espaces à la fin
# - test avec des mots identiques



class TestReverseMessage(unittest.TestCase):

    # vérifie que la fonction renvoi quelque chose
    def test0_None(self):
        args = ["Test", "hahaha", "ha haha ha "]
        rep = _("Votre fonction a retourné None pour {} comme argument. Cela implique probablement qu'il manque un return dans votre code.")
        for n in args:
            try:
                student_ans = student.reverse_word(n)
            except IndexError as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, n))
            self.assertIsNotNone(student_ans, rep.format(n))

    # vérifie ce que la fonction renvoi avec: une chaine de caractère vide => elle devrait renvoyer une chaine de caractère vide
    def test1_ReverseMessage_empty(self):
        args = [""]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec une chaine de caractère vide : {} alors que la réponse attendue est {}")
        for n in args:
            try:
                student_ans = student.reverse_word(n)
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, n))
            correct_ans = correct.reverse_word(n)
            self.assertEqual(student_ans, correct_ans,
                             rep.format(student_ans, n, correct_ans))

    # vérifie ce que la fonction renvoi avec: une chaine de caractère constituée d'un seul mot => elle devrait renvoyer ce même mot
    def test2_ReverseMessage_1Word(self):
        args = ["saperlipopette", "coronavirus", "chine", "italie", "suisse", "belgique", "danger"]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec une chaine de caractère constituée d'un unique mot : {} alors que la réponse attendue est {}")
        for n in args:
            try:
                student_ans = student.reverse_word(n)
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, n))
            correct_ans = correct.reverse_word(n)
            self.assertEqual(student_ans, correct_ans,
                             rep.format(student_ans, n, correct_ans))

    # vérifie ce que la fonction renvoi avec: une chaine de caractère dénombrant plusieurs espaces entre les mots
    def test2_ReverseMessage_WordsAndSpaces(self):
        args = ["mange    je", "vous?  allez comment", "moi    aidez", "A    B        C D   E"]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}")
        for n in args:
            try:
                student_ans = student.reverse_word(n)
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, n))
            correct_ans = correct.reverse_word(n)
            self.assertEqual(student_ans, correct_ans,
                             rep.format(student_ans, n, correct_ans))

    # vérifie ce que la fonction renvoi avec: une chaine de caractère ayant un ou plusieurs espaces au début
    def test2_ReverseMessage_SpacesStart(self):
        args = ["   Wars Star", " Thromes of Game", "     rire très drôle je suis mort de Hahahaha"]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec une chaine de caractères contenant des espaces au début: {} alors que la réponse attendue est {}")
        for n in args:
            try:
                student_ans = student.reverse_word(n)
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, n))
            correct_ans = correct.reverse_word(n)
            self.assertEqual(student_ans, correct_ans,
                             rep.format(student_ans, n, correct_ans))

    # vérifie ce que la fonction renvoi avec: une chaine de caractère ayant un ou plusieurs espaces à la fin
    def test2_ReverseMessage_SpacesEnd(self):
        args = ["Wars Star   ", "Thromes of Game ", "rire très drôle je suis mort de Hahahaha     "]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec une chaine de caractères contenant des espaces à la fin: {} alors que la réponse attendue est {}")
        for n in args:
            try:
                student_ans = student.reverse_word(n)
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, n))
            correct_ans = correct.reverse_word(n)
            self.assertEqual(student_ans, correct_ans,
                             rep.format(student_ans, n, correct_ans))

    # vérifie ce que la fonction renvoi avec: une chaine de caractère contenant des mots identiques, notament ceux à inverser
    def test2_ReverseMessage_SameWords(self):
        args = ["chocolat chocolat", "haha vraiment très drole haha", "A B C C B A", "A B C B A", "A C C B"]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}")
        for n in args:
            try:
                student_ans = student.reverse_word(n)
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, n))
            correct_ans = correct.reverse_word(n)
            self.assertEqual(student_ans, correct_ans,
                             rep.format(student_ans, n, correct_ans))

if __name__ == '__main__':
    unittest.main()
