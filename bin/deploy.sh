#!/bin/bash

if [ "${BRANCH_NAME}" == "master" ]
then
	# ssh octavia@51.255.166.37 "cd /webapps/octavia/ && sudo git pull && source envoctavia/bin/activate && python manage.py migrate && sudo /etc/mod_wsgi-express-80/apachectl stop && sudo /etc/mod_wsgi-express-80/apachectl start"
	
	cd /home/octavia/current
	sudo git pull
	echo "### git pulled"
	source envoctavia/bin/activate
	echo "### activated"
	python manage.py migrate
	echo "### managed migrated"
	python manage.py collectstatic --noinput --clear
	echo "### managed collectstaticted"
	sudo service gunicorn restart
	"### restarted"
else
	echo "Deploy to prod only on master"
fi