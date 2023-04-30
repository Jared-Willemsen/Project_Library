import mysql.connector
import dotenv
import os
from database import Database


# Connect to database
# NOTE: required ".env" file with database settings
dotenv.load_dotenv()
database = Database(os.getenv("MYSQL_HOST"), os.getenv("MYSQL_USER"),
                    os.getenv("MYSQL_PASSWORD"), os.getenv("MYSQL_DATABASE"))

try:
    database.connect()
    query = """ SELECT * FROM books limit 20"""
    database.cursor.execute(query)

    for row in database.cursor:
        print(row)

    database.disconnect()
except mysql.connector.Error as err:
    print(f'Error: {err}')


