import unittest


__author__ = 'Daniel Dinu'


def run_tests():
    test_suites = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=2).run(test_suites)


if '__main__' == __name__:
    run_tests()