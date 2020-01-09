#! /bin/sh

if [ -e ".python-version" ]
then
  eval "$(pyenv init -)"
  pyenv activate $(cat ".python-version")
fi

make test
