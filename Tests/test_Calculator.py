import unittest

from Calculator.Calculator import Calculator

class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator
        self.assertIsInstance(Calculator, calculator)


if __name__ == '__main__':
    unittest.main()