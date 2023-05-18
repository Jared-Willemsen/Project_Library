class Auth:
    def __init__(self, database):
        self.database = database

    def login(self, username: str, password: str) -> bool:
        """Checks whether user with given username and password exists"""

        query = """SELECT employee_id FROM employees WHERE email = %s AND password = %s"""
        result = self.database.execute_query(query, (username, password))
        return result