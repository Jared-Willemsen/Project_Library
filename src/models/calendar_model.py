class Calendar:
    def __init__(self, database):
        self.database = database
    
    def add_note(self, data):
        query = f'''INSERT INTO calendar_notes(notes_desc, notes_date)
                    VALUES('{data[0]}', {data[1]}) '''
        print(query)
        self.database.execute_query(query)
    
    def edit_note(self, data, id):
        query = f'''UPDATE calendar_notes
                    SET notes_desc='{data[0]}',
                    WHERE notes_id={id}'''
        print(query)
        self.database.execute_query(query)