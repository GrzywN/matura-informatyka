import unittest


# is_anagram(s) - Sprawdza, czy ciąg znaków s jest anagramem innego ciągu znaków.
def is_anagram(s):
    pass


class TestIsAnagram(unittest.TestCase):
    def test_is_anagram(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("heart", "earth"))
        self.assertTrue(is_anagram("debit card", "bad credit"))
        self.assertFalse(is_anagram("hello", "world"))


if __name__ == '__main__':
    unittest.main()
