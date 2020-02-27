#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import sys

import CorrLoveTest as correct
import LoveTest as student

i1 = ["Kenny",20,"Bleu","Chien","Fifa","Got"]

l1 = [["Alice",20,"Bleu","Chien","Pes","Got"],
      ["Morgane",20,"Rouge","Chien","Fifa","Walking Dead"],
      ["Monika",30,"Rouge","Chat","Fifa","Got"],
      ["Charlotte",40,"Bleu","Chat","Fifa","Gossip girl"],
      ["Alix",20,"Vert","Chien","Pes","Got"]]

class TestLoveTest(unittest.TestCase):

    def test0_None(self):
        args = [-3, 0, 5]
        rep = _("Votre fonction a retourné None pour {} comme argument. Cela implique probablement qu'il manque un return dans votre code.")
        for n in args:
            try:
                student_ans = student.abs(n)
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, n))
            self.assertIsNotNone(student_ans, rep.format(n))

    def test1_abs_0(self):
        args = [0]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}")
        for n in args:
            try:
                student_ans = student.abs(n)
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, n))
            correct_ans = correct.abs(n)
            self.assertEqual(student_ans, correct_ans,
                             rep.format(student_ans, n, correct_ans))

    def test1_abs_pos(self):
        args = [1, 5, 17, 98]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument positif alors que la réponse attendue est {}")
        for n in args:
            try:
                student_ans = student.abs(n)
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, n))
            correct_ans = correct.abs(n)
            self.assertEqual(student_ans, correct_ans,
                             rep.format(student_ans, n, correct_ans))

    def test2_abs_neg(self):
        args = [-1, -9, -22, -1234]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument négatif alors que la réponse attendue est {}")
        for n in args:
            try:
                student_ans = student.abs(n)
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, n))
            correct_ans = correct.abs(n)
            self.assertEqual(student_ans, correct_ans,
                             rep.format(student_ans, n, correct_ans))


if __name__ == '__main__':
    unittest.main()
