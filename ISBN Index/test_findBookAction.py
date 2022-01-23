"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import unittest
import isbn_index

class TestFindBookAction( unittest.TestCase ):

    def input_replacement( self, prompt ):
        self.assertFalse( self.too_many_inputs )
        self.input_given_prompt = prompt
        r = self.input_response_list[ self.input_response_index ]
        self.input_response_index += 1
        if self.input_response_index >= len( self.input_response_list ):
            self.input_response_index = 0
            self.too_many_inputs = True
        return r

    def print_replacement( self, *text ):
        line = " ".join( text ) + "\n"
        self.printed_lines.append( line )
        return

    def setUp(self):

        self.too_many_inputs = False
        self.input_given_prompt = None
        self.input_response_index = 0
        self.input_response_list = [ "" ]
        isbn_index.input = self.input_replacement

        self.printed_lines = [ ]
        isbn_index.print = self.print_replacement


        return

    def tearDown(self):
        return

    def test001_findBookActionExists(self):
        self.assertTrue('findBookAction' in dir( isbn_index ),
                        'Function "findBookAction" is not defined, check your spelling')
        return

    def test002_findBookActionFindsBook(self):
        isbn = "0000-12345678"
        title = "War of the Worlds"
        index = { isbn: title }
        expected = { isbn: title }

        self.input_response_list = [ isbn + "\n" ]
        isbn_index.findBookAction( index )
        self.assertDictEqual( index, expected )
        printed_text = "".join( self.printed_lines )
        self.assertIn( title, printed_text )
        return

    def test003_findBookActionDoesNotFindMissingBook(self):
        isbn = "0000-12345678"
        title = "War of the Worlds"
        index = { }
        expected = { }

        self.input_response_list = [ isbn + "\n" ]
        isbn_index.findBookAction( index )
        self.assertDictEqual( index, expected )
        printed_text = "".join( self.printed_lines )
        self.assertNotIn( title, printed_text )
        self.assertGreater( len( self.printed_lines ), 0 )
        return

if __name__ == '__main__':
    unittest.main()
