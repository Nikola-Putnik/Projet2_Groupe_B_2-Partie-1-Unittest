#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import sys

import CorrLoveTest as correct
import LoveTest as student

i1 = ["Kenny",20,"Bleu","Chien","Fifa","Got"]
i2 = ["Platon",30,"Bleu","Chat","Fifa","Got"]

l1 = [["Alice",20,"Bleu","Chien","Pes","Got"],
      ["Morgane",20,"Rouge","Chien","Fifa","Walking Dead"],
      ["Monika",30,"Rouge","Chat","Fifa","Got"],
      ["Charlotte",40,"Bleu","Chat","Fifa","Gossip girl"],
      ["Alix",20,"Vert","Chien","Pes","Got"]]

class TestLoveTest(unittest.TestCase):

    def test1_LoveTest(self):
        args = [[i1,l1], [i2,l1]]
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
