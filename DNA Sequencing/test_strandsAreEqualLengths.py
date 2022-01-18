"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import unittest
import dna

class TestStrandsAreEqualLengths(unittest.TestCase):
    def test001_strandsAreEqualLengthsExists(self):
        self.assertTrue('strandsAreEqualLengths' in dir(dna),
                        'Function "strandsAreEqualLengths" was not defined, check your spelling')

    def test002_strandsAreEqualLengths1(self):
        from dna import strandsAreEqualLengths
        self.assertTrue(strandsAreEqualLengths('aaa', 'bbb'), 'The strands were equal lengths')

    def test003_strandsAreEqualLengths2(self):
        from dna import strandsAreEqualLengths
        self.assertTrue(strandsAreEqualLengths('aaa', 'aaa'), 'The strands were equal lengths')

    def test004_strandsAreNotEqualLengths1(self):
        from dna import strandsAreEqualLengths
        self.assertFalse(strandsAreEqualLengths('aa', 'bbb'), 'The strands were not equal lengths')

    def test005_strandsAreNotEqualLengths2(self):
        from dna import strandsAreEqualLengths
        self.assertFalse(strandsAreEqualLengths('aaa', 'bb'), 'The strands were not equal lengths')

if __name__ == '__main__':
    unittest.main()
