import unittest


# leader(T) - Zwraca liderów listy T (elementy, które występują w T ponad połowę razy).
def leader(T):
    pass


class TestLeader(unittest.TestCase):
    def test_leader(self):
        self.assertEqual(leader([3, 3, 4, 2, 4, 4, 2, 4, 4]), 4)
        self.assertEqual(leader([1, 1, 2]), -1)
        self.assertEqual(leader([1, 2, 3]), -1)
        self.assertEqual(leader([]), -1)


if __name__ == '__main__':
    unittest.main()
