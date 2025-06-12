import Flask
import hashlib
from flask import Flask, render_template, request, redirect, url_for, session, flash
from dbManage import initdb

app = Flask(__name__)
app.secret_key = '12'
db_locale = 'users.db'

#! ^ Imports and global variables ^


#! Home Page

@app.route('/')
def index():
    return render_template('index.html')

#! SignUp

@app.route('/SignUp', methods=['GET','POST'])
def SignUp():
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()
        tabtype ='signup'
        initdb(username, password)
        flash('Account created successfully!')
        return redirect(url_for('LogIn'))
    return render_template('signup.html')
#! LogIn

@app.route('/LogIn', methods=['GET','POST'])
def LogIn():
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()
        tabtype = 'login'
        if initdb(username, password):
            session['username'] = username
            flash('Logged in successfully!')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password!')

#! Dashboard

@app.route('/dashboard')
def dashboard():
    

#! SignOut

@app.route('/Signout')
def SignOut():
    

#! Main Run

if __name__ == '__main__':
    app.run(debug=True, port=5001)