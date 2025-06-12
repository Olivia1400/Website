import sqlite3
from app import username, password, tabtype

#! selects command type to be used in following function

def selectcmd(username, password):
    if tabtype == 'login':
        try:
            sqlite3.connect('database.db')
            data = runcmd(cmdType='Login')
            readcomp(username, password, data)
            
        except sqlite3.OperationalError:
            print("Database not found. Please create the database first.")
            runcmd(cmdType='create')
            initdb(username, password)
    elif tabtype == 'signup':
        try:
            sqlite3.connect('database.db')
            runcmd(cmdType='upload')
        except sqlite3.OperationalError:
            print("Database not found. Please create the database first.")
            runcmd(cmdType='create')
            initdb(username, password)

#! This is the start function for determining creating or uploading for the database                                                                                                                                                                                                                                                

def runcmd(cmdType,username, password):
    if cmdType == 'create':
        rundb(createcmd())
        print("Database created successfully.")
    elif cmdType == 'upload':
        rundb(uploadcmd(username, password))
        print("Data uploaded successfully.")
    elif cmdType == 'Login':
        rundb(readcmd(username))
        print("You are Logged In.")
    else:
        print("Invalid command type. Please use 'create' or 'upload'.")

#! Runs THe command for the database

def rundb(command):
    
    cursor = sqlite3.connect('database.db')
    cursor.execute(command)
    cursor.commit()
    cursor.close()

#! Creates the database and the table if it does not exist.

def createcmd():
    command = ('''CREATE TABLE IF NOT EXISTS Database (
        uuid INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )''')
    
    
    return command

#! Runs the database upload command.

def uploadcmd(username, password):
    
    command = (''' INSERT INTO Database 
            (username, password) 
            VALUES (?, ?)''', 
            (username, password))
    
    return command

#! Runs Database Read Command

def readcmd(username):
    
    command = (''' SELECT ROW FROM Database
        WHERE username='''(username)''';
    ''')
    return command

#! Reads Contents of the database and compares them with username and password values form login

def readcomp(username, password, data):
    cursor = sqlite3.connect('database.db')
    cursor.execute(data)
    result = cursor.fetchone()
    
    if result:
        db_username, db_password = result[1], result[2]
        if db_username == username and db_password == password:
            status = "Login successful."
        else:
            status = "Invalid username or password."
    else:
        status = "No user found with that username."
    
    cursor.close()
    return status







#! Runs the database creation and uploading of any data into the database.

def initdb(username, password):
    username = username.strip().lower()
    password = password.strip()
    selectcmd(username, password)