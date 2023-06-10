def is_palindrome(string):
    # Remove whitespace and convert to lowercase
    string = string.replace(" ", "").lower()
    
    # Check if the reversed string is equal to the original string
    if string == string[::-1]:
        return True
    else:
        return False

import unittest

class PalindromeTestCase(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("madam"))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("world"))

if __name__ == '__main__':
    unittest.main()
