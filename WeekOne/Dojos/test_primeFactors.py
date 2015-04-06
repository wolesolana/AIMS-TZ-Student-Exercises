import unittest
from unittest import TestCase
from PrimeFactors import *

class TestPrimeFactors(TestCase):
    def test_returns_the_prime_factor_of_2_as_2(self):
        self.assertEqual(PrimeFactors().factorize(2), [2])


if __name__ == '__main__':
    unittest.main()