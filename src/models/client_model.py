import random

class ClientModel:
    def __init__(self, database):
        self.database = database
    def search_clients(self, view, column, search_input):
        if view == 'All clients':
            view = 'clients'
        elif view == 'Borrowing clients':
            view = 'borrowing_clients'
        else:
            view = 'non_borrowing_clients'
        query = f'SELECT name, surname, email, client_id FROM {view} WHERE {column} LIKE "%{search_input}%" AND client_id != 1'
        return self.database.execute_query(query)
    
    def add_client(self, data):
        query = f'''INSERT INTO clients(name, surname, email, password)
                    VALUES('{data[0]}', '{data[1]}', '{data[2]}', {self.generate_random_password()}) '''
        self.database.execute_query(query)
    
    def edit_client(self, data, id):
        query = f'''UPDATE clients
                    SET name='{data[0]}',
                        surname='{data[1]}',
                        email='{data[2]}'
                    WHERE client_id={id}'''
        self.database.execute_query(query)

    def delete_client(self, id):
        query = f'''DELETE FROM clients
                    WHERE client_id = {id}'''
        self.database.execute_query(query)

    def generate_random_password(self):
        random_password = ''
        for _ in range(10):
            random_password += str(random.randint(0, 9))
        return random_password