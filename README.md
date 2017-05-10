# Octavia
Main Web Plateform Django


### Install

First off, install Python 3.6+

```bash
# OS X
[ ven ~/git/octavia ] brew install python3
...
# create the virtual env
[ ven ~/git/octavia ] python3 -m venv envoctavia
```

Then you need to `cd` into this directory, and enable the virtual environment (`venv`):

*YOU NEED TO DO THIS EVERY TIME YOU WORK ON THE PROJECT* 

```bash
# (inside the git directory)
# bash
[ ven ~/git/octavia ] source envoctavia/bin/activate
```

Your prompt should show `(envoctavia)` before it:

```bash
[ ven ~/git/octavia ] source envoctavia/bin/activate
(envoctavia) [ ven ~/git/octavia ] python --version
Python 3.6.1
```

And let's install app:

```bash
(envoctavia) [ ven ~/git/octavia ] git clone https://github.com/PLI-Octavia/Octavia.git

```
Let's install `pip` (Python's package manager):

```bash
(envoctavia) [ ven ~/git/octavia ] pip install --upgrade pip
Requirement already up-to-date: pip in ./octavia/lib/python3.6/site-packages
```

```bash
(envoctavia) [ ven ~/git/octavia ] pip install -r requirements.txt
Will install all depedencies in requirements.txt
```

Time to install postgre and import data:
```bash
(envoctavia) [ ven ~/git/octavia ] brew install postgresql
```
```bash
(envoctavia) [ ven ~/git/octavia ] createuser -dtc 
```

To see if it works :
```bash
(envoctavia) [ ven ~/git/octavia ] psql --user octavia
```

```bash
octavia#= /c octavia
You are now connected to 'octavia' with user 'octavia'
```

If it is ok : 
```bash
(envoctavia) [ ven ~/git/octavia ] python manage.py migrate
```

You will see list of all table have been create.


# References

https://tutorial.djangogirls.org/en/
https://tutorial.djangogirls.org/en/django_installation/

# TODO

https://github.com/matannoam/pypugjs ?
Frontend language?

