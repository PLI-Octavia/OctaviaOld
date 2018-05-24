#!/bin/bash

LOCALDIR=$(dirname "$0")
cd "${LOCALDIR}"/.. || exit

python3 -m venv envoctavia
source envoctavia/bin/activate
# pip install gunicorn
python envoctavia/bin/pip install --upgrade pip
python envoctavia/bin/pip install -r requirements.txt
python manage.py migrate
# yes | python manage.py collectstatic
deactivate

echo $0