#!/bin/bash

if [ "${BRANCH}" == "master" ]
then
	ssh octavia@51.255.166.37
	cd /webapps/octavia/
	sudo git pull
	source envoctavia/bin/activate
	python manage.py migrate
	sudo /etc/mod_wsgi-express-80/apachectl stop && sudo /etc/mod_wsgi-express-80/apachectl start
else
	echo "Deploy to prod only on master"
fi