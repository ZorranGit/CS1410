# # python -m unittest discover -vbs tests

import unittest

from wvaluestodict import *

class Test_values_to_dict(unittest.TestCase):

    def test_01(self):
        # at bats, hits, runs batted in, average
        parameters = [ ( 300, 80, 20, 0.300),
                       ( 200, 70, 30, 0.280),
                       ( 350, 90, 40, 0.320),
                       ( 275, 85, 23, 0.330), ]
        correct_answers = [ { "AB": 300, "H": 80, "RBI": 20, "AVG": 0.300 },
                            { "AB": 200, "H": 70, "RBI": 30, "AVG": 0.280 },
                            { "AB": 350, "H": 90, "RBI": 40, "AVG": 0.320 },
                            { "AB": 275, "H": 85, "RBI": 23, "AVG": 0.330 }, ]

        for i in range(len(parameters)):
            correct_answer = correct_answers[i]
            ab, h, rbi, avg = parameters[i]
            ans = values_to_dict(ab, h, rbi, avg)

            msg = "values_to_dict(%s, %s, %s, %s) returned %s." % (str(ab), str(h), str(rbi), str(avg), str(ans))
            msg = msg + "  It should have returned %s." % (str(correct_answer))
            msg = msg + "  Check your logic and try again."
            same = (ans == correct_answer)
            self.assertTrue(same, msg)

        return
