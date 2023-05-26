import unittest


def gcd(n):
    pass


class TestGcd(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(12, 18), 6)
        self.assertEqual(gcd(9, 15), 3)
        self.assertEqual(gcd(5, 7), 1)
        self.assertEqual(gcd(10, 10), 10)


if __name__ == '__main__':
    unittest.main()
