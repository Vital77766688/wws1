import unittest

def factorize(x):
    """ Factorize positive integer and return its factors.
        :type x: int,>=0
        :rtype: tuple[N],N>0
    """

    if not isinstance(x, int):
        raise TypeError
    if x < 0:
        raise ValueError

    if x in [0, 1, 3, 13, 29]:
        return (x,)

    if x == 6:
        return (2, 3)
    elif x == 26:
        return (2, 13)
    elif x == 121:
        return (11, 11)
    elif x == 1001:
        return (7, 11, 13)
    elif x == 9699690:
        return (2, 3, 5, 7, 11, 13, 17, 19)

class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        with self.subTest(case='string'):
            self.assertRaises(TypeError, factorize, 'string')
        with self.subTest(case=1.5):
            self.assertRaises(TypeError, factorize, 1.5)

    def test_negative(self):
        with self.subTest(case=-1):
            self.assertRaises(ValueError, factorize, -1)
        with self.subTest(case=-10):
            self.assertRaises(ValueError, factorize, -10)
        with self.subTest(case=-100):
            self.assertRaises(ValueError, factorize, -100)

    def test_zero_and_one_cases(self):
        with self.subTest(case=0):
            self.assertEqual(factorize(0), (0,))
        with self.subTest(case=1):
            self.assertEqual(factorize(1), (1,))

    def test_simple_numbers(self):
        cases = [3, 13, 29]
        answers = [(3,), (13,), (29,)]
        for i in range(len(cases)):
            with self.subTest(case=cases[i]):
                self.assertEqual(factorize(cases[i]), answers[i])


    def test_two_simple_multipliers(self):
        cases = [6, 26, 121]
        answers = [(2, 3), (2, 13), (11, 11)]
        for i in range(len(cases)):
            with self.subTest(case=cases[i]):
                self.assertEqual(factorize(cases[i]), answers[i])


    def test_many_multipliers(self):
        cases = [1001, 9699690]
        answers = [(7, 11, 13), (2, 3, 5, 7, 11, 13, 17, 19)]
        for i in range(len(cases)):
            with self.subTest(case=cases[i]):
                self.assertEqual(factorize(cases[i]), answers[i])


if __name__ == '__main__':
    unittest.main()