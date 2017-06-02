import unittest
import Factorial as fa


class FactorialTest(unittest.TestCase):
    """
    test class
    """

    # starts with 'test_' is test method
    def test_fact(self):
        res = fa.fact(5)
        self.assertEqual(res, 120)


if __name__ == '__main__':
    unittest.main()
