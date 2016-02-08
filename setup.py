from distutils.cmd import Command
from distutils.core import setup

from run_tests import run_tests


class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        run_tests()


setup(
    name='rational',
    version='1.0.0',
    packages=['rational', 'test_rational'],
    url='https://github.com/daniel-dinu/rational-python',
    license='MIT',
    author='Daniel Dinu',
    author_email='dumitru-daniel.dinu@uni.lu',
    description='Support for rational numbers',
    cmdclass={'test': TestCommand}
)
