import sqlite3

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
    run_database(create_command())
    print("Database executing command.")