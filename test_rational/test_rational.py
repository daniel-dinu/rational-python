import unittest2
from unittest2 import TestCase

from rational.rational import gcd
from rational.rational import Rational


__author__ = 'Daniel Dinu'


class TestRational(TestCase):
    def setUp(self):
        self.known_values = [(1, 2, 1, 2),
                             (-1, 2, -1, 2),
                             (1, -2, -1, 2),
                             (-1, -2, 1, 2),

                             (2, 4, 1, 2),
                             (-2, 4, -1, 2),
                             (2, -4, -1, 2),
                             (-2, -4, 1, 2),

                             (2, 1, 2, 1),
                             (-2, 1, -2, 1),
                             (2, -1, -2, 1),
                             (-2, -1, 2, 1),

                             (4, 2, 2, 1),
                             (-4, 2, -2, 1),
                             (4, -2, -2, 1),
                             (-4, -2, 2, 1)]

    def tearDown(self):
        del self.known_values

    def test_constructor_numerator_type_error(self):
        self.assertRaises(TypeError, Rational, 1.2)

    def test_constructor_denominator_type_error(self):
        self.assertRaises(TypeError, Rational, 1, 1.2)

    def test_constructor_denominator_zero_division_error(self):
        numerator = 1
        denominator = 0
        with self.subTest(numerator=numerator):
            self.assertRaises(ZeroDivisionError, Rational, numerator, denominator)

        numerator = Rational()
        denominator = 0
        with self.subTest(numerator=numerator, denominator=denominator):
            self.assertRaises(ZeroDivisionError, Rational, numerator, denominator)

        numerator = Rational()
        denominator = Rational()
        with self.subTest(numerator=numerator, denominator=denominator):
            self.assertRaises(ZeroDivisionError, Rational, numerator, denominator)

    def test_constructor_numerator(self):
        for numerator, denominator, expected_numerator, expected_denominator in self.known_values:
            with self.subTest(numerator=numerator, denominator=denominator):
                r = Rational(numerator, denominator)
                self.assertEqual(expected_numerator, r.numerator)

    def test_constructor_denominator(self):
        for numerator, denominator, expected_numerator, expected_denominator in self.known_values:
            with self.subTest(numerator=numerator, denominator=denominator):
                r = Rational(numerator, denominator)
                self.assertEqual(expected_denominator, r.denominator)

    def test_constructor_transform(self):
        test_constructor_transform_values = [(Rational(1, 2), Rational(1, 2), Rational(1)),
                                             (Rational(1, 2), Rational(1, 4), Rational(2)),
                                             (Rational(1, 4), Rational(1, 2), Rational(1, 2)),
                                             (Rational(-1, 2), Rational(1, 2), Rational(-1)),
                                             (Rational(-1, 2), Rational(1, 4), Rational(-2)),
                                             (Rational(-1, 4), Rational(1, 2), Rational(-1, 2)),
                                             (Rational(1, 2), Rational(-1, 2), Rational(-1)),
                                             (Rational(1, 2), Rational(-1, 4), Rational(-2)),
                                             (Rational(1, 4), Rational(-1, 2), Rational(-1, 2)),
                                             (Rational(-1, 2), Rational(-1, 2), Rational(1)),
                                             (Rational(-1, 2), Rational(-1, 4), Rational(2)),
                                             (Rational(-1, 4), Rational(-1, 2), Rational(1, 2))]

        for a, b, expected_result in test_constructor_transform_values:
            with self.subTest(a=a, b=b, expected_result=expected_result):
                computed_result = Rational(a, b)
                self.assertEqual(expected_result, computed_result)

    def test_transform(self):
        test_transform_values = [(1, 2, (1, 2)),
                                 (2, 4, (2, 4)),
                                 (-1, 2, (-1, 2)),
                                 (-2, 4, (-2, 4)),
                                 (1, -2, (1, -2)),
                                 (2, -4, (2, -4)),
                                 (-1, -2, (-1, -2)),
                                 (-2, -4, (-2, -4)),

                                 (Rational(1, 2), 1, (1, 2)),
                                 (Rational(1, 2), 2, (1, 4)),
                                 (Rational(-1, 2), 1, (-1, 2)),
                                 (Rational(-1, 2), 2, (-1, 4)),
                                 (Rational(1, -2), 1, (-1, 2)),
                                 (Rational(1, -2), 2, (-1, 4)),
                                 (Rational(1, 2), -1, (1, -2)),
                                 (Rational(1, 2), -2, (1, -4)),
                                 (Rational(-1, 2), -1, (-1, -2)),
                                 (Rational(-1, 2), -2, (-1, -4)),

                                 (1, Rational(1, 2), (2, 1)),
                                 (2, Rational(1, 2), (4, 1)),
                                 (-1, Rational(1, 2), (-2, 1)),
                                 (-2, Rational(1, 2), (-4, 1)),
                                 (1, Rational(-1, 2), (2, -1)),
                                 (2, Rational(-1, 2), (4, -1)),
                                 (1, Rational(1, -2), (2, -1)),
                                 (2, Rational(1, -2), (4, -1)),
                                 (-1, Rational(1, 2), (-2, 1)),
                                 (-2, Rational(1, 2), (-4, 1)),


                                 (Rational(1, 2), Rational(1, 2), (2, 2)),
                                 (Rational(1, 2), Rational(1, 4), (4, 2)),
                                 (Rational(1, 4), Rational(1, 2), (2, 4)),
                                 (Rational(-1, 2), Rational(1, 2), (-2, 2)),
                                 (Rational(-1, 2), Rational(1, 4), (-4, 2)),
                                 (Rational(-1, 4), Rational(1, 2), (-2, 4)),
                                 (Rational(1, 2), Rational(-1, 2), (2, -2)),
                                 (Rational(1, 2), Rational(-1, 4), (4, -2)),
                                 (Rational(1, 4), Rational(-1, 2), (2, -4)),
                                 (Rational(-1, 2), Rational(-1, 2), (-2, -2)),
                                 (Rational(-1, 2), Rational(-1, 4), (-4, -2)),
                                 (Rational(-1, 4), Rational(-1, 2), (-2, -4))]

        for a, b, expected_result in test_transform_values:
            with self.subTest(a=a, b=b, expected_result=expected_result):
                computed_result = Rational.transform(a, b)
                self.assertEqual(expected_result, computed_result)

    def test_gcd(self):
        gcd_test_values = [(0, 0, 0),
                           (0, 1, 1),
                           (1, 0, 1),
                           (0, -1, -1),
                           (-1, 0, -1),
                           (2, 4, 2),
                           (-2, 4, 2),
                           (-2, -4, -2),
                           (42, 30, 6),
                           (42, -30, -6),
                           (-42, -30, -6)]

        for a, b, expected_gcd in gcd_test_values:
            with self.subTest(a=a, b=b, expected_gcd=expected_gcd):
                computed_gcd = gcd(a, b)
                self.assertEqual(expected_gcd, computed_gcd)

    def test_value(self):
        for numerator, denominator, expected_numerator, expected_denominator in self.known_values:
            with self.subTest(numerator=numerator, denominator=denominator):
                r = Rational(numerator, denominator)
                expected_value = expected_numerator / (expected_denominator * 1.0)
                self.assertEqual(expected_value, r.value)

    def test_quotient(self):
        for numerator, denominator, expected_numerator, expected_denominator in self.known_values:
            with self.subTest(numerator=numerator, denominator=denominator):
                r = Rational(numerator, denominator)
                expected_value = expected_numerator // expected_denominator
                self.assertEqual(expected_value, r.quotient)

    def test_remainder(self):
        for numerator, denominator, expected_numerator, expected_denominator in self.known_values:
            with self.subTest(numerator=numerator, denominator=denominator):
                r = Rational(numerator, denominator)
                expected_value = expected_numerator % expected_denominator
                self.assertEqual(expected_value, r.remainder)

    def test_str(self):
        for numerator, denominator, expected_numerator, expected_denominator in self.known_values:
            with self.subTest(numerator=numerator, denominator=denominator):
                r = Rational(numerator, denominator)
                if 1 == expected_denominator:
                    expected_str = '{0}'.format(expected_numerator)
                else:
                    expected_str = '{0}/{1}'.format(expected_numerator, expected_denominator)
                self.assertEqual(expected_str, str(r))

    def test_repr(self):
        for numerator, denominator, expected_numerator, expected_denominator in self.known_values:
            with self.subTest(numerator=numerator, denominator=denominator):
                r = Rational(numerator, denominator)
                expected_repr = 'Rational({0}, {1})'.format(expected_numerator, expected_denominator)
                self.assertEqual(expected_repr, repr(r))

    def test_float(self):
        for numerator, denominator, expected_numerator, expected_denominator in self.known_values:
            with self.subTest(numerator=numerator, denominator=denominator):
                r = Rational(numerator, denominator)
                expected_value = expected_numerator / (expected_denominator * 1.0)
                self.assertEqual(expected_value, float(r))

    def test_int(self):
        for numerator, denominator, expected_numerator, expected_denominator in self.known_values:
            with self.subTest(numerator=numerator, denominator=denominator):
                r = Rational(numerator, denominator)
                expected_value = expected_numerator // expected_denominator
                self.assertEqual(expected_value, int(r))

    def test_neg(self):
        for numerator, denominator, expected_numerator, expected_denominator in self.known_values:
            with self.subTest(numerator=numerator, denominator=denominator):
                r = -Rational(numerator, denominator)
                self.assertEqual(-expected_numerator, r.numerator)
                self.assertEqual(expected_denominator, r.denominator)

    def test_pos(self):
        for numerator, denominator, expected_numerator, expected_denominator in self.known_values:
            with self.subTest(numerator=numerator, denominator=denominator):
                r = +Rational(numerator, denominator)
                self.assertEqual(expected_numerator, r.numerator)
                self.assertEqual(expected_denominator, r.denominator)

    def test_abs(self):
        for numerator, denominator, expected_numerator, expected_denominator in self.known_values:
            with self.subTest(numerator=numerator, denominator=denominator):
                r = abs(Rational(numerator, denominator))
                self.assertEqual(abs(expected_numerator), r.numerator)
                self.assertEqual(expected_denominator, r.denominator)

    def test_invert_zero_division_error(self):
        r = Rational(0)
        with self.assertRaises(ZeroDivisionError):
            ~r

    def test_invert(self):
        for numerator, denominator, expected_numerator, expected_denominator in self.known_values:
            with self.subTest(numerator=numerator, denominator=denominator):
                r = ~Rational(numerator, denominator)

                if 0 > expected_numerator:
                    expected_inverted_numerator = -expected_denominator
                    expected_inverted_denominator = -expected_numerator
                else:
                    expected_inverted_numerator = expected_denominator
                    expected_inverted_denominator = expected_numerator

                self.assertEqual(expected_inverted_numerator, r.numerator)
                self.assertEqual(expected_inverted_denominator, r.denominator)

    def test_lt(self):
        true_test_cases = [(Rational(-1, 2), Rational()),
                           (Rational(), Rational(1, 2)),
                           (Rational(-1, 2), Rational(1, 2)),
                           (Rational(1, 4), Rational(1, 2)),
                           (Rational(-1, 2), Rational(-1, 4))]

        false_test_cases = [(Rational(), Rational()),
                            (Rational(1, 2), Rational()),
                            (Rational(), Rational(-1, 2)),
                            (Rational(-1, 2), Rational(1, -2)),
                            (Rational(1, 2), Rational(2, 4)),
                            (Rational(1, 2), Rational(-1, 2)),
                            (Rational(1, 2), Rational(1, 4)),
                            (Rational(-1, 4), Rational(-1, 2))]

        for r1, r2 in true_test_cases:
            with self.subTest(r1=r1, r2=r2, result=True):
                self.assertTrue(r1 < r2)

        for r1, r2 in false_test_cases:
            with self.subTest(r1=r1, r2=r2, result=False):
                self.assertFalse(r1 < r2)

    def test_le(self):
        true_test_cases = [(Rational(), Rational()),
                           (Rational(-1, 2), Rational()),
                           (Rational(), Rational(1, 2)),
                           (Rational(-1, 2), Rational(1, -2)),
                           (Rational(1, 2), Rational(2, 4)),
                           (Rational(-1, 2), Rational(1, 2)),
                           (Rational(1, 4), Rational(1, 2)),
                           (Rational(-1, 2), Rational(-1, 4))]

        false_test_cases = [(Rational(1, 2), Rational()),
                            (Rational(), Rational(-1, 2)),
                            (Rational(1, 2), Rational(-1, 2)),
                            (Rational(1, 2), Rational(1, 4)),
                            (Rational(-1, 4), Rational(-1, 2))]

        for r1, r2 in true_test_cases:
            with self.subTest(r1=r1, r2=r2, result=True):
                self.assertTrue(r1 <= r2)

        for r1, r2 in false_test_cases:
            with self.subTest(r1=r1, r2=r2, result=False):
                self.assertFalse(r1 <= r2)

    def test_eq(self):
        true_test_cases = [(Rational(), Rational()),
                           (Rational(-1, 2), Rational(1, -2)),
                           (Rational(1, 2), Rational(2, 4))]

        false_test_cases = [(Rational(-1, 2), Rational()),
                            (Rational(), Rational(1, 2)),
                            (Rational(1, 2), Rational()),
                            (Rational(), Rational(-1, 2)),
                            (Rational(-1, 2), Rational(1, 2)),
                            (Rational(1, 4), Rational(1, 2)),
                            (Rational(-1, 2), Rational(-1, 4)),
                            (Rational(1, 2), Rational(-1, 2)),
                            (Rational(1, 2), Rational(1, 4)),
                            (Rational(-1, 4), Rational(-1, 2))]

        for r1, r2 in true_test_cases:
            with self.subTest(r1=r1, r2=r2, result=True):
                self.assertTrue(r1 == r2)

        for r1, r2 in false_test_cases:
            with self.subTest(r1=r1, r2=r2, result=False):
                self.assertFalse(r1 == r2)

    def test_neq(self):
        true_test_cases = [(Rational(-1, 2), Rational()),
                           (Rational(), Rational(1, 2)),
                           (Rational(1, 2), Rational()),
                           (Rational(), Rational(-1, 2)),
                           (Rational(-1, 2), Rational(1, 2)),
                           (Rational(1, 4), Rational(1, 2)),
                           (Rational(-1, 2), Rational(-1, 4)),
                           (Rational(1, 2), Rational(-1, 2)),
                           (Rational(1, 2), Rational(1, 4)),
                           (Rational(-1, 4), Rational(-1, 2))]

        false_test_cases = [(Rational(), Rational()),
                            (Rational(-1, 2), Rational(1, -2)),
                            (Rational(1, 2), Rational(2, 4))]

        for r1, r2 in true_test_cases:
            with self.subTest(r1=r1, r2=r2, result=True):
                self.assertTrue(r1 != r2)

        for r1, r2 in false_test_cases:
            with self.subTest(r1=r1, r2=r2, result=False):
                self.assertFalse(r1 != r2)

    def test_ge(self):
        true_test_cases = [(Rational(), Rational()),
                           (Rational(1, 2), Rational()),
                           (Rational(), Rational(-1, 2)),
                           (Rational(-1, 2), Rational(1, -2)),
                           (Rational(1, 2), Rational(2, 4)),
                           (Rational(1, 2), Rational(-1, 2)),
                           (Rational(1, 2), Rational(1, 4)),
                           (Rational(-1, 4), Rational(-1, 2))]

        false_test_cases = [(Rational(-1, 2), Rational()),
                            (Rational(), Rational(1, 2)),
                            (Rational(-1, 2), Rational(1, 2)),
                            (Rational(1, 4), Rational(1, 2)),
                            (Rational(-1, 2), Rational(-1, 4))]

        for r1, r2 in true_test_cases:
            with self.subTest(r1=r1, r2=r2, result=True):
                self.assertTrue(r1 >= r2)

        for r1, r2 in false_test_cases:
            with self.subTest(r1=r1, r2=r2, result=False):
                self.assertFalse(r1 >= r2)

    def test_gt(self):
        true_test_cases = [(Rational(1, 2), Rational()),
                           (Rational(), Rational(-1, 2)),
                           (Rational(1, 2), Rational(-1, 2)),
                           (Rational(1, 2), Rational(1, 4)),
                           (Rational(-1, 4), Rational(-1, 2))]

        false_test_cases = [(Rational(), Rational()),
                            (Rational(-1, 2), Rational()),
                            (Rational(), Rational(1, 2)),
                            (Rational(-1, 2), Rational(1, -2)),
                            (Rational(1, 2), Rational(2, 4)),
                            (Rational(-1, 2), Rational(1, 2)),
                            (Rational(1, 4), Rational(1, 2)),
                            (Rational(-1, 2), Rational(-1, 4))]

        for r1, r2 in true_test_cases:
            with self.subTest(r1=r1, r2=r2, result=True):
                self.assertTrue(r1 > r2)

        for r1, r2 in false_test_cases:
            with self.subTest(r1=r1, r2=r2, result=False):
                self.assertFalse(r1 > r2)

    def test_add_type_error(self):
        r = Rational()
        with self.assertRaises(TypeError):
            r + 1.2

    def test_add(self):
        add_test_values = [(Rational(), Rational(1, 2), Rational(1, 2)),
                           (Rational(1, 2), Rational(), Rational(1, 2)),
                           (Rational(1, 2), Rational(1, 2), Rational(1, 1)),
                           (Rational(1, 2), Rational(-1, 2), Rational(0, 1)),
                           (Rational(1, 4), Rational(2, 4), Rational(3, 4)),
                           (Rational(1, 4), Rational(3, 4), Rational(1, 1)),
                           (Rational(1, 4), Rational(-3, 4), Rational(-1, 2)),
                           (Rational(1, 2), Rational(1, 3), Rational(5, 6)),
                           (Rational(2), -1, Rational(1)),
                           (Rational(2), 1, Rational(3))]

        for r1, r2, expected_r in add_test_values:
            with self.subTest(r1=r1, r2=r2, expected_r=expected_r):
                r = r1 + r2
                self.assertEqual(expected_r, r)

    def test_sub_type_error(self):
        r = Rational()
        with self.assertRaises(TypeError):
            r - 1.2

    def test_sub(self):
        sub_test_values = [(Rational(), Rational(1, 2), Rational(-1, 2)),
                           (Rational(1, 2), Rational(), Rational(1, 2)),
                           (Rational(1, 2), Rational(1, 2), Rational(0, 1)),
                           (Rational(1, 2), Rational(-1, 2), Rational(1, 1)),
                           (Rational(1, 4), Rational(2, 4), Rational(-1, 4)),
                           (Rational(1, 4), Rational(3, 4), Rational(-1, 2)),
                           (Rational(1, 4), Rational(-3, 4), Rational(1, 1)),
                           (Rational(1, 2), Rational(1, 3), Rational(1, 6)),
                           (Rational(2), -1, Rational(3)),
                           (Rational(2), 1, Rational(1))]

        for r1, r2, expected_r in sub_test_values:
            with self.subTest(r1=r1, r2=r2, expected_r=expected_r):
                r = r1 - r2
                self.assertEqual(expected_r, r)

    def test_mul_type_error(self):
        r = Rational()
        with self.assertRaises(TypeError):
            r * 1.2

    def test_mul(self):
        mul_test_values = [(Rational(), Rational(1, 2), Rational()),
                           (Rational(1, 2), Rational(), Rational()),
                           (Rational(1, 2), Rational(1, 2), Rational(1, 4)),
                           (Rational(1, 2), Rational(-1, 2), Rational(-1, 4)),
                           (Rational(1, 4), Rational(2, 4), Rational(1, 8)),
                           (Rational(1, 4), Rational(3, 4), Rational(3, 16)),
                           (Rational(1, 4), Rational(-3, 4), Rational(-3, 16)),
                           (Rational(1, 2), Rational(1, 3), Rational(1, 6)),
                           (Rational(2), 1, Rational(2)),
                           (Rational(2), -1, Rational(-2))]

        for r1, r2, expected_r in mul_test_values:
            with self.subTest(r1=r1, r2=r2, expected_r=expected_r):
                r = r1 * r2
                self.assertEqual(expected_r, r)

    def test_truediv_zero_division_error(self):
        r1 = Rational(1, 2)
        r2 = Rational()
        with self.assertRaises(ZeroDivisionError):
            r1 / r2

    def test_truediv_type_error(self):
        r = Rational()
        with self.assertRaises(TypeError):
            r / 1.2

    def test_truediv(self):
        div_test_values = [(Rational(), Rational(1, 2), Rational()),
                           (Rational(1, 2), Rational(1, 2), Rational(1, 1)),
                           (Rational(1, 2), Rational(-1, 2), Rational(-1, 1)),
                           (Rational(1, 4), Rational(2, 4), Rational(1, 2)),
                           (Rational(1, 4), Rational(3, 4), Rational(1, 3)),
                           (Rational(1, 4), Rational(-3, 4), Rational(-1, 3)),
                           (Rational(1, 2), Rational(1, 3), Rational(3, 2)),
                           (Rational(2), 1, Rational(2)),
                           (Rational(2), -1, Rational(-2))]

        for r1, r2, expected_r in div_test_values:
            with self.subTest(r1=r1, r2=r2, expected_r=expected_r):
                r = r1 / r2
                self.assertEqual(expected_r, r)

    def test_pow_zero_division_error(self):
        r = Rational()
        for power in range(-3, 0):
            with self.subTest(r=r, power=power):
                with self.assertRaises(ZeroDivisionError):
                    r ** power

    def test_pow_type_error(self):
        r = Rational()
        with self.assertRaises(TypeError):
            r ** 1.2

    def test_pow(self):
        pow_test_values = [(Rational(), 0, Rational()),
                           (Rational(), 1, Rational()),
                           (Rational(), 2, Rational()),
                           (Rational(), 3, Rational()),

                           (Rational(1, 2), -3, Rational(8, 1)),
                           (Rational(1, 2), -2, Rational(4, 1)),
                           (Rational(1, 2), -1, Rational(2, 1)),
                           (Rational(1, 2), 0, Rational(1, 1)),
                           (Rational(1, 2), 1, Rational(1, 2)),
                           (Rational(1, 2), 2, Rational(1, 4)),
                           (Rational(1, 2), 3, Rational(1, 8)),

                           (Rational(-1, 2), -3, Rational(-8, 1)),
                           (Rational(-1, 2), -2, Rational(4, 1)),
                           (Rational(-1, 2), -1, Rational(-2, 1)),
                           (Rational(-1, 2), 0, Rational(1, 1)),
                           (Rational(-1, 2), 1, Rational(-1, 2)),
                           (Rational(-1, 2), 2, Rational(1, 4)),
                           (Rational(-1, 2), 3, Rational(-1, 8)),

                           (Rational(1, 3), -3, Rational(27, 1)),
                           (Rational(1, 3), -2, Rational(9, 1)),
                           (Rational(1, 3), -1, Rational(3, 1)),
                           (Rational(1, 3), 0, Rational(1, 1)),
                           (Rational(1, 3), 1, Rational(1, 3)),
                           (Rational(1, 3), 2, Rational(1, 9)),
                           (Rational(1, 3), 3, Rational(1, 27)),

                           (Rational(-1, 3), -3, Rational(-27, 1)),
                           (Rational(-1, 3), -2, Rational(9, 1)),
                           (Rational(-1, 3), -1, Rational(-3, 1)),
                           (Rational(-1, 3), 0, Rational(1, 1)),
                           (Rational(-1, 3), 1, Rational(-1, 3)),
                           (Rational(-1, 3), 2, Rational(1, 9)),
                           (Rational(-1, 3), 3, Rational(-1, 27))]

        for r1, power, expected_r in pow_test_values:
            with self.subTest(r1=r1, power=power, expected_r=expected_r):
                r = r1 ** power
                self.assertEqual(expected_r, r)

    def test_radd_type_error(self):
        r = Rational()
        with self.assertRaises(TypeError):
            1.2 + r

    def test_radd(self):
        radd_test_values = [(1, Rational(1, 2), Rational(3, 2)),
                            (1, Rational(), Rational(1, 1)),
                            (-1, Rational(1, 2), Rational(-1, 2)),
                            (1, Rational(-1, 2), Rational(1, 2)),
                            (1, Rational(2, 4), Rational(3, 2)),
                            (1, Rational(3, 4), Rational(7, 4)),
                            (1, Rational(-3, 4), Rational(1, 4)),
                            (1, Rational(1, 3), Rational(4, 3))]

        for r1, r2, expected_r in radd_test_values:
            with self.subTest(r1=r1, r2=r2, expected_r=expected_r):
                r = r1 + r2
                self.assertEqual(expected_r, r)

    def test_rsub_type_error(self):
        r = Rational()
        with self.assertRaises(TypeError):
            1.2 - r

    def test_rsub(self):
        rsub_test_values = [(1, Rational(1, 2), Rational(1, 2)),
                            (1, Rational(), Rational(1, 1)),
                            (-1, Rational(1, 2), Rational(-3, 2)),
                            (1, Rational(-1, 2), Rational(3, 2)),
                            (1, Rational(2, 4), Rational(1, 2)),
                            (1, Rational(3, 4), Rational(1, 4)),
                            (1, Rational(-3, 4), Rational(7, 4)),
                            (1, Rational(1, 3), Rational(2, 3))]

        for r1, r2, expected_r in rsub_test_values:
            with self.subTest(r1=r1, r2=r2, expected_r=expected_r):
                r = r1 - r2
                self.assertEqual(expected_r, r)

    def test_rmul_type_error(self):
        r = Rational()
        with self.assertRaises(TypeError):
            1.2 * r

    def test_rmul(self):
        rmul_test_values = [(1, Rational(1, 2), Rational(1, 2)),
                            (1, Rational(), Rational(0, 1)),
                            (-1, Rational(1, 2), Rational(-1, 2)),
                            (1, Rational(-1, 2), Rational(-1, 2)),
                            (1, Rational(2, 4), Rational(1, 2)),
                            (1, Rational(3, 4), Rational(3, 4)),
                            (1, Rational(-3, 4), Rational(-3, 4)),
                            (1, Rational(1, 3), Rational(1, 3))]

        for r1, r2, expected_r in rmul_test_values:
            with self.subTest(r1=r1, r2=r2, expected_r=expected_r):
                r = r1 * r2
                self.assertEqual(expected_r, r)

    def test_rtruediv_zero_division_error(self):
        r = Rational()
        with self.assertRaises(ZeroDivisionError):
            1 / r

    def test_rtruediv_type_error(self):
        r = Rational()
        with self.assertRaises(TypeError):
            1.2 / r

    def test_rtruediv(self):
        rdiv_test_values = [(1, Rational(1, 2), Rational(2, 1)),
                            (-1, Rational(1, 2), Rational(-2, 1)),
                            (1, Rational(-1, 2), Rational(-2, 1)),
                            (1, Rational(2, 4), Rational(2, 1)),
                            (1, Rational(3, 4), Rational(4, 3)),
                            (1, Rational(-3, 4), Rational(-4, 3)),
                            (1, Rational(1, 3), Rational(3, 1))]

        for r1, r2, expected_r in rdiv_test_values:
            with self.subTest(r1=r1, r2=r2, expected_r=expected_r):
                r = r1 / r2
                self.assertEqual(expected_r, r)

    def test_rpow_zero_division_error(self):
        base = 0
        for denominator in range(-3, 0):
            power = Rational(1, denominator)
            with self.subTest(base=base, power=power):
                with self.assertRaises(ZeroDivisionError):
                    base ** power

    def test_rpow_value_error(self):
        rpow_test_values = [(-2, Rational(1, 2)),
                            (-1, Rational(1, 2)),
                            (-3, Rational(-1, 2)),
                            (-2, Rational(-1, 2)),
                            (-1, Rational(-1, 2)),
                            (-3, Rational(1, 3)),
                            (-2, Rational(1, 3)),
                            (-1, Rational(1, 3)),
                            (-3, Rational(-1, 3)),
                            (-2, Rational(-1, 3)),
                            (-1, Rational(-1, 3))]

        for base, power in rpow_test_values:
            with self.subTest(base=base, power=power):
                with self.assertRaises(ValueError):
                    base ** power

    def test_rpow(self):
        rpow_test_values = [(0, Rational(), 1),
                            (1, Rational(), 1),
                            (2, Rational(), 1),
                            (3, Rational(), 1),

                            (0, Rational(1, 2), 0),
                            (1, Rational(1, 2), 1),
                            (2, Rational(1, 2), 1.4142135623730951),
                            (3, Rational(1, 2), 1.7320508075688772),

                            (1, Rational(-1, 2), 1),
                            (2, Rational(-1, 2), 0.7071067811865476),
                            (3, Rational(-1, 2), 0.5773502691896257),

                            (0, Rational(1, 3), 0),
                            (1, Rational(1, 3), 1),
                            (2, Rational(1, 3), 1.2599210498948732),
                            (3, Rational(1, 3), 1.4422495703074083),

                            (1, Rational(-1, 3), 1),
                            (2, Rational(-1, 3), 0.7937005259840998),
                            (3, Rational(-1, 3), 0.6933612743506348),

                            (-1, Rational(1), -1),
                            (-2, Rational(1), -2),
                            (-1, Rational(-1), -1),
                            (-2, Rational(-2), 0.25)]

        for base, power, expected_power in rpow_test_values:
            with self.subTest(base=base, power=power, expected_power=expected_power):
                computed_power = base ** power
                self.assertAlmostEqual(expected_power, computed_power)


if '__main__' == __name__:
    unittest2.main()
