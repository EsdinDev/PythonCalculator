import sys
import os
import unittest

# Ensure the src directory is in the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from PythonCalculator import PythonCalculator

class TestPythonCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = PythonCalculator()

    def test_sumar(self):
        self.assertEqual(self.calc.sumar(1, 2), 3)
        self.assertEqual(self.calc.sumar(-1, 1), 0)
        self.assertEqual(self.calc.sumar(-1, -1), -2)

    def test_restar(self):
        self.assertEqual(self.calc.restar(10, 5), 5)
        self.assertEqual(self.calc.restar(-1, 1), -2)
        self.assertEqual(self.calc.restar(-1, -1), 0)

    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(3, 7), 21)
        self.assertEqual(self.calc.multiplicar(-1, 1), -1)
        self.assertEqual(self.calc.multiplicar(-1, -1), 1)

    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)
        self.assertEqual(self.calc.dividir(-1, 1), -1)
        self.assertEqual(self.calc.dividir(-1, -1), 1)
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

if __name__ == '__main__':
    unittest.main()