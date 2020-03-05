import prettify
import unittest


class KnownValues(unittest.TestCase):
    known_values = ((1000000, '1M'),
                    (2500000.34, '2.5M'),
                    (532, '532'),
                    (1123456789, '1.1B'),
                    (9487634567534, '9.5T'),
                    (199000, '199,000'),
                    (0, '0'),
                    (-1000, '-1,000'),
                    (18599.784, '18,599.784'))

    def test_prettify_number_known_values(self):
        '''prettify.number should give known results with valid input'''
        for number, string in self.known_values:
            self.assertEqual(prettify.number(number), string)


class BadInput(unittest.TestCase):
    def test_invalid_input(self):
        '''prettify.number should raise an exception with text input'''
        self.assertRaises(TypeError, prettify.number, 'foo')

    def test_out_of_range_input(self):
        '''prettify.number should raise an exception with out of range input'''
        self.assertRaises(ValueError, prettify.number, 1000000000000000)


if __name__ == '__main__':
    unittest.main()
