#!/bin/bash

set -e
set -x

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
    # Install some custom requirements on OS X

    # Install pyenv
    git clone https://github.com/yyuu/pyenv.git ~/.pyenv
    PYENV_ROOT="$HOME/.pyenv"
    PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init -)"

    case "${TOXENV}" in
        py26|py27)
            curl -O https://bootstrap.pypa.io/get-pip.py
            python get-pip.py --user
            ;;
        py33)
            pyenv install 3.3.6
            pyenv global 3.3.6
            ;;
        py34)
            pyenv install 3.4.4
            pyenv global 3.4.4
            ;;
        py35)
            pyenv install 3.5.1
            pyenv global 3.5.1
            ;;
    esac

    pyenv rehash
    python -m pip install --user virtualenv
else
    # Install some custom requirements on Linux

    pip install virtualenv
fi

python -m virtualenv ~/.venv

# Activate virtual environment
source ~/.venv/bin/activate

pip install coverage
pip install codecov

pip install -r requirements.txt
