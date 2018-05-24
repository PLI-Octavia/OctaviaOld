#!/bin/bash

LOCALDIR=$(dirname "$0")
echo "${LOCALDIR}"
cd "${LOCALDIR}"/.. || exit

source envoctavia/bin/activate
python manage.py test
deactivate