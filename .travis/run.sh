#!/bin/bash

set -e
set -x

#if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
#    # Initialize pyenv
#    PYENV_ROOT="$HOME/.pyenv"
#    PATH="$PYENV_ROOT/bin:$PATH"
#    eval "$(pyenv init -)"
#fi

# Activate virtual environment
source ~/.venv/bin/activate

python --version

python setup.py test
