#!/bin/bash
set -e
python3 setup.py build_ext --inplace
rm -rf src/ build/ build.sh
