# Octavia
Main Web Plateform Django


### Install

First off, install Python 3.6+

```bash
# OS X
$ brew install python3
```

Then you need to `cd` into this directory, and enable the virtual environment (`venv`):

*YOU NEED TO DO THIS EVERY TIME YOU WORK ON THE PROJECT* 

```bash
# (inside the git directory)
# bash
$ source octavia/bin/activate
```

Your prompt should show `(octavia)` before it:

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
(envoctavia) [ ven ~/git/octavia ] pip install django~=1.10.0
Collecting django~=1.10.0
  Downloading Django-1.10.6-py2.py3-none-any.whl (6.8MB)
    100% |████████████████████████████████| 6.8MB 136kB/s 
Installing collected packages: django
Successfully installed django-1.10.6
```

# References

https://tutorial.djangogirls.org/en/

# TODO

https://github.com/matannoam/pypugjs ?
Frontend language?
