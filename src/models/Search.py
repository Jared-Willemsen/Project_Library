class Search:
    def __init__(self, database):
        self.database = database
    
    def search_books(self, column, search_input):
        return self.database.execute_query(f'SELECT title, author, genre, language FROM books WHERE {column} LIKE "%{search_input}%"')