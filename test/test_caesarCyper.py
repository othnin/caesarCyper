import unittest

class TestCyper(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_upper_fail(self):
        self.assertEqual('foo'.upper(), 'BAD')


if __name__ == '__main__':
    unittest.main()