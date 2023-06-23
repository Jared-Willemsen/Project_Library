class LentModel:
    def __init__(self, database):
        self.database = database
    
    def search_lendings(self, column, search_input):
        query = f'SELECT a.title, CONCAT(b.name, " ", b.surname), c.from_date, c.to_date FROM books a, clients b, borrowings c WHERE a.book_id=c.book_id AND b.client_id=c.client_id AND {column} LIKE "%{search_input}%"'
        return self.database.execute_query(query)
    
    def add_lending(self, book_id, client_id):
        query = f'''INSERT INTO borrowings(book_id, client_id, from_date)
                    VALUES({book_id}, {client_id}, curdate())'''
        self.database.execute_query(query)