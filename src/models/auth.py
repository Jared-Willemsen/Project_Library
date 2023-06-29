import bcrypt
import re
import string
import secrets
import time


class Auth:
    """
    A class to handle user authentication
    """

    def __init__(self, database):
        self.database = database

    def login(self, email: str, password: str) -> bool:
        """Checks if given email and password are valid."""
        # Fetch the stored hashed password for the given email
        stored_password = self.get_stored_password(email)

        # Verify the entered password against the stored hashed password
        if stored_password and self.verify_password(password, stored_password):
            return True
        return False

    def get_stored_password(self, email: str) -> str | None:
        """Fetch stored password for given email from database"""
        query = "SELECT password FROM employees WHERE email = %s"
        result = self.database.execute_query_fetchone(query, (email,))
        if result:
            return result[0]
        return

    def get_stored_password_client(self, email: str) -> str | None:
        """Fetch stored password for given email from database"""
        query = "SELECT password FROM clients WHERE email = %s"
        result = self.database.execute_query_fetchone(query, (email,))
        if result:
            return result[0]
        return

    def update_password(self, email: str, new_password: str):
        """Update stored password for given email in database"""
        hashed_password = self.hash_password(new_password)
        query = "UPDATE employees SET password = %s WHERE email = %s"
        self.database.execute_query(query, (hashed_password, email))

    @staticmethod
    def hash_password(password: str) -> str:
        """Hash entered password"""
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed_password.decode('utf-8')

    @staticmethod
    def verify_password(password: str, stored_password: str) -> bool:
        """Check if given password matches with stored in database"""
        return bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8'))

    def levelOfAccessStaff(self, username: str):
        """Checks the level of access the staff member has."""

        query = """SELECT b.title FROM employees a LEFT JOIN jobs b ON a.employee_id=b.employee_id WHERE email = %s AND b.to_date IS NULL"""
        param = (username,)
        access = self.database.access_query(query, param)

        if not access:
            return

        title = access[0]

        if title is None:
            title = ['invalid']
            return title
        else:
            return title

    def levelOfAccessClient(self, username: str, password: str) -> bool:
        """Checks if the user is a client."""

        # Fetch the stored hashed password for the given email
        stored_password = self.get_stored_password_client(username)

        # Verify the entered password against the stored hashed password
        if stored_password and self.verify_password(password, stored_password):
            return True
        return False

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """Validate format of email address."""
        # Regular expression pattern for validating email addresses
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        # Use the pattern to match the email address
        match = re.match(pattern, email)

        # Return True if the email is valid, False otherwise
        return bool(match)

    def is_employee(self, email: str) -> bool:
        """Checks if given email belongs to employee"""
        query = '''
                    SELECT employee_id FROM employees WHERE email = %s'''
        result = self.database.execute_query_fetchone(query, (email,))
        return bool(result)

    @staticmethod
    def generate_token(length=6) -> str:
        """Generate n-digit token"""
        alphabet = string.digits
        token = ''.join(secrets.choice(alphabet) for _ in range(length))
        return token

    def insert_token_to_db(self, email: str, token: str):
        """Insert hashed token to database"""
        hashed_token = bcrypt.hashpw(token.encode(), bcrypt.gensalt())
        query = '''INSERT INTO password_reset_tokens (employee_id, token, token_expiry)
            (SELECT employee_id, %s, UNIX_TIMESTAMP(DATE_ADD(NOW(), INTERVAL 10 MINUTE)) FROM employees WHERE email = %s)'''
        self.database.execute_query_fetchone(query, (hashed_token, email,))

    def get_tokens_from_db(self, employee_id: str) -> list[tuple[str, int]]:
        """Get all hashed tokens from database"""
        query = '''
                SELECT token, token_expiry
                FROM password_reset_tokens
                WHERE employee_id = %s
            '''
        results = self.database.execute_query(query, (employee_id,))
        return results

    def redeem_token(self, token: str, email: str) -> bool | None:
        """Check if given token is valid and not expired"""
        # Query the database and find a matching employee
        query = '''SELECT employee_id FROM employees WHERE email = %s'''
        result = self.database.execute_query_fetchone(query, (email,))

        if result is None:
            return  # "Not an employee"

        employee_id = result[0]

        # Start a database transaction
        connection = self.database.start_transaction()

        try:
            # Get all tokens for the user
            stored_tokens = self.get_tokens_from_db(employee_id)

            # Search for the row that matches the hashed token
            matched_row = None
            for row in stored_tokens:
                stored_token = row[0]
                if self.verify_password(token, stored_token):
                    matched_row = row
                    break

            if matched_row is None:
                # The token was redeemed by another transaction
                self.database.rollback(connection)
                return  # "Invalid password reset token"

            # Delete all tokens belonging to the user
            query = "DELETE FROM password_reset_tokens WHERE employee_id = %s"
            self.database.execute_query(query, (employee_id,))

            # Check if the token has expired
            stored_datestamp = matched_row[1]
            if stored_datestamp < int(time.time()):
                self.database.rollback(connection)
                return  # "Token has expired. Please try again"

            # Commit the transaction
            self.database.commit(connection)
            return True

        except Exception as err:
            self.database.rollback(connection)
            raise err
