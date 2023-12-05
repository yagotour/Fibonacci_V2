import unittest
from fibo import fibonacci
class TestFibonacci(unittest.TestCase):
    def test_posicion(self):
        result = fibonacci(5)
        self.assertEqual(result, 3)

