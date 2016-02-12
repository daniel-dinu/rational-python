#!/bin/bash

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
else
    # Install some custom requirements on Linux
    echo "Linux"

    pip install virtualenv
fi

# Activate virtual environment
source ~/.venv/bin/activate
