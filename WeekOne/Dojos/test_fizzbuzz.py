import unittest
from unittest import TestCase
from Fizzbuzz import *

class TestFizzbuzz(TestCase):
    def test_should_return_fizz_if_the_number_is_divisible_by_3(self):
        self.assertEqual(Fizzbuzz().convert(3), "Fizz")


if __name__ == '__main__':
    unittest.main()