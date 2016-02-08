#!/bin/bash

brew update

# install pyenv
git clone https://github.com/yyuu/pyenv.git ~/.pyenv
PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"

case $PYTHON_VERSION in
    3.4)
        pyenv install 3.4.4
        pyenv global 3.4.4
        ;;
    3.5)
        pyenv install 3.5.1
        pyenv global 3.5.1
        ;;
    *)
        echo "Unknown Python version '$PYTHON_VERSION'!"
        exit 1
esac

pyenv rehash
python -m pip install --user virtualenv