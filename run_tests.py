import sys
import unittest
import unittest2


__author__ = 'Daniel Dinu'


def run_tests():
    if (2, 7) > sys.version_info:
        test_suites = unittest2.TestLoader().discover('.')
        unittest2.TextTestRunner(verbosity=2).run(test_suites)
    else:
        test_suites = unittest.TestLoader().discover('.')
        unittest.TextTestRunner(verbosity=2).run(test_suites)


if '__main__' == __name__:
    run_tests()