import unittest
from unittest import TestCase
from unittest.mock import patch

from Bezdelushka import *


class TestCalculatorClass(TestCase):

    def setUp(self):
        self.calculator = CalculatorClass()

    def test_plus(self):
        self.assertEqual(self.calculator.plus(), "5.0 + 6.0 = 11.0")

    def test_minus(self):
        self.assertEqual(self.calculator.minus(), "7.0 - 3.0 = 4.0")

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(), "8.0 * 9.0 = 72.0")

    def test_divide(self):
        self.assertEqual(self.calculator.divide(), "12.0 / 3.0 = 4.0")

    def test_modulo(self):
        self.assertEqual(self.calculator.modulo(), "15.0 % 4.0 = 3.0")

    def test_power(self):
        self.assertEqual(self.calculator.power(), "2.0 ** 3.0 = 8.0")

    def test_floor_divide(self):
        self.assertEqual(self.calculator.floor_divide(), "13.0 // 5.0 = 2.0")


class TestMathematicalClass(TestCase):

    def setUp(self):
        self.mathematical = MathematicalClass()

    def test_table(self):
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = ["1"]
            self.mathematical.table()

    def test_procent_stavka(self):
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = ["10", "100", "50"]
            self.assertEqual(self.mathematical.procent_stavka(), '(110, 50)')

    def test_injiner_calculator(self):
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = ["1", "90"]
            self.assertAlmostEqual(self.mathematical.injiner_calculator(), 0.00)


class TestProgrammClass(TestCase):

    def setUp(self):
        self.programm = ProgrammClass()

    def test_golos(self):
        with patch('builtins.input') as mock_input:
            mock_input.return_value = "Привет"
            self.programm.golos()


class TestSpeedTest(TestCase):

    def setUp(self):
        self.speed_test = SpeedTest()

    def test_humansize(self):
        self.assertEqual(self.speed_test.humansize(1024), '1.00 KB')
        self.assertEqual(self.speed_test.humansize(1048576), '1.00 MB')
        self.assertEqual(self.speed_test.humansize(1073741824), '1.00 GB')


if __name__ == '__main__':
    unittest.main()
