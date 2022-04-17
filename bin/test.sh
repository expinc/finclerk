#!/usr/bin/env sh

export PYTHONPATH=$PYTHONPATH:$PWD
export DATABASE_NAME=tmp/test.db
mkdir tmp
pytest --capture=tee-sys $1
rm -rf tmp
