#!/bin/bash

LOCALDIR=$(dirname "$0")
cd "${LOCALDIR}"/.. || exit

python3 -m venv envoctavia
source envoctavia/bin/activate
python envoctavia/bin/pip install --upgrade pip
python envoctavia/bin/pip install -r requirements.txt
deactivate

echo $0