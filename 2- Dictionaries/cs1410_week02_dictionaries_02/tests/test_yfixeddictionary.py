# # python -m unittest discover -vbs tests

import unittest

from yfixeddictionary import *

class Test_fixed_dictionary(unittest.TestCase):

    def test_01(self):
        parameters = [ (), ]
        correct_answers = [ { "Utah": "Quaking Aspen",
                              "Texas": "Pecan",
                              "Vermont": "Sugar Maple" }, ]

        for i in range(len(parameters)):
            correct_answer = correct_answers[i]
            ans = fixed_dictionary()

            msg = "fixed_dictionary() returned %s." % (str(ans))
            msg = msg + "  It should have returned %s." % (str(correct_answer))
            msg = msg + "  Check your logic and try again."
            same = (ans == correct_answer)
            self.assertTrue(same, msg)

        return
