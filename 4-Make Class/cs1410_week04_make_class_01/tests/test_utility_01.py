# # python -m unittest discover -vbs tests

import unittest

from car import *

class Test_CarUtility01(unittest.TestCase):

    def test_01(self):

        accel   = [  0.1,  1.0,  2.3, 12.3,   0.0,  -1.0, 100.0,   1.0 ]
        ret     = [ True, True, True, True, False, False,  True, False ]
        correct = [  0.1,  1.1,  3.4, 15.7,  15.7,  15.7,  80.0,  80.0 ]

        # check initial speed
        c = Car()
        correct_answer = 0.0
        your_ans = c.getSpeed()

        msg = "getSpeed() returned a speed of %s." % (str(your_ans), )
        msg = msg + "  It should have returned a speed of %s." % (str(correct_answer))
        msg = msg + "  Check your logic and try again."
        same = (abs(your_ans - correct_answer) < 0.0001)
        self.assertTrue(same, msg)

        for i in range(len(correct)):
            # check return value
            correct_answer = ret[i]
            your_ans = c.accelerate(accel[i])

            msg = "accelerate(%s) returned %s." % (str(accel[i]), str(your_ans), )
            msg = msg + "  It should have returned %s." % (str(correct_answer))
            msg = msg + "  Check your logic and try again."
            same = (correct_answer == your_ans)
            self.assertTrue(same, msg)

            # check assigned speed
            correct_answer = correct[i]
            your_ans = c.getSpeed()

            msg = "After accelerate(%s) the speed is %s." % (str(accel[i]), str(your_ans), )
            msg = msg + "  It should be %s." % (str(correct_answer))
            msg = msg + "  Check your logic and try again."
            same = (abs(your_ans - correct_answer) < 0.0001)
            self.assertTrue(same, msg)

        return
