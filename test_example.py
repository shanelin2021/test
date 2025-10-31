import unittest
from example import greet


class TestExample(unittest.TestCase):
    """Unit tests for example.py"""
    
    def test_greet_default(self):
        """Test greet function with default parameter"""
        result = greet()
        self.assertEqual(result, "Hello, World!")
    
    def test_greet_with_name(self):
        """Test greet function with custom name"""
        result = greet("Alice")
        self.assertEqual(result, "Hello, Alice!")
    
    def test_greet_different_names(self):
        """Test greet function with various names"""
        self.assertEqual(greet("Bob"), "Hello, Bob!")
        self.assertEqual(greet("Charlie"), "Hello, Charlie!")
        self.assertEqual(greet("123"), "Hello, 123!")
    
    def test_greet_empty_string(self):
        """Test greet function with empty string"""
        result = greet("")
        self.assertEqual(result, "Hello, !")


if __name__ == "__main__":
    unittest.main()

