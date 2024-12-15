
# importing sqlite3 module 
import sqlite3 
from backend.authentication import get_password_hash
from utilities.config import config

def create_structure():

    try:
        # create connection by using object to  
        # connect with college_details database 
        connection = sqlite3.connect(config.DBPATH) 
        
        print("Starting to create user_details table") 
        
        # sqlite execute query to create a table 
        connection.execute("""
        CREATE TABLE IF NOT EXISTS user_details (
            [user_id] INTEGER PRIMARY KEY AUTOINCREMENT,
            [full_name] VARCHAR(100),
            [email] VARCHAR(100),
            [password] VARCHAR(20)
        );""") 
        
        print("Table created successfully") 
        
        # terminate the connection 
        connection.close() 
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
def initialize_data():

    try:
        # create connection by using object to  
        # connect with college_details database 
        connection = sqlite3.connect(config.DBPATH) 
        
        print("Starting to default user..") 
        
        hash = get_password_hash('123123')
        
        # sqlite execute query to create a table 
        connection.execute(f"""
        INSERT INTO user_details (full_name, email, password)
        SELECT 'Khushi Gupta', 'iam.khushi@rediffmail.com', '{hash}'
        WHERE NOT EXISTS (
            SELECT * FROM user_details WHERE email = 'iam.khushi@rediffmail.com'
        );""") 
        connection.commit()
        
        print("Added default user") 
        
        # terminate the connection 
        connection.close() 
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
