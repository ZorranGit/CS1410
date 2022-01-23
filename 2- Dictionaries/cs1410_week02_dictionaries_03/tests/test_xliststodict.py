# # python -m unittest discover -vbs tests

import unittest

from xliststodict import *

class Test_lists_to_dict(unittest.TestCase):

    def test_01(self):
        parameters = [ ( ["Utah", "Texas", "Vermont"], ["Quaking Aspen", "Pecan", "Sugar Maple"] ),
                       ( ["North Carolina", "North Dakota", "Ohio"], ["Longleaf Pine", "American Elm", "Ohio Buckeye"] ), ]
        correct_answers = [ { "Utah": "Quaking Aspen", "Texas": "Pecan", "Vermont": "Sugar Maple" },
                            { "North Carolina": "Longleaf Pine", "North Dakota": "American Elm", "Ohio": "Ohio Buckeye" }, ]

        for i in range(len(parameters)):
            correct_answer = correct_answers[i]
            keys, values = parameters[i]
            ans = lists_to_dict(keys, values)

            msg = "lists_to_dict(%s, %s) returned %s." % (str(keys), str(values), str(ans))
            msg = msg + "  It should have returned %s." % (str(correct_answer))
            msg = msg + "  Check your logic and try again."
            same = (ans == correct_answer)
            self.assertTrue(same, msg)

        return
