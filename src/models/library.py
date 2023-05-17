class LibraryModel:
    """
    A class to perform library business logic.
    """

    def __init__(self, database):
        self.database = database

    def select_all_books(self):
        query = """SELECT * FROM books"""
        result = self.database.execute_query(query)
        return result
