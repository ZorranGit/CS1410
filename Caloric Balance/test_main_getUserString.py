"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import sys
if sys.version_info.major != 3:
    print('You must use Python 3.x version to run this unit test')
    sys.exit(1)

import unittest

import main


class TestGetUserString(unittest.TestCase):
    def input_replacement(self, prompt):
        self.assertFalse(self.too_many_inputs)
        self.input_given_prompt = prompt
        r = self.input_response_list[self.input_response_index]
        self.input_response_index += 1
        if self.input_response_index >= len(self.input_response_list):
            self.input_response_index = 0
            self.too_many_inputs = True
        return r

    def print_replacement(self, *args, **kargs):
        return

    def setUp(self):
        self.too_many_inputs = False
        self.input_given_prompt = None
        self.input_response_index = 0
        self.input_response_list = [""]
        main.input = self.input_replacement
        main.print = self.print_replacement

        return

    def tearDown(self):
        main.input = input
        main.print = print

    def test001_getUserStringExists(self):
        self.assertTrue('getUserString' in dir(main),
                        'Function "getUserString" is not defined, check your spelling')
        return

    def test002_getUserStringSendsCorrectPrompt(self):
        from main import getUserString
        expected_prompt = "HELLO"
        expected_response = "WORLD"
        self.input_response_list = [expected_response]
        actual_response = getUserString(expected_prompt)
        self.assertEqual(self.input_given_prompt, expected_prompt)
        return

    def test003_getUserStringGetsInput(self):
        from main import getUserString
        expected_prompt = "HELLO"
        expected_response = "WORLD"
        self.input_response_list = [expected_response]
        actual_response = getUserString(expected_prompt)
        self.assertEqual(actual_response, expected_response)
        return

    def test004_getUserStringStripsWhitespace(self):
        from main import getUserString
        expected_prompt = "HELLO"
        expected_response = "WORLD"
        self.input_response_list = [" \t\n" + expected_response + " \t\n"]
        actual_response = getUserString(expected_prompt)
        self.assertEqual(actual_response, expected_response)
        return

    def test005_getUserStringIgnoresBlankLines(self):
        from main import getUserString
        expected_prompt = "HELLO"
        expected_response = "WORLD"
        self.input_response_list = ["", "\n", " \t\n" + expected_response + " \t\n"]
        actual_response = getUserString(expected_prompt)
        self.assertEqual(actual_response, expected_response)
        return


if __name__ == '__main__':
    unittest.main()
