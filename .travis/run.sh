#!/bin/bash

set -e
set -x

# Activate virtual environment
source ~/.venv/bin/activate

python --version

python setup.py test
