# Event Ticketing System: DIS_Prototype
The DIS_prototype is a web application built with Python and Flask for managing event ticketing. The system allows users to browse events, purchase tickets, and manage their orders. It serves as a prototype for learning Flask development and database integration.
The database schema supports event management and ticket sales (not in this version), with a user system that handles customer registration, event browsing, and ticket purchasing (not in this version).

    git repository:  https://github.com/Jeanette1997/VS-DIS.git

# Databse schema
The system includes the following main entities:
- Users: Customer login
- Events: Event details including artist, venue, date, and pricing
- Tickets: Individual ticket records linked to users and events (not yet implemented)
- Orders: Purchase tracking and ticket grouping (not yet implemented)

## Requirements:
Run the code below to install the necessary modules.

    pip install -r requirements.txt

Make sure to run from VS-DIS-main using Python 3.12 or higher

### Install faker seperately if needed
For this project, faker might have to be installed seperately using:

py -m pip install faker


### Virtual Environment Setup.

python -m venv .venv          

pip install Flask


## For Login to MOV3 use:
Alice@mail.com
password123


# Project Structure
├── app.py                  # Application entry point
├── queryscript.py          # Calling functions
├── testDataCreator.py      # Creating testData
├── requirements.txt        # Python dependencies
├── Database.sql            # Database schema
├── templates/              # HTML templates
├── ER-Diagram.png          # ER-diagram for the database
└── README.md               # This file

# Usage

1. Start the application using one of the methods above
2. Open your web browser and navigate to http://localhost:5000
3. Register as a new user or log in with existing credentials as seen above.
4. Browse available events
5. See events you can eddit (Not currently implementet)

# Development Notes

The Flask framework extends HTML with Jinja2 templating ({{ }} syntax).
SQL datasets can be displayed using loops and conditional statements in templates.
Database queries should be parameterized to prevent SQL injection.

## Future development

Some files in this work has not been used. This is as the time we had, to figure out the settings in the code, was not sufficient with our code level. This is a add on, that can be used for further development. There are some 'bloat' in the code, as it is not optimized. In the Sign up function it is possible to make a user, but this new user cannot login on the site. 


