from os import name
from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def hello_dojo():
    return 'Dojo!' 

@app.route('/say/<string:name>')
def hi_name(name):
    return f"Hi {name}!"

# @app.route('/repeat/<int:number>/<string:name>') 
# def repeat_word(number, name):
#   return (number * name + " " )

@app.route('/repeat/<int:number>/<string:word>')
def repeat_word(number, word ):
    repeat = ""
    for i in range(number):
        repeat += f"{str(word)} " #The str() function converts values to a string form so they can be combined with other strings.
    return repeat


@app.errorhandler(404)
def error_url(error):
    return 'Sorry! No respose. Try again'


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

