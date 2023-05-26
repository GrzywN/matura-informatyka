import unittest


# idol(T) - Zwraca idola listy T (element, który występuje w T ponad połowę razy, gdy usuniemy wszystkie pary różnych elementów).
def idol(T):
    pass


class TestIdol(unittest.TestCase):
    def test_idol(self):
        self.assertEqual(idol([3, 3, 4, 2, 4, 4, 2, 4, 4]), 4)
        self.assertEqual(idol([1, 1, 2]), 1)
        self.assertEqual(idol([1, 2, 3]), -1)
        self.assertEqual(idol([]), -1)


if __name__ == '__main__':
    unittest.main()
