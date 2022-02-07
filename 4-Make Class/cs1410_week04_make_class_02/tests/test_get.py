# # python -m unittest discover -vbs tests

import unittest

from circle import *

class Test_CircleGet(unittest.TestCase):

    def test_01(self):
        c = Circle(2.1)

        correct_answer = 2.1
        your_ans = c.getRadius()

        msg = "getRadius() returned a radius of %s." % (str(your_ans), )
        msg = msg + "  It should have returned a radius of %s." % (str(correct_answer))
        msg = msg + "  Check your logic and try again."
        same = (abs(your_ans - correct_answer) < 0.0001)
        self.assertTrue(same, msg)


        radii   = [ 1.0, 10.0, 100.0, 0.0 ]
        correct = [ 1.0, 10.0, 100.0, 0.0 ]

        for i in range(len(correct)):

            c = Circle(radii[i])

            correct_answer = correct[i]
            your_ans = c.getRadius()

            msg = "getRadius() returned a radius of %s." % (str(your_ans), )
            msg = msg + "  It should have returned a radius of %s." % (str(correct_answer))
            msg = msg + "  Check your logic and try again."
            same = (abs(your_ans - correct_answer) < 0.0001)
            self.assertTrue(same, msg)

        return
