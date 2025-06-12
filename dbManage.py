import sqlite3
from app import username, password, tabtype

#! selects command type to be used in following function

def selectcmd(username, password):
    if tabtype == 'login':
        try:
            sqlite3.connect('database.db')
            runcmd(cmdType='Login')
            return
        except sqlite3.OperationalError:
            print("Database not found. Please create the database first.")
            runcmd(cmdType='create')
            initdb(username, password)
    elif tabtype == 'signup':
        try:
            sqlite3.connect('database.db')
            runcmd(cmdType='upload')
            return 
        except sqlite3.OperationalError:
            print("Database not found. Please create the database first.")
            runcmd(cmdType='create')
            initdb(username, password)

#! This is the start function for determining creating or uploading for the database                                                                                                                                                                                                                                                

def runcmd(cmdType):
    if cmdType == 'create':
        rundb(createcmd())
        print("Database created successfully.")
    elif cmdType == 'upload':
        rundb(uploadcmd())
        print("Data uploaded successfully.")
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

def readcmd():
    
    command = (''' SELECT *
            FROM Database
            ''')
    
    return command


#! Runs the database creation and uploading of any data into the database.

def initdb(username, password):
    username = username.strip().lower()
    password = password.strip()
    selectcmd(username, password)