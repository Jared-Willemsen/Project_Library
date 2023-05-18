import mysql.connector
from mysql.connector import errorcode
import os
import dotenv


class Database:
    """
    A class that represents a connection to a MySQL database.
    """

    def __init__(self):
        dotenv.load_dotenv()
        self.host = os.getenv("MYSQL_HOST")
        self.user = os.getenv("MYSQL_USER")
        self.password = os.getenv("MYSQL_PASSWORD")
        self.database = os.getenv("MYSQL_DATABASE")

    def connect(self):
        try:
            # Establish a connection to the database
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your MYSQL user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            elif err.errno == errorcode.CR_CANNOT_OPEN_UNIX_SOCKET:
                print("Cannot open named pipe to MYSQL server")
            else:
                print(f"Error: {err}")
            raise
        # finally:
        #     if self.conn:
        #         self.cursor.close()
        #         self.conn.close()

    def execute_query(self, query, values=None):
        self.connect()
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        self.disconnect()
        return result

    def commit(self):
        # Save all modifications to a database
        self.conn.commit()

    def disconnect(self):
        # Close the cursor and connection
        self.cursor.close()
        self.conn.close()
