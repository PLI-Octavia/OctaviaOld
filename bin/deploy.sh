#!/bin/bash

if [ "${BRANCH_NAME}" == "master" ]
then
	# ssh octavia@51.255.166.37 "cd /webapps/octavia/ && sudo git pull && source envoctavia/bin/activate && python manage.py migrate && sudo /etc/mod_wsgi-express-80/apachectl stop && sudo /etc/mod_wsgi-express-80/apachectl start"
	
	cd /home/octavia/current
	su octavia
	sudo git pull
	source envoctavia/bin/activate
	python manage.py migrate
	python manage.py collectstatic --noinput ## --clear
	exit
	sudo service gunicorn restart
elif [ "${BRANCH_NAME}" == "develop" ]
then
	cd /home/octaviadev/current
	sudo -u octaviadev git pull
	source envoctavia/bin/activate
	## python manage.py migrate
	python manage.py collectstatic --noinput ## --clear
	exit
	sudo service gunicorn-dev restart
else
	echo "Deploy to prod only on master"
fi
