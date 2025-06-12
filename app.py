from flask import Flask, render_template, request,redirect,url_for,session
import os
import sqlite3
from dbmanage import initdb

app = Flask(__name__)
app.secret_key = '12'
db_locale = 'users.db'



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/SignUp', methods=['GET','POST'])
def SignUp():
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()
        connection = sqlite3.connect(dblocale)
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            connection.commit()
            flash()
            

@app.route('/LogIn', methods=['GET','POST'])
def LogIn():
    

@app.route('/dashboard')
def dashboard():
    

@app.route('/Signout')
def SignOut():
    


if __name__ == '__main__':
    app.run(debug=True, port=5001)