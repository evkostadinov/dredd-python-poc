#!/usr/bin/env bash
npm install
python -m virtualenv .virtualenv
source .virtualenv/bin/activate
pip install -r requirements.txt
node_modules/dredd/bin/dredd --config dredd.yml --language python  --hookfiles ./hooks.py 