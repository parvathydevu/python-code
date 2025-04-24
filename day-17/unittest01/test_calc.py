# Reference: https://docs.python.org/3/library/unittest.html

import unittest
from calc import Calculator

# We write all the test cases in a class
class TestCasesForCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()  # : Initializes self.data before each test method.

    # test case 1
    def test_add(self):
        self.assertEqual(self.calc.add(10, 3), 13, "The actual sum does not match expected sum")

    # test case 2
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 3), 7, "The actual diff does not match expected diff")

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(10, 3), 30, "The actual prod does not match expected prod")

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5, "The actual quot does not match expected quot")

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)


    def tearDown(self): # Cleans up self.data after each test method.
        del self.calc

if __name__ == "__main__":
    unittest.main()
    ''' self.assertRaises is a context manager provided by the unittest module. 
It is used to verify that a specific exception is raised during the execution of a block of code.'''