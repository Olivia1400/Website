import os, sqlite3

def run_database(command):
    
    cursor = sqlite3.connect('database.db')
    cursor.execute(command)
    cursor.commit()
    cursor.close()



def create_command():
    command = ('''CREATE TABLE IF NOT EXISTS Database (
        uuid INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        age INTEGER,
        gender TEXT
    )''')
    
    
    return command


def upload_command():
    command = (''' INSERT INTO Database 
            (username, password, age, gender) 
            VALUES (?, ?, ?, ?)''')
    
    
    return command


#! 

if __name__ == '__main__':
    run_database(create_command())
    print("Database executing command.")