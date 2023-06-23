class BookModel:
    def __init__(self, database):
        self.database = database

    def search_books(self, column, search_input):
        query = f'SELECT title, author, genre, language, book_id FROM books WHERE {column} LIKE "%{search_input}%"'
        return self.database.execute_query(query)
    
    def add_book(self, data):
        query = f'''INSERT INTO books(title, author, genre, language)
                    VALUES('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}') '''
        print(query)
        return self.database.execute_query(query)
    
    def edit_book(self, data, id):
        query = f'''UPDATE books
                    SET title='{data[0]}',
                        author='{data[1]}',
                        genre='{data[2]}',
                        language='{data[3]}'
                    WHERE book_id={id}'''
        print(query)
        return self.database.execute_query(query)