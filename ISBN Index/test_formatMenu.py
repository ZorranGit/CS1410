"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import unittest
import re
import isbn_index

class TestFormatMenu( unittest.TestCase ):

    def setUp(self):
        return

    def tearDown(self):
        return

    def test001_formatMenuExists(self):
        self.assertTrue('formatMenu' in dir( isbn_index ),
                        'Function "formatMenu" is not defined, check your spelling')
        return

    def test002_formatMenuContainsAllActions(self):
        expected = [ "\[r\]",
                     "\[f\]",
                     "\[l\]",
                     "\[q\]" ]
        menu_list = isbn_index.formatMenu( )
        for expected_line in expected:
            found = False
            for actual_line in menu_list:
                if re.search( expected_line, actual_line ):
                    found = True
                    break
            self.assertTrue( found, "'" + expected_line + "' not found in formatMenu return" )
        return


if __name__ == '__main__':
    unittest.main()
