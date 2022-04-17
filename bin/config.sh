#!/usr/bin/env sh

token=$(python -c 'import secrets; print(secrets.token_hex())')
echo SECRET_KEY = \'$token\' > $1/config.py
