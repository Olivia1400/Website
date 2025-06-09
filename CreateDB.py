import sqlite3


#! selects command type to be used in following function
def select_command():
    
    try:
        sqlite3.connect('database.db')
        return
    except sqlite3.OperationalError:
        print("Database not found. Please create the database first.")
        start(cmd_Type='create')
        return

#! This is the start function for determining creating or uploading to db

def start(cmd_Type):
    if cmd_Type == 'create':
        run_database(create_command())
        print("Database created successfully.")
    elif cmd_Type == 'upload':
        run_database(upload_command())
        print("Data uploaded successfully.")
    else:
        print("Invalid command type. Please use 'create' or 'upload'.")

#! Runs THe command for the database
def run_database(command):
    
    cursor = sqlite3.connect('database.db')
    cursor.execute(command)
    cursor.commit()
    cursor.close()

#! Creates the database and the table if it does not exist.

def create_command():
    command = ('''CREATE TABLE IF NOT EXISTS Database (
        uuid INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        age INTEGER,
        gender TEXT
    )''')
    
    
    return command


#! Runs the database upload command.
def upload_command():
    
    command = (''' INSERT INTO Database 
            (username, password, age, gender) 
            VALUES (?, ?, ?, ?)''')
    
    return command


#! Runs the database creation and uploading of any data into the database.

if __name__ == '__main__':
    select_command()