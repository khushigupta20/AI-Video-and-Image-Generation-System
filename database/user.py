# importing sqlite3 module 
import sqlite3 
from utilities.config import config
from database.models import LoginItem, UserItem

def validate_user(user: LoginItem):
    try:
        # create connection by using object to  
        # connect with college_details database 
        connection = sqlite3.connect(config.DBPATH) 
        

        connection.row_factory = sqlite3.Row

        # Set the row_factory to sqlite3.Row so we can access columns by name
        print("Starting to validate user details..") 
        
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM user_details WHERE email = ?", (user.email,))

        data = cursor.fetchall()
        returnObj: UserItem = None
        returnValue = False
        if len(data)==0:
            print(f'Email - {user.email} is not found!')
        elif user.password != data[0]['password']:
            print(f'Password for email is Incorrect!')
        else:
            print(f'Login successful for {user.email}')
            for row in data:
                returnObj = UserItem(user_email=user.email, user_full_name=row['user_full_name'])           
            returnValue = True

        # terminate the connection 
        connection.close() 
        return (returnValue, returnObj)
     
    except Exception as e:
        print(f"An error occurred: {e}")
        return (False, None)
    
def find_user(email: str):
    returnObj: UserItem = None
    try:
        # create connection by using object to  
        # connect with college_details database 
        connection = sqlite3.connect(config.DBPATH) 
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM user_details WHERE email = ?", (email,))

        data = cursor.fetchall()
        if len(data) > 0:
            for row in data:
                returnObj = UserItem(   \
                    user_email=email, \
                    user_full_name=row['full_name'],   \
                    user_password=row['password'])           

        # terminate the connection 
        connection.close() 
     
    except Exception as e:
        print(f"An error occurred: {e}")
    return returnObj
