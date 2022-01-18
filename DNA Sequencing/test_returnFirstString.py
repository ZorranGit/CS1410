"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import unittest
import dna

class TestReturnFirstString(unittest.TestCase):

    def test001_returnFirstStringExists(self):
        self.assertTrue('returnFirstString' in dir(dna),
                        'Function "returnFirstString" was not defined, check your spelling')

    def test002_nonEmptyString1(self):
        from dna import returnFirstString
        self.assertEqual(returnFirstString(['aaa', 'bbb', 'ccc']), 'aaa', 'Your function should have returned "aaa"')

    def test003_nonEmptyString2(self):
        from dna import returnFirstString
        self.assertEqual(returnFirstString(['bbb', 'aaa', 'ccc']), 'bbb', 'Your function should have returned "bbb"')

    def test004_nonEmptyString3(self):
        from dna import returnFirstString
        self.assertEqual(returnFirstString(['ccc', 'bbb', 'aaa']), 'ccc', 'Your function should have returned "ccc"')

    def test005_nonEmptyString4(self):
        from dna import returnFirstString
        self.assertEqual(returnFirstString([]), '', 'Your function should have returned an empty string')

if __name__ == '__main__':
    unittest.main()
