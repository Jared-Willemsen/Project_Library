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

    def levelOfAccessStaff(self, username: str, password: str):
        """Checks the level of access the staff member has."""

        query = """SELECT b.title FROM employees a LEFT JOIN jobs b ON a.employee_id=b.employee_id WHERE email = %s AND password = %s AND b.to_date IS NULL"""
        param = (username, password)
        access = self.database.access_query(query, param)
        
        if not access:
            return
        
        title = access[0]

        if title == None:
            title = ['invalid']
            return title
        else:
            return title
    
    def levelOfAccessClient(self, username: str, password: str) -> bool:
        """Checks if the user is a client."""

        query = """SELECT client_id FROM clients WHERE email = %s AND password = %s"""
        param = (username, password)
        access = self.database.execute_query(query, param)
        return bool(access)