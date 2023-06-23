import mysql.connector
from mysql.connector import pooling
import os
import dotenv
import logging


class Database:
    """
    A class to perform connection to a database using connection pooling and session management.
    """

    def __init__(self):
        dotenv.load_dotenv()
        self.host = os.getenv("MYSQL_HOST")
        self.user = os.getenv("MYSQL_USER")
        self.password = os.getenv("MYSQL_PASSWORD")
        self.database = os.getenv("MYSQL_DATABASE")

        self.pool = None

    def create_connection_pool(self):
        """Create a connection pool"""
        try:
            self.pool = pooling.MySQLConnectionPool(
                pool_name="my_pool",
                pool_size=5,
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            logging.info("Connection pool created successfully.")
        except mysql.connector.Error as err:
            logging.error(f"Error creating connection pool: {err}")
            raise

    def get_connection(self):
        """Get a connection from the connection pool"""
        if self.pool is None:
            self.create_connection_pool()

        try:
            connection = self.pool.get_connection()
            logging.info("Connection retrieved from the connection pool.")
            return connection
        except mysql.connector.Error as err:
            logging.error(f"Error getting connection from the connection pool: {err}")
            raise

    @staticmethod
    def release_connection(connection):
        """Release the connection back to the connection pool"""
        try:
            connection.close()
            logging.info("Connection released back to the connection pool.")
        except mysql.connector.Error as err:
            logging.error(f"Error releasing connection to the connection pool: {err}")
            raise

    def execute_query(self, query: str, values: str | tuple[str, ...] = None):
        """Execute raw SQL query within a session"""
        connection = self.get_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(query, values)
            result = cursor.fetchall()
            logging.info("Query executed successfully.")
            return result
        except mysql.connector.Error as err:
            logging.error(f"Error executing query: {err}")
            raise
        finally:
            self.commit(connection)
            #self.release_connection(connection)
            logging.info("Connection pool released successfully.")

    def start_transaction(self):
        """Start a new transaction"""
        connection = self.get_connection()
        try:
            connection.start_transaction()
            logging.info("Transaction started successfully.")
            return connection
        except mysql.connector.Error as err:
            logging.error(f"Error starting transaction: {err}")
            raise

    def commit(self, connection):
        """Commit the transaction"""
        try:
            connection.commit()
            logging.info("Transaction committed successfully.")
        except mysql.connector.Error as err:
            logging.error(f"Error committing transaction: {err}")
            raise
        finally:
            self.release_connection(connection)

    def rollback(self, connection):
        """Rollback the transaction"""
        try:
            connection.rollback()
            logging.info("Transaction rolled back successfully.")
        except mysql.connector.Error as err:
            logging.error(f"Error rolling back transaction: {err}")
            raise
        finally:
            self.release_connection(connection)
