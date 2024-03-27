#!/bin/bash

if [ -z "$1" ]; then
  echo "Argument 1 is missing this is mandatory"
  exit 1
fi

if [ -z "$2" ]; then
  echo "Argument 2 is missing this is mandatory"
  exit 1
fi

arg1=$1
arg2=$2

echo "Argument 1: $arg1"
echo "Argument 2: $arg2"

# Continue with the rest of the script
pipenv run python src/main.py -f $1 -t $2
