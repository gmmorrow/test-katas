import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(10, 5), 15)
        self.assertEqual(katas.add(4, 2), 6)
        self.assertEqual(katas.add(7, 4), 11)

    def test_multiply(self):
        self.assertEqual(katas.multiply(10, 5), 50)
        self.assertEqual(katas.multiply(7, 4), 28)
        self.assertEqual(katas.multiply(6, 3), 18)

    def test_power(self):
        self.assertEqual(katas.power(2, 3), 8)
        self.assertEqual(katas.power(4, 7), 16384)
        self.assertEqual(katas.power(8, 3), 512)

    def test_factorial(self):
        self.assertEqual(katas.factorial(5), 120)

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(5), 5)


if __name__ == '__main__':
    unittest.main()
