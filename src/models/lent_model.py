class LentModel:
    def __init__(self, database):
        self.database = database
    
    def search_lendings(self, view, column, search_input):
        if view == 'All borrowings':
            view = 'borrowings'
        elif view == 'Returned books':
            view='returned_books' 
        elif view == 'Borrowed books':
            view='borrowed_books'
        else:
            view='overdue_books'
        query = f'''SELECT a.title, CONCAT(b.name, " ", b.surname), c.from_date, c.to_date, c.due_date, c.extention, borrowed_id 
                    FROM books a, clients b, {view} c 
                    WHERE a.book_id=c.book_id AND b.client_id=c.client_id AND {column} LIKE "%{search_input}%"'''
        return self.database.execute_query(query)
    
    def add_lending(self, book_id, client_id):
        query = f'''INSERT INTO borrowings(book_id, client_id, from_date, to_date, due_date)
                    VALUES({book_id}, {client_id}, curdate(), NULL, adddate(curdate(), INTERVAL 7 DAY))'''
        self.database.execute_query(query)
    
    def extend_due_date(self, borrowed_id):
        query = f'''UPDATE borrowings
                    SET due_date=adddate(due_date, INTERVAL 7 DAY),
                        extention = 1
                    WHERE borrowed_id={borrowed_id}'''
        self.database.execute_query(query)
    
    def add_return_date(self, borrowed_id):
        query = f'''UPDATE borrowings
                    SET to_date=curdate()
                    WHERE borrowed_id={borrowed_id}'''
        self.database.execute_query(query)