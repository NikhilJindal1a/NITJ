# 1. Write a program that has a class Fraction with attributes numerator 
# and denominator. Enter the values of the attributes 
# and print the fraction in simplified form.

import math

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def simplify(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def display(self):
        self.simplify()
        print(f"Simplified Fraction: {self.numerator}/{self.denominator}")

# Example usage
f = Fraction(8, 12)
f.display()
