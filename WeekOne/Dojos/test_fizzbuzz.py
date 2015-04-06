import unittest
from unittest import TestCase
from Fizzbuzz import *
from test import test_support


class TestFizzbuzz(TestCase):
    def test_should_return_fizz_for_3(self):
        self.assertEqual(Fizzbuzz().convert(3), "Fizz")

    def test_should_return_buzz_for_5(self):
        self.assertEqual(Fizzbuzz().convert(5), "Buzz")

    def test_should_return_fizzbuzz_if_number_is_divisible_by_3_and_5(self):
        self.assertEqual(Fizzbuzz().convert(30), "FizzBuzz")

    def test_should_return_fizz_for_multiples_of_3(self):
        self.assertEqual(Fizzbuzz().convert(6), "Fizz")

    def test_should_return_buzz_for_multiples_of_5(self):
        self.assertEqual(Fizzbuzz().convert(10), "Buzz")

    def test_should_return_the_number_if_it_is_NOT_divisible_by_either_3_nor_5(self):
        self.assertEqual(Fizzbuzz().convert(7), "7")

    def test_should_print_out_a_converted_list_when_given_a_range_of_numbers(self):
        last_number = 15

        with test_support.captured_stdout() as printed_output:
            Fizzbuzz().print_converted_numbers(last_number)

        self.assertEqual(printed_output.getvalue().rstrip(), "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz Fizz 14 FizzBuzz")

    def test_should_return_fizz_if_the_number_contains_a_3(self):
        self.assertEqual(Fizzbuzz().convert(13), "Fizz")

    def test_should_return_buzz_if_the_number_contains_a_5(self):
        self.assertEqual(Fizzbuzz().convert(52), "Buzz")

if __name__ == '__main__':
    unittest.main()