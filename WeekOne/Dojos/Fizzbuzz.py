#!/usr/bin/env python
import sys
import os

class Fizzbuzz(object):
    def convert(self, number):
        if (number % 15) == 0:
            return "FizzBuzz"
        elif (number % 3) == 0 or "3" in str(number):
            return "Fizz"
        elif (number % 5) == 0 or "5" in str(number):
            return "Buzz"
        else:
            return str(number)

    def print_converted_numbers(self, last_number):
        converted_list = []
        for i in range(1, last_number + 1):
            converted_list.append(self.convert(i))

        print " ".join(converted_list)


try:
    if len(sys.argv) == 2:
        Fizzbuzz().print_converted_numbers(int(sys.argv[1]))

except IOError:
    path = os.getcwd()
    print path
