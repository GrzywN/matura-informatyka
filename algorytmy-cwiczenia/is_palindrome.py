import unittest


# is_palindrome(s) - Sprawdza, czy ciąg znaków s jest palindromem.
def is_palindrome(s):
    pass


class TestIsPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("deified"))
        self.assertTrue(is_palindrome("level"))
        self.assertFalse(is_palindrome("hello"))


if __name__ == '__main__':
    unittest.main()
