#!/usr/bin/env sh

export FLASK_APP=finclerk
export DATABASE_NAME=instance/finclerk.db
flask init-schema
