#!/bin/bash

set -e
set -x

# Activate virtual environment
source ~/.venv/bin/activate

coverage run -m test_rational.test_rational
codecov