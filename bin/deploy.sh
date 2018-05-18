#!/bin/bash

if [ "${BRANCH_NAME}" == "master" ]
then
	# ssh octavia@51.255.166.37 "cd /webapps/octavia/ && sudo git pull && source envoctavia/bin/activate && python manage.py migrate && sudo /etc/mod_wsgi-express-80/apachectl stop && sudo /etc/mod_wsgi-express-80/apachectl start"
	
	cd /home/octavia/current
	sudo git pull
	source envoctavia/bin/activate
	python manage.py migrate
	yes | python manage.py collectstatic
	sudo service gunicorn restart
else
	echo "Deploy to prod only on master"
fi