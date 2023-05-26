import unittest


def prime_factors(n):
    pass


class TestPrimeFactors(unittest.TestCase):
    def test_prime_factors(self):
        self.assertEqual(prime_factors(12), [2, 2, 3])
        self.assertEqual(prime_factors(30), [2, 3, 5])
        self.assertEqual(prime_factors(35), [5, 7])
        self.assertEqual(prime_factors(71), [71])


if __name__ == '__main__':
    unittest.main()
