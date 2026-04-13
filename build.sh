#!/bin/bash
set -e
python3 setup.py build_ext --inplace
rm -rf src/ build/ build.sh
git add -A
git commit -m "ship prebuilt extension"
git push
