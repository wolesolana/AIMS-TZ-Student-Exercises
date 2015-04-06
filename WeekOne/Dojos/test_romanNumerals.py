import unittest
from unittest import TestCase
from RomanNumerals import *

class TestRomanNumerals(TestCase):
    def test_converts_1_to_I(self):
        self.assertEqual(RomanNumerals().convert_to_roman(1), "I")

    def test_converts_2_to_II(self):
        self.assertEqual(RomanNumerals().convert_to_roman(2), "II")

    def test_converts_4_to_IV(self):
        self.assertEqual(RomanNumerals().convert_to_roman(4), "IV")

    def test_converts_5_to_V(self):
        self.assertEqual(RomanNumerals().convert_to_roman(5), "V")

    def test_converts_6_to_VI(self):
        self.assertEqual(RomanNumerals().convert_to_roman(6), "VI")

    def test_converts_9_to_IX(self):
        self.assertEqual(RomanNumerals().convert_to_roman(9), "IX")

    def test_converts_10_to_X(self):
        self.assertEqual(RomanNumerals().convert_to_roman(10), "X")

if __name__ == '__main__':
    unittest.main()