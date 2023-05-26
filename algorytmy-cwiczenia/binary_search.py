import unittest


def binary_search(T, n):
    pass


class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(binary_search(["apple", "banana", "cherry"], "banana"), 1)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)


if __name__ == '__main__':
    unittest.main()
