#!/bin/bash

#!/bin/bash

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then

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

    # Activate virtual environment
    source ~/.venv/bin/activate
else
    # Install some custom requirements on Linux
fi
