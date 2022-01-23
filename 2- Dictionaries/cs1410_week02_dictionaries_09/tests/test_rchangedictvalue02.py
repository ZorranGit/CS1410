# # python -m unittest discover -vbs tests

import unittest

from rchangedictvalue02 import *

import random, os

def random_key():
    s = ""
    size = random.randint(3, 8)
    for i in range(size):
        c = chr(random.randint(ord('a'), ord('z')))
        s += c
    return s

def random_value():
    s = ""
    size = random.randint(8, 20)
    for i in range(size):
        c = chr(random.randint(ord('a'), ord('z')))
        s += c
    return s

def random_dictionary():
    d = {}
    size = random.randint(5, 10)
    for i in range(size):
        k = random_key()
        v = random_value()
        d[k] = v
    return d

class Test_change_dict_value02(unittest.TestCase):

    def test_01(self):
        for i in range(10):
            dictionary = random_dictionary()
            key = random.choice(list(dictionary.keys()))
            new_value = random_value()
            correct_answer = dictionary.copy()
            correct_answer[key] = new_value
            ans = change_dict_value02(dictionary, key, new_value)

            msg = "change_dict_value02(%s, %s, %s) returned %s." % (str(dictionary), str(key), str(new_value), str(ans))
            msg = msg + "  It should have returned %s." % (correct_answer)
            msg = msg + "  Check your logic and try again."
            same = (ans == correct_answer)
            self.assertTrue(same, msg)
        return
