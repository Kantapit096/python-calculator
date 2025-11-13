import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add(self):
        self.assertEqual(self.calc.add(4, 0), 4)
        # self.assertEqual(self.calc.add(-1, 'a'), 3)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3,2),1)
        self.assertEqual(self.calc.subtract(10,5),5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 4),8)
        self.assertEqual(self.calc.multiply(5, 3),15)

    def test_divide(self):
        self.assertEqual(self.calc.divide(5, 4),1)
        self.assertEqual(self.calc.divide(8,-4),-2)
        self.assertEqual(self.calc.divide(10, 0),'not divide')

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(9,2),1)
        self.assertEqual(self.calc.modulo(7,5),2)
        self.assertEqual(self.calc.modulo(9,3),0)

if __name__ == '__main__':
    unittest.main()