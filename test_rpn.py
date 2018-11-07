import unittest

import rpn

class TestBasics(unittest.TestCase):    
    def test_add(self):
        hist = list()
        result = rpn.calculate("1 1 +", hist)
        self.assertEqual(2, result)
    def test_subtract(self):
        hist = list()
        result = rpn.calculate("5 3 -", hist)
        self.assertEqual(2, result)
    def test_multiply(self):
        hist = list()
        result = rpn.calculate("5 3 *", hist)
        self.assertEqual(15, result)
    def test_divide(self):
        hist = list()
        result = rpn.calculate("6 3 /", hist)
        self.assertEqual(2, result)
    def test_exponent(self):
        hist = list()
        result = rpn.calculate("2 3 ^", hist)
        self.assertEqual(8, result)
    def test_factorial(self):
        hist = list()
        result = rpn.calculate("4 !", hist)
        self.assertEqual(24, result)
    def test_history(self):
        hist = list()
        calculation = rpn.calculate("2 3 +", hist)
        result = rpn.calculate("history", hist)
        self.assertEqual("2 + 3 = 5", result)
        calculation = rpn.calculate("4 !", hist)
        result = rpn.calculate("history", hist)
        self.assertEqual("4 ! = 24", result)
    def test_dividezero(self):
        hist = list()
        result = rpn.calculate("2 0 /", hist)
        self.assertEqual("Divide by zero error", result)

if __name__ == "__main__":
   unittest.main()
