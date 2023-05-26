import unittest


def is_perfect(n):
    pass


class TestIsPerfect(unittest.TestCase):
    def test_is_perfect(self):
        self.assertEqual(is_perfect(6), True)
        self.assertEqual(is_perfect(28), True)
        self.assertEqual(is_perfect(496), True)
        self.assertEqual(is_perfect(8128), True)
        self.assertEqual(is_perfect(10), False)
        self.assertEqual(is_perfect(100), False)


if __name__ == '__main__':
    unittest.main()
