# Octavia
Main Web Plateform Django


### Install

First off, install Python 3.6+

```bash
# OS X
[ ven ~/git/octavia ] brew install python3
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

Let's install `pip` (Python's package manager):

```bash
(envoctavia) [ ven ~/git/octavia ] pip install --upgrade pip
Requirement already up-to-date: pip in ./octavia/lib/python3.6/site-packages
```

And let's install Django:

```bash
(envoctavia) [ ven ~/git/octavia ] pip install django~=1.11.0
Collecting django~=1.11.0
  Downloading Django-1.11-py2.py3-none-any.whl (6.9MB)
    100% |████████████████████████████████| 6.9MB 112kB/s 
Collecting pytz (from django~=1.11.0)
  Downloading pytz-2017.2-py2.py3-none-any.whl (484kB)
    100% |████████████████████████████████| 491kB 1.8MB/s 
Installing collected packages: pytz, django
Successfully installed django-1.11 pytz-2017.2
```

# References

https://tutorial.djangogirls.org/en/

# TODO

https://github.com/matannoam/pypugjs ?
Frontend language?

