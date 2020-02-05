import unittest

from Calculator.Calculator import Calculator

class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator
        self.assertIsInstance(Calculator, calculator)

    def test_calculator_addition(self, a, b):
        calculator = Calculator
        result = calculator.addition(1, 2)
        self.assertEqual(3, result)

    def test_calculator_subtraction(self, a, b):
        calculator = Calculator
        result = calculator.subtraction(1, 2)
        self.assertEqual(-1, result)

    def test_calculator_multiply(self, a, b):
        calculator = Calculator
        result = calculator.multiply(1, 2)
        self.assertEqual(2, result)

    def test_calculator_divide(self, a, b):
        calculator = Calculator
        result = calculator.subtraction(6, 2)
        self.assertEqual(3, result)

if __name__ == '__main__':
    unittest.main()