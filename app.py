from flask import Flask, render_template, request,redirect,url_for,session
import 
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/SignUp', methods=['GET','POST'])
def SignUp():
    

@app.route('/LogIn', methods=['GET','POST'])
def LogIn():
    

@app.route('/dashboard')
def dashboard():
    

@app.route('/Signout')
def SignOut():
    


if __name__ == '__main__':
    app.run(debug=True, port=5001)


