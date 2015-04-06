#!/usr/bin/env python
from enum import Enum

class BaseRomanNumerals(Enum):
    X = 10
    IX = 9
    V = 5
    IV = 4
    I = 1

class RomanNumerals(object):
    def convert_to_roman(self, arabic_number):
        converted_number = ""

        for numeral in BaseRomanNumerals.__reversed__():
            while arabic_number >= numeral.value:
                converted_number += numeral.name
                arabic_number -= numeral.value

        return converted_number