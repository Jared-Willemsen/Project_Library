import mysql.connector


class Database:
    """
    A class that represents a connection to a MySQL database.
    """
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        # Establish a connection to the database
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        # Create a cursor object to execute SQL queries
        self.cursor = self.conn.cursor()

    def commit(self):
        # Save all modifications to a database
        self.conn.commit()

    def disconnect(self):
        # Close the cursor and connection
        self.cursor.close()
        self.conn.close()
