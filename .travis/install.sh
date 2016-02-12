#!/bin/bash

set -e
set -x

if [[ "$(uname -s)" == 'Darwin' ]]; then
    echo "D"
else
    echo "L"
fi

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
    echo "OSX"

    # Install some custom requirements on OS X
    # e.g. brew install pyenv-virtualenv

    # Install pyenv
    git clone https://github.com/yyuu/pyenv.git ~/.pyenv
    PYENV_ROOT="$HOME/.pyenv"
    PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init -)"

    case "${TOXENV}" in
        py32)
            # Install some custom Python 3.2 requirements on OS X
            pyenv install 3.2.6
            pyenv global 3.2.6
            ;;
        py33)
            # Install some custom Python 3.3 requirements on OS X
            pyenv install 3.3.6
            pyenv global 3.3.6
            ;;
    esac

    pyenv rehash
    python -m pip install --user virtualenv
else
    # Install some custom requirements on Linux
    echo "Linux"

    pip install virtualenv
fi

python -m virtualenv ~/.venv

# Activate virtual environment
source ~/.venv/bin/activate

pip install coverage
pip install codecov

pip install -r requirements.txt
