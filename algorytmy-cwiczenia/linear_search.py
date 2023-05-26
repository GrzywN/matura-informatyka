import unittest


def linear_search(T, target):
    pass


class TestLinearSearch(unittest.TestCase):
    def test_linear_search(self):
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(linear_search(["apple", "banana", "cherry"], "banana"), 1)
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 6), -1)


if __name__ == '__main__':
    unittest.main()
