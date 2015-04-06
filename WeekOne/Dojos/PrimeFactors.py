#!/usr/bin/env python
import sys
import os

class PrimeFactors(object):
    def factorize(self, number):
        prime_factors = []
        for divisor in range(2, number + 1):
            while number % divisor == 0:
                if divisor not in prime_factors:
                    prime_factors.append(divisor)
                number //= divisor

        return prime_factors

    def print_prime_factors(self, number):
        print self.factorize(number)


try:
    if len(sys.argv) > 1:
        PrimeFactors().print_prime_factors(int(sys.argv[1]))

except IOError:
    path = os.getcwd()
    print path