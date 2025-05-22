# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)


@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def home():
   return 'Hello!'

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/MUV3')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Movie Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #2c3e50;
                color: #ecf0f1;
                text-align: center;
                padding: 50px;
            }
            h1 {
                font-size: 3em;
                color: #e74c3c;
            }
            p {
                font-size: 1.5em;
            }
            a {
                color: #3498db;
                text-decoration: none;
                font-weight: bold;
            }
            a:hover {
                color: #e67e22;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to the test Page!</h1>
        <p>Explore the lorem and ipsum of entertainment.</p>
        <p><a href="/">Go Back to Home</a></p>
    </body>
    </html>
    '''

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
