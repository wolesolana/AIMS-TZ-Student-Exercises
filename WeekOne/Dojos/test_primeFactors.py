import unittest
from unittest import TestCase
from PrimeFactors import *
from test import test_support

class TestPrimeFactors(TestCase):
    def test_returns_the_prime_factor_of_2_as_2(self):
        self.assertEqual(PrimeFactors().factorize(2), [2])

    def test_returns_the_prime_factor_of_3_as_3(self):
        self.assertEqual(PrimeFactors().factorize(3), [3])

    def test_returns_the_prime_factor_of_5_as_5(self):
        self.assertEqual(PrimeFactors().factorize(5), [5])

    def test_returns_the_prime_factors_of_30_as_2_3_5(self):
        self.assertEqual(PrimeFactors().factorize(30), [2, 3, 5])

    def test_returns_the_prime_factors_of_12_as_2_3(self):
        self.assertEqual(PrimeFactors().factorize(12), [2, 3])

    def test_prints_out_the_prime_factors_of_49_as_7(self):
        with test_support.captured_stdout() as printed_output:
            PrimeFactors().print_prime_factors(49)

        self.assertEqual(printed_output.getvalue().rstrip(), "[7]")


if __name__ == '__main__':
    unittest.main()