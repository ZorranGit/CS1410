"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import sys
if sys.version_info.major != 3:
    print('You must use Python 3.x version to run this unit test')
    sys.exit(1)

import unittest

import caloric_balance


class TestCaloricBalanceRecordActivity(unittest.TestCase):
    def test001_recordActivityExists(self):
        self.assertTrue('recordActivity' in dir(caloric_balance.CaloricBalance),
                        'Function "recordActivity" is not defined, check your spelling')

    def test002_recordActivity(self):
        from caloric_balance import CaloricBalance
        cb = CaloricBalance('f', 23.0, 65.0, 130.0)

        balance = cb.getBalance()
        expected = -1417.9
        self.assertAlmostEqual(balance, expected, 2,
                               'Your result (%s) is not close enough to (%s)' % (balance, expected))

        cb.recordActivity(.074, 30)
        balance = cb.getBalance()
        expected = -1706.5
        self.assertAlmostEqual(balance, expected, 2,
                               'Your result (%s) is not close enough to (%s)' % (balance, expected))

        cb.recordActivity(.074, 45)
        balance = cb.getBalance()
        expected = -2139.4
        self.assertAlmostEqual(balance, expected, 2,
                               'Your result (%s) is not close enough to (%s)' % (balance, expected))

    def test003_getBalance(self):
        from caloric_balance import CaloricBalance
        cb = CaloricBalance('f', 27.0, 74.0, 155.0)

        balance = cb.getBalance()
        expected = -1550.15
        self.assertAlmostEqual(balance, expected, 2,
                               'Your result (%s) is not close enough to (%s)' % (balance, expected))

        cb.recordActivity(.087, 45)
        balance = cb.getBalance()
        expected = -2156.975
        self.assertAlmostEqual(balance, expected, 2,
                               'Your result (%s) is not close enough to (%s)' % (balance, expected))

        cb.recordActivity(.087, 15)
        balance = cb.getBalance()
        expected = -2359.25
        self.assertAlmostEqual(balance, expected, 2,
                               'Your result (%s) is not close enough to (%s)' % (balance, expected))

    def test004_m_getBalance(self):
        from caloric_balance import CaloricBalance
        cb = CaloricBalance('m', 26.0, 70.5, 185.0)

        balance = cb.getBalance()
        expected = -1937.1

        self.assertAlmostEqual(balance, expected, 2,
                               'Your result (%s) is not close enough to (%s)' % (balance, expected))

        cb.recordActivity(.009, 85)
        balance = cb.getBalance()
        expected = -2078.625
        self.assertAlmostEqual(balance, expected, 2,
                               'Your result (%s) is not close enough to (%s)' % (balance, expected))

        cb.recordActivity(.009, 32.6)
        balance = cb.getBalance()
        expected = -2132.90
        self.assertAlmostEqual(balance, expected, 2,
                               'Your result (%s) is not close enough to (%s)' % (balance, expected))

    def test005_m_getBalance(self):
        from caloric_balance import CaloricBalance
        cb = CaloricBalance('m', 35.0, 76.0, 275.0)

        balance = cb.getBalance()
        expected = -2506.45

        self.assertAlmostEqual(balance, expected, 2,
                               'Your result (%s) is not close enough to (%s)' % (balance, expected))

        cb.recordActivity(.036, 45)
        balance = cb.getBalance()
        expected = -2951.95
        self.assertAlmostEqual(balance, expected, 2,
                               'Your result (%s) is not close enough to (%s)' % (balance, expected))

        cb.recordActivity(.036, 30)
        balance = cb.getBalance()
        expected = -3248.95
        self.assertAlmostEqual(balance, expected, 2,
                               'Your result (%s) is not close enough to (%s)' % (balance, expected))


if __name__ == '__main__':
    unittest.main()
