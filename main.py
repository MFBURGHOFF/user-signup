from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('forms.html')

@app.route("/", methods=['POST'])

@app.route("/welcome")
def welcome():
    username = request.form['username']
    return render_template('welcome.html', name=username)


#error if: 
    #user leaves any of the following fields empty: username, password, verify password
    #user's username or password is not valid -- for example, it contains a space character or it consists of less than 3 characters or more than 20 characters
    #user's password and password-confirmation do not match.
    #user provides an email, but it's not a valid email
        #The criteria for a valid email address in this assignment are that it has a single @, a single ., contains no spaces, and is between 3 and 20 characters long

# def empty_fields():
    #if 

app.run()