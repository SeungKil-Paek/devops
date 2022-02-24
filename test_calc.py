import unittest
from unittest.mock import MagicMock, patch
import calc


class testCalc(unittest.TestCase):
    def test_sum(self):
        result = calc.sum(3, 7)
        self.assertEqual(10, result)

    def test_minus(self):
        self.assertEqual(5, calc.minus(10, 5))

    @patch("calc.api", return_value=2)
    def test_sum2(self, mock):
        self.assertEqual(2, calc.api())

    @patch("calc.api")
    def test_sum3(self, mock):
        mock.return_value = 2
        self.assertEqual(7, calc.sumWithApi(5))

    def test_sum2_(self):
        self.assertEqual(2, calc.api())
