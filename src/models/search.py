class Search:
    def __init__(self, database):
        self.database = database

    def search_books(self, column, search_input):
        query = f'SELECT title, author, genre, language FROM books WHERE {column} LIKE "%{search_input}%"'
        return self.database.execute_query(query)

    def search_clients(self, column, search_input):
        query = f'SELECT name, surname, email language FROM clients WHERE {column} LIKE "%{search_input}%"'
        return self.database.execute_query(query)
    
    def search_lendings(self, column, search_input):
        query = f'SELECT a.title, CONCAT(b.name, " ", b.surname), c.from_date, c.to_date FROM books a, clients b, borrowings c WHERE a.book_id=c.book_id AND b.client_id=c.client_id AND {column} LIKE "%{search_input}%"'
        return self.database.execute_query(query)
    
    def search_reservations(self, column, search_input):
        query = f'SELECT a.title, CONCAT(b.name, " ", b.surname), c.from_date, c.to_date FROM books a, clients b, reservings c WHERE a.book_id=c.book_id AND b.client_id=c.client_id AND {column} LIKE "%{search_input}%"'
        return self.database.execute_query(query)
    