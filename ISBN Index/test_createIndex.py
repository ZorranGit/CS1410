"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import unittest
import isbn_index

class TestCreateIndex(unittest.TestCase):

    def setUp(self):
        self.mExpectedResults = { }
        return

    def tearDown(self):
        return

    def test001_createIndexExists(self):
        self.assertTrue('createIndex' in dir( isbn_index ),
                        'Function "createIndex" is not defined, check your spelling')
        return

    def test002_createIndexReturnsEmptyDictionary(self):
        self.assertDictEqual( isbn_index.createIndex( ), self.mExpectedResults )
        return


if __name__ == '__main__':
    unittest.main()
