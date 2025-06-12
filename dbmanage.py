import sqlite3
from app import username, password
#! selects command type to be used in following function

def selectcmd():
    
    try:
        sqlite3.connect('database.db')
        return
    except sqlite3.OperationalError:
        print("Database not found. Please create the database first.")
        start(cmd_Type='create')
        return

#! This is the start function for determining creating or uploading for the database                                                                                                                                                                                                                                                

def startdb(cmd_Type):
    if cmd_Type == 'create':
        run_database(create_command())
        print("Database created successfully.")
    elif cmd_Type == 'upload':
        run_database(upload_command())
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

def uploadcmd():
    
    command = (''' INSERT INTO Database 
            (username, password, age, gender) 
            VALUES (?, ?, ?, ?)''')
    
    return command

#! Runs the database creation and uploading of any data into the database.

def initdb():
    selectcmd()