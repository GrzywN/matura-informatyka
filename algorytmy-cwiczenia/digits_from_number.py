import unittest


# digits_from_number(n) - Zwraca listę cyfr liczby n w kolejności od najmniej
# znaczącej do najbardziej znaczącej.
def digits_from_number(n):
    pass


class TestDigitsFromNumber(unittest.TestCase):
    def test_digits_from_number(self):
        self.assertEqual(digits_from_number(12345), [5, 4, 3, 2, 1])
        self.assertEqual(digits_from_number(8675309), [9, 0, 3, 5, 7, 6, 8])
        self.assertEqual(digits_from_number(100), [0, 0, 1])


if __name__ == '__main__':
    unittest.main()
