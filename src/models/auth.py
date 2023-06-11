class Auth:
    """
    A class to handle user authentication
    """

    def __init__(self, database):
        self.database = database

    def login(self, email: str, password: str) -> bool:
        """Checks if the provided email and password are valid."""

        query = """SELECT employee_id FROM employees WHERE email = %s AND password = %s"""
        result = self.database.execute_query(query, (email, password))
        return bool(result)
