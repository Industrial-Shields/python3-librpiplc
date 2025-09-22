#!/bin/bash
set -eu

ruff check librpiplc/

ruff format

mypy --pretty --config-file mypy.ini librpiplc/ setup.py
