#!/bin/bash

cd /webapps/octavia || exit
source envoctavia/bin/activate
python manage.py test