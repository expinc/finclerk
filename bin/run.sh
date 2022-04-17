#!/usr/bin/env sh

export DATABASE_NAME=instance/finclerk.db
waitress-serve --call 'finclerk:create_app'
