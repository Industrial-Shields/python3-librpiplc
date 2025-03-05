#!/bin/bash

python -m mypy --pretty --config-file mypy.ini librpiplc/ setup.py && python -m pyright --pythonversion 3.9 librpiplc/ setup.py
