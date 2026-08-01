# https://github.com/csmith-19/lab11-CS-JF
# Partner 1: Charles Smith
# Partner 2: Jaxon Forkey
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""


import math

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

# First example

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b / a

def logarithm(a, b):
    if a <= 0:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a ** b

