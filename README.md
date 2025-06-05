# Event Ticketing System: DIS_Prototype
The DIS_prototype is a web application built with Python and Flask for managing event ticketing. The system allows users to browse events, purchase tickets, and manage their orders. It serves as a prototype for learning Flask development and database integration.
The database schema supports event management and ticket sales, with a user system that handles customer registration, event browsing, and ticket purchasing.

    git repository:  https://github.com/Jeanette1997/VS-DIS.git

# Databse schema
The system includes the following main entities:
- Users: Customer login
- Events: Event details including artist, venue, date, and pricing
- Tickets: Individual ticket records linked to users and events
- Artists: Performer information
- Orders: Purchase tracking and ticket grouping


## Requirements:
Run the code below to install the necessary modules.

    pip install -r requirements.txt

#### notes. When solving codepage problems 
For WINDOWS: Loading data into postgres using psql needs a codepage set. Invoking a cmd shell like this set the codepage: 

    cmd /c chcp 65001   

This makes a subshell with the codepage set to UTF8. 'cmd /c chcp 1252' makes a subshell with the codepage set to 1252. The requirements may have to be run again in the subshell. And you might also have to run the requirements again when invoking a virtual environment (see below). 

## Database setup
Configure your database connection in __init__.py
Run the SQL schema files to create the database structure:

schema.sql - Main database schema
schema_ins.sql - Initial data insertion
schema_upd.sql - Database updates

PostgreSQL Setup Example:

    psql -d{database_name} -U{username} -W -f schema.sql
    psql -d{database_name} -U{username} -W -f schema_ins.sql
    psql -d{database_name} -U{username} -W -f schema_upd.sql 


#### Ubuntu/Linux Note:
Add host parameter for PostgreSQL:

    psql -d{database_name} -U{username} -h127.0.0.1 -W -f schema.sql


## Running flask
### Method 1: The python way

    python3 run.py

### Method 2: The flask way.

    export FLASK_APP=run.py
    export FLASK_DEBUG=1
    export FLASK_RUN_PORT=5000
    flask run

#### notes for Windows users
For Windows you may have to use the SET command instead of EXPORT. 

    set FLASK_APP=run.py
    set FLASK_DEBUG=1
    set FLASK_RUN_PORT=5000
    flask run

### The flask way with Virtual Environment Setup.

Set up virtual environment as specified in https://flask.palletsprojects.com/en/1.1.x/installation/ (OSX/WINDOWS)
vitualenv may be bundled with python.

#### OSX: 

    mkdir myproject
    cd myproject

Create virtual environment in folder

    python3 -m venv .venv

Activate virtual environment in folder

    . .venv/bin/activate

Install flask

    pip install Flask

Set environment variables and start flask

    export FLASK_APP=run.py
    export FLASK_DEBUG=1           (Replaces export FLASK_ENV=development)
    export FLASK_RUN_PORT=5000     (Optional if you want to change port number. Default port is port 5000.)
    flask run
 

#### WINDOWS:

Create virtual environment in folder

    mkdir myproject
    cd myproject
    py -3 -m venv .venv

Activate virtual environment in folder

    .venv\Script\activate
    pip install Flask

Set environment variables and start flask

    set FLASK_APP=run.py
    set FLASK_DEBUG=1           (Replaces export FLASK_ENV=development)
    set FLASK_RUN_PORT=5000     (Optional if you want to change port number. Default port is port 5000.)
    flask run

## Character Encoding (Windows Users)
If you encounter codepage issues when loading data into PostgreSQL:
cmdcmd /c chcp 65001
This sets the codepage to UTF-8. Use chcp 1252 for Windows-1252 encoding.

# Project Structure
event-ticketing/
├── run.py                 # Application entry point
├── __init__.py           # Flask app configuration
├── requirements.txt      # Python dependencies
├── schema.sql           # Database schema
├── schema_ins.sql       # Initial data
├── schema_upd.sql       # Schema updates
├── templates/           # HTML templates
├── static/             # CSS, JS, images
└── README.md           # This file

# Usage

1. Start the application using one of the methods above
2. Open your web browser and navigate to http://localhost:5000
3. Register as a new user or log in with existing credentials
4. Browse available events
5. Order tickets for events you want to attend
6. View your order history and tickets

# Development Notes

The Flask framework extends HTML with Jinja2 templating ({{ }} syntax).
SQL datasets can be displayed using loops and conditional statements in templates.
Database queries should be parameterized to prevent SQL injection.
