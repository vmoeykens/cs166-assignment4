# cs-166-catamount-community-bank

## Objective

The source code provided in this project will serve as the web application you will need to study and modify in order to practice and/or mitigate various attacks. This web application was written using the `Python Flask` web framework. It is recommended that you review the [Flask documentation](https://flask.palletsprojects.com/en/2.0.x/quickstart/) to familiarize yourself with the basics of building and deploying a Flask app (a local development server only). We will be using Flask in several subsequent assignments, so it would behoove you to spend some time learning the fundamentals. 

## Note About Classes

In some files, you'll see Python classes. *If you haven't seen classes before
don't panic.* You can (for now) just think of a class as a container for
constants, variables and functions. Variables are called "attributes" when 
they're in a class. Functions are called "methods" when they're in a class. No big deal, you can handle it! 


## General Setup

Requires `Python >= 3.9` (download here is you don't have it: https://www.python.org/downloads/)

You are welcome to setup and run this project however you'd like. I use PyCharm frequently on my larger Python projects, so that is my IDE of choice these days. If you haven't used PyCharm before, it's worth a look. You can get the professional version for free with an .edu domain email address, apply here: https://www.jetbrains.com/community/education/#students

To get setup in PyCharm, first download the project files from GitLab, then you can simply create a new project and add the downloaded files to that project. Be sure to maintain the same directory names and structure as posted on GitLab, as Flask requires this specific structure -- particularly the `static` and `templates` directories. You may need to play around with the PyCharm preferences to ensure you're interpreter is setup correctly and you're running the project in Python >= 3.9


If setting up the project via the command line, you (likely) will want to use a virtual environment, in which case...

    python -m venv venv
    
If this doesn't work, you may have Python 2.7 in your path before Python 3+.

    python -V
    
Will let you know what version you are using. The location of your Python 3 
installation will vary, but if you can start Python 3 (from a command prompt
or IDLE, etc.) try this:

    >> import sys
    >> sys.path
    
This will display your Python path. You should be able to figure out the path
to your Python binary. It will likely look something like this

    /some/path/somewhere/bin/python3.9
    
Once you find the path to the correct Python binary you can call this explicitly
to create your virtual environment, e.g.,

    /some/path/somewhere/bin/python3.9 -m venv venv
    
This will create a virtual environment in a directory named 'venv'. To activate
`cd` to the directory just above `venv` (if you aren't already there) and run

    . venv/bin/activate
    
Your prompt should change -- you should see `venv` prepended. This way you know
if you have your virtual environment activated.

If you are using an IDE like PyCharm, go to Preferences and set the project
interpreter to the Python in this virtual environment. If you are running
PyCharm from the same directory as above, PyCharm will automatically create/detect
the virtual environment and make this an option. Just select, apply, and click
OK. Other IDEs should have similar options.
    
Make sure you have the correct version of Python and (if needed) a new virtual
environment set up before running this.

## Application setup

To install requirements:

    pip install -U -r requirements.txt
    
If you haven't run the app in its current version yet or if you want to start
with a clean slate, you should run `setup.py` from your IDE, or from the 
command line:

    python setup.py
    
This will create the directories the app needs to run and will initialize 
the database. 

## Running the Application

Run `werk.py` from your IDE, or from the command line 

    python werk.py
    
Flask application will be served from `http://localhost:8097/`



