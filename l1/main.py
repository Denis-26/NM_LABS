import gorner
from derivative import derivative
import unittest


class Test(unittest.TestCase):
    def test_upper_border(self):
        upper = gorner.upper_border([2, -4, 5, -2])
        print("\nUpper border: {}".format(upper))
        self.assertEqual(upper, 3)

    def test_lower_border(self):
        lower = gorner.lower_border([2, -4, 5, -2])
        print("\nLower border: {}".format(lower))
        self.assertEqual(gorner.lower_border([2, -4, 5, -2]), -1)

    def test_derivative(self):
        der = derivative([2,3,4,3])
        print("\nDeriviate: {}".format(der))
        self.assertEqual(der, [6, 6, 4, 0])

if __name__ == "__main__":
    unittest.main()
