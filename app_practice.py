# import the dependency, will enable your code to access all that Flask has to offer
# import the Flask dependency
from flask import Flask

# create a new Flask app instance. "Instance" is a general term in programming to refer to a singular version of something
app = Flask(__name__)

# Create Flask Routes
#@app.route('/')

# create a function called hello_world(). Whenever you make a route in Flask, you put the code you want in that specific route below @app.route()
@app.route('/')
def hello_world():
    return "Hello world"

# create a function called Lavina, Data Analyst(). Whenever you make a route in Flask, you put the code you want in that specific route below @app.route()
@app.route('/L')
def Lavina():
    return "Lavina, Data Analyst"

# Run a Flask App
# export FLASK_APP=app.py

# set FLASK_APP=app.py

# flask run
