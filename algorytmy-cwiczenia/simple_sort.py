import unittest


def simple_sort(T):
    pass


class TestSimpleSort(unittest.TestCase):
    def test_simple_sort(self):
        self.assertEqual(simple_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])
        self.assertEqual(simple_sort([1, 1, 1, 1]),  [1, 1, 1, 1])
        self.assertEqual(simple_sort([4, 3, 2, 1]),  [1, 2, 3, 4])
        self.assertEqual(simple_sort([]), [])


if __name__ == '__main__':
    unittest.main()
