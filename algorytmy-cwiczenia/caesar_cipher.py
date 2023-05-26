import unittest


def caesar_cipher(s, rot):
    pass


class TestCaesarCipher(unittest.TestCase):
    def test_caesar_cipher(self):
        self.assertEqual(caesar_cipher("hello", 3), "khoor")
        self.assertEqual(caesar_cipher("world", -5), "rcopa")
        self.assertEqual(caesar_cipher("A B C", 1), "B C D")


if __name__ == '__main__':
    unittest.main()
