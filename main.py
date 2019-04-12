from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('forms.html')

@app.route("/welcome")
def welcome():
    username = request.form['username']
    return render_template('welcome.html', name=username)
    
@app.route("/", methods=['POST'])
def validate_form():
    username = request.form['username']
    password = request.form['password']
    verify_pw = request.form['verify_pw']
    email = request.form['email']

    name_error = ''
    password_error = ''
    verify_pw_error = ''
    email_error = ''

    if " " in username:
        name_error = "Username cannot contain a space."
        username = username

    elif username == "":
        name_error = "Username cannot be blank."
        username = username

    elif len(username) < 3 or len(username) > 20:
        name_error = "Username must be greater than 3 characters and less than 20."
        username = username

    if " " in password:
        password_error = "password cannot contain a space."

    elif password == "":
        password_error = "password cannot be blank."

    elif len(password) < 3 or len(password) > 20:
        password_error = "password must be greater than 3 characters and less than 20."
    
    if verify_pw != password:
        verify_pw_error = "The passwords do not match!"

    if " " in email:
        email_error = "Email cannot contain a space."
        email = email
    
    if "@" not in email:
        email_error = "Email must have an @."
        email = email
    
    elif "." not in email:
        email_error = "Email must have a ."
        email = email

    elif len(email) < 3 or len(email) > 20:
        email_error = "Email must be greater than 3 characters and less than 20."
        email = email 

    if not name_error and not password_error and not verify_pw_error and not email_error:
        return render_template('welcome.html', name=username)
    else:
        return render_template('forms.html', name_error=name_error, password_error = password_error, verify_pw_error = verify_pw_error, email_error = email_error, username=username, password=password, verify_pw=verify_pw, email=email)

#error if: 
    #user leaves any of the following fields empty: username, password, verify password
    #user's username or password is not valid -- for example, it contains a space character or it consists of less than 3 characters or more than 20 characters
    #user's password and password-confirmation do not match.
    #user provides an email, but it's not a valid email
        #The criteria for a valid email address in this assignment are that it has a single @, a single ., contains no spaces, and is between 3 and 20 characters long

# def empty_fields():
    #if 

app.run()