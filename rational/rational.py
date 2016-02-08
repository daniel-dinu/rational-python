__author__ = 'Daniel Dinu'


NUMERATOR_STR_FORMAT = '{}'
RATIONAL_STR_FORMAT = '{}/{}'

RATIONAL_REPR_FORMAT = '{}({}, {})'

NUMERATOR_TYPE_ERROR_MESSAGE = 'The numerator of a rational must be a rational or an integer value!'
DENOMINATOR_TYPE_ERROR_MESSAGE = 'The denominator of a rational must be a rational or an integer value!'

DENOMINATOR_ZERO_DIVISION_ERROR_MESSAGE = 'The denominator of a rational number can not be zero!'

DIVIDER_ZERO_DIVISION_ERROR_MESSAGE = 'The divider cannot be 0!'

ZERO_TO_NEGATIVE_POWER_ZERO_DIVISION_ERROR_MESSAGE = '0 cannot be raised to a negative power!'

FIRST_TERM_TYPE_ERROR_MESSAGE = 'The first term must be a rational or an integer value!'
SECOND_TERM_TYPE_ERROR_MESSAGE = 'The second term must be a rational or an integer value!'


def gcd(a, b):
    while 0 != b:
        r = a % b
        a = b
        b = r

    return a


class Rational:
    def __init__(self, numerator=0, denominator=1):
        if not isinstance(numerator, Rational) and not isinstance(numerator, int):
            raise TypeError(NUMERATOR_TYPE_ERROR_MESSAGE)

        if not isinstance(numerator, Rational) and not isinstance(denominator, int):
            raise TypeError(DENOMINATOR_TYPE_ERROR_MESSAGE)

        if isinstance(denominator, int) and 0 == denominator:
            raise ZeroDivisionError(DENOMINATOR_ZERO_DIVISION_ERROR_MESSAGE)

        if isinstance(denominator, Rational) and 0 == denominator.numerator:
            raise ZeroDivisionError(DENOMINATOR_ZERO_DIVISION_ERROR_MESSAGE)

        if isinstance(numerator, Rational) or isinstance(denominator, Rational):
            numerator, denominator = self.transform(numerator, denominator)

        divisor = gcd(numerator, denominator)

        self.__numerator = numerator // divisor
        self.__denominator = denominator // divisor

    @staticmethod
    def transform(a, b):
        if isinstance(a, Rational):
            numerator = a.numerator
            denominator = a.denominator
        else:
            numerator = a
            denominator = 1

        if isinstance(b, Rational):
            numerator *= b.denominator
            denominator *= b.numerator
        else:
            denominator *= b

        return numerator, denominator

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    @property
    def value(self):
        return self.__numerator / self.__denominator

    @property
    def quotient(self):
        return self.__numerator // self.__denominator

    @property
    def remainder(self):
        return self.__numerator % self.__denominator

    def __str__(self):
        if 1 == self.__denominator:
            return NUMERATOR_STR_FORMAT.format(self.__numerator)
        else:
            return RATIONAL_STR_FORMAT.format(self.__numerator, self.__denominator)

    def __repr__(self):
        return RATIONAL_REPR_FORMAT.format(self.__class__.__name__, self.__numerator, self.__denominator)

    def __float__(self):
        return self.__numerator / self.__denominator

    def __int__(self):
        return self.__numerator // self.__denominator

    def __neg__(self):
        return Rational(-self.__numerator, self.__denominator)

    def __pos__(self):
        return Rational(self.__numerator, self.__denominator)

    def __abs__(self):
        return Rational(abs(self.__numerator), self.__denominator)

    def __invert__(self):
        return Rational(self.__denominator, self.__numerator)

    def __lt__(self, other):
        return self.__numerator * other.__denominator < self.__denominator * other.__numerator

    def __le__(self, other):
        return self.__numerator * other.__denominator <= self.__denominator * other.__numerator

    def __eq__(self, other):
        return self.__numerator * other.__denominator == self.__denominator * other.__numerator

    def __ne__(self, other):
        return self.__numerator * other.__denominator != self.__denominator * other.__numerator

    def __ge__(self, other):
        return self.__numerator * other.__denominator >= self.__denominator * other.__numerator

    def __gt__(self, other):
        return self.__numerator * other.__denominator > self.__denominator * other.__numerator

    def __add__(self, other):
        if not isinstance(other, Rational) and not isinstance(other, int):
            raise TypeError(SECOND_TERM_TYPE_ERROR_MESSAGE)

        if isinstance(other, int):
            other = Rational(other)

        numerator = self.__numerator * other.__denominator + self.__denominator * other.__numerator
        denominator = self.__denominator * other.__denominator

        return Rational(numerator, denominator)

    def __sub__(self, other):
        if not isinstance(other, Rational) and not isinstance(other, int):
            raise TypeError(SECOND_TERM_TYPE_ERROR_MESSAGE)

        if isinstance(other, int):
            other = Rational(other)

        numerator = self.__numerator * other.__denominator - self.__denominator * other.__numerator
        denominator = self.__denominator * other.__denominator

        return Rational(numerator, denominator)

    def __mul__(self, other):
        if not isinstance(other, Rational) and not isinstance(other, int):
            raise TypeError(SECOND_TERM_TYPE_ERROR_MESSAGE)

        if isinstance(other, int):
            other = Rational(other)

        numerator = self.__numerator * other.__numerator
        denominator = self.__denominator * other.__denominator

        return Rational(numerator, denominator)

    def __truediv__(self, other):
        if not isinstance(other, Rational) and not isinstance(other, int):
            raise TypeError(SECOND_TERM_TYPE_ERROR_MESSAGE)

        if isinstance(other, int):
            other = Rational(other)

        if 0 == other.__numerator:
            raise ZeroDivisionError(DIVIDER_ZERO_DIVISION_ERROR_MESSAGE)

        numerator = self.__numerator * other.__denominator
        denominator = self.__denominator * other.__numerator

        return Rational(numerator, denominator)

    def __pow__(self, power):
        if not isinstance(power, int):
            raise TypeError(FIRST_TERM_TYPE_ERROR_MESSAGE)

        if 0 > power and 0 == self.__numerator:
            raise ZeroDivisionError(ZERO_TO_NEGATIVE_POWER_ZERO_DIVISION_ERROR_MESSAGE)

        if 0 == power and 0 == self.__numerator:
            return Rational(self.__numerator, self.__denominator)

        if 0 > power:
            numerator = self.__denominator ** -power
            denominator = self.__numerator ** -power
        else:
            numerator = self.__numerator ** power
            denominator = self.__denominator ** power

        return Rational(numerator, denominator)

    def __radd__(self, other):
        if not isinstance(other, int):
            raise TypeError(FIRST_TERM_TYPE_ERROR_MESSAGE)
        else:
            return Rational(other) + self

    def __rsub__(self, other):
        if not isinstance(other, int):
            raise TypeError(FIRST_TERM_TYPE_ERROR_MESSAGE)
        else:
            return Rational(other) - self

    def __rmul__(self, other):
        if not isinstance(other, int):
            raise TypeError(FIRST_TERM_TYPE_ERROR_MESSAGE)
        else:
            return Rational(other) * self

    def __rtruediv__(self, other):
        if not isinstance(other, int):
            raise TypeError(FIRST_TERM_TYPE_ERROR_MESSAGE)
        else:
            return Rational(other) / self

    def __rpow__(self, power):
        return power ** self.value
