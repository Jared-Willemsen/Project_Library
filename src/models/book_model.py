class BookModel:
    def __init__(self, database):
        self.database = database

    def search_books(self, view, column, search_input):
        if view == 'All books':
            view = 'books'
        elif view == 'Available books':
            view = 'available_books'
        elif view == 'Unavailable books':
            view = 'unavailable_books'
        query = f'SELECT title, author, genre, language, book_id FROM {view} WHERE {column} LIKE "%{search_input}%" AND book_id != 1'
        return self.database.execute_query(query)
    
    def add_book(self, data):
        query = f'''INSERT INTO books(title, author, genre, language)
                    VALUES('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}') '''
        self.database.execute_query(query)
    
    def edit_book(self, data, id):
        query = f'''UPDATE books
                    SET title='{data[0]}',
                        author='{data[1]}',
                        genre='{data[2]}',
                        language='{data[3]}'
                    WHERE book_id={id}'''
        self.database.execute_query(query)
    
    def delete_book(self, id):
        query = f'''DELETE FROM books
                    WHERE book_id = {id}'''
        self.database.execute_query(query)

    def get_unavailable_books(self):
        query = 'SELECT book_id FROM unavailable_books'
        return self.database.execute_query(query)