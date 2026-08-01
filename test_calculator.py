# https://github.com/csmith-19/lab11-CS-JF
# Partner 1: Charles Smith
# Partner 2: Jaxon Forkey

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 2), 1)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(2, 1), 1)
        self.assertEqual(subtract(-1, 2), -3)
        self.assertEqual(subtract(0, 0), 0)

    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(0, 1), 0)
        self.assertNotEqual(mul(3, 3), 10)
        self.assertEqual(mul(1.2, 1.0), 1.2)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(5.0, 10.0), 2)
        self.assertNotEqual(div(10.0, 5.0), 2)
        self.assertEqual(div(1, 10), 10)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(0,5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(10,100), 2)
        self.assertEqual(logarithm(2,8), 3)
        self.assertEqual(logarithm(5,25), 2)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(-10,100)
            
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 10)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(-3, -4), 5)
        self.assertEqual(hypotenuse(0, 0), 0)

    def test_sqrt(self): # 3 assertions
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(0), 0)
        with self.assertRaises(ValueError):
            square_root(-1)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()