"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
Do Not Move on to the next function until its tests report 'ok' or your code
may not work as expected.
"""

import sys
if sys.version_info.major != 3:
    print('You must use Python 3.x version to run this unit test')
    sys.exit(1)

import unittest

from test_CaloricBalance_init import TestCaloricBalanceInit
from test_CaloricBalance_getBMR import TestCaloricBalanceGetBMR
from test_CaloricBalance_getBalance import TestCaloricBalanceGetBalance
from test_CaloricBalance_recordActivity import TestCaloricBalanceRecordActivity
from test_CaloricBalance_eatFood import TestCaloricBalanceEatFood
from test_CaloricBalance_all import TestCaloricBalanceAll
from test_main_formatMenu import TestFormatMenu
from test_main_formatMenuPrompt import TestFormatMenuPrompt
from test_main_formatActivityMenu import TestFormatActivityMenu
from test_main_getUserString import TestGetUserString
from test_main_getUserFloat import TestGetUserFloat
from test_main_createCaloricBalance import TestCreateCaloricBalance
from test_main_recordActivityAction import TestRecordActivityAction
from test_main_eatFoodAction import TestEatFoodAction
from test_main_quitAction import TestQuitAction
from test_main_applyAction import TestApplyAction

if __name__ == '__main__':
    testCases = [
        TestCaloricBalanceInit,
        TestCaloricBalanceGetBMR,
        TestCaloricBalanceGetBalance,
        TestCaloricBalanceRecordActivity,
        TestCaloricBalanceEatFood,
        TestCaloricBalanceAll,
        TestFormatMenu,
        TestFormatMenuPrompt,
        TestFormatActivityMenu,
        TestGetUserString,
        TestGetUserFloat,
        TestCreateCaloricBalance,
        TestRecordActivityAction,
        TestEatFoodAction,
        TestQuitAction,
        TestApplyAction
    ]

    allTests = []
    for testCase in testCases:
        allTests.append(unittest.TestLoader().loadTestsFromTestCase(testCase))

    unittest.TextTestRunner().run(unittest.TestSuite(allTests))
