import unittest


def is_prime(n):
    pass


class TestIsPrime(unittest.TestCase):
    def test_is_prime(self):
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(3), True)
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(29), True)
        self.assertEqual(is_prime(100), False)


if __name__ == '__main__':
    unittest.main()
