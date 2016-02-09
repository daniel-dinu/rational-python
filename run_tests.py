import sys
import unittest2


__author__ = 'Daniel Dinu'


def run_tests():
        test_suites = unittest2.TestLoader().discover('.')
        unittest2.TextTestRunner(verbosity=2).run(test_suites)


if '__main__' == __name__:
    run_tests()
