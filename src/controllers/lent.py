import customtkinter as ctk


class LentController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames['lent']

        self.frame.table.insert_rows(
            self.model.database.execute_query('SELECT a.title, CONCAT(b.name, " ", b.surname), c.from_date, '
                                              'c.to_date, c.due_date, c.extention, c.borrowed_id FROM books a, clients b, borrowings c WHERE '
                                              'a.book_id=c.book_id and b.client_id=c.client_id ORDER BY c.from_date'))

        self._bind()

    def _bind(self):
        # Add keyboard/button controls for entries
        self.frame.search_bar.entry.bind('<Return>', lambda e: self.update_lent_table())
        self.frame.search_bar.button.configure(command=self.update_lent_table)
        self.frame.search_bar.view_dropdown.configure(command= lambda e: self.update_lent_table())

        self.frame.add_button.configure(command=self.show_add_conformation)
        self.frame.extend_button.configure(command=self.show_extention_conformation)
        self.frame.return_button.configure(command=self.show_return_conformation)
        self.frame.conformation_frame.cancel_button.configure(command=self.cancel_form)

    def cancel_form(self):
        self.frame.hide_form()
        self.frame.show_widgets()
        self.view.sidebar.books_button.configure(state=ctk.NORMAL)
        self.view.sidebar.clients_button.configure(state=ctk.NORMAL)

    def show_add_conformation(self):
        # set confirm button
        self.frame.conformation_frame.confirm_button.configure(command=self.add_borrowing)

        # get selected book and client
        book = self.view.frames['books'].table.get_selection()
        client = self.view.frames['clients'].table.get_selection()

        # check selection
        if book == 'no selection' or client == 'no selection':
            self.view.show_messagebox(self.frame, title='Required fields', message='Please select a book and client',
                                      icon='warning')
            return

        unavailable_books = self.model.book_model.get_unavailable_books() 
        book_id = book['values'][4] 
        for id in unavailable_books:
            if book_id in id:
                self.view.show_messagebox(self.frame, title='Required fields', message='Please select an available book',
                                          icon='warning')
                return

        # switch widgets
        self.frame.hide_widgets()
        self.frame.show_form('Add borrowing')
        self.frame.conformation_frame.change_labels(
            [book['values'][0], f'{client["values"][0]} {client["values"][1]}'])

        self.view.sidebar.books_button.configure(state=ctk.DISABLED)
        self.view.sidebar.clients_button.configure(state=ctk.DISABLED)
    
    def show_extention_conformation(self):
        # get selected borrowing
        borrowing = self.frame.table.get_selection()['values']

        #check if selection is valid
        if borrowing[3] != 'None':
            self.view.show_messagebox(self.frame, title='Required fields', message='Please select a current borrowing',
                            icon='warning')
            return
        if borrowing[5] != 0:
            self.view.show_messagebox(self.frame, title='Required fields', message='This book has already been extended',
                            icon='warning')
            return
        
         # set confirm button
        self.frame.conformation_frame.confirm_button.configure(command=self.extend_borrowing)

        # switch widgets
        self.frame.hide_widgets()
        self.frame.show_form('Extend borrowing')
        self.frame.conformation_frame.change_labels([borrowing[0], borrowing[1]])
        

    def show_return_conformation(self):
        # get selected borrowing
        borrowing = self.frame.table.get_selection()['values']

        #check if selection is valid
        if borrowing[3] != 'None':
            self.view.show_messagebox(self.frame, title='Required fields', message='Please select a current borrowing',
                                      icon='warning')
            return

        # set confirm button
        self.frame.conformation_frame.confirm_button.configure(command=self.return_borrowing)

        # switch widgets
        self.frame.hide_widgets()
        self.frame.show_form('Return borrowing')
        self.frame.conformation_frame.change_labels([borrowing[0], borrowing[1]])

    '''
    ===========================
    MODEL FUNCTIONS
    ===========================
    '''

    def add_borrowing(self):
        book_id = self.view.frames['books'].table.get_selection()['values'][4]
        client_id = self.view.frames['clients'].table.get_selection()['values'][3]
        self.model.lent_model.add_lending(book_id, client_id)
        
        self.update_lent_table()
        self.update_book_table()
        self.cancel_form()

    def extend_borrowing(self):
        borrowing_id = self.frame.table.get_selection()['values'][6]
        self.model.lent_model.extend_due_date(borrowing_id)

        self.update_lent_table()
        self.cancel_form()

    def return_borrowing(self):
        borrowing_id = self.frame.table.get_selection()['values'][6]
        self.model.lent_model.add_return_date(borrowing_id)

        self.update_lent_table()
        self.update_book_table()
        self.cancel_form()

    def update_lent_table(self):
        self.frame.table.clear_rows()

        search_input = self.frame.search_bar.get_search_input()
        search_column = self.frame.search_bar.get_selected_column()
        if search_column == 'Book':
            search_column = 'a.title'
        elif search_column == 'Client':
            search_column = 'CONCAT(b.name, " ", b.surname)'
        elif search_column == 'From':
            search_column = 'c.from_date'
        elif search_column == 'To':
            search_column = 'c.to_date'
        else:
            search_column = 'c.due_date'
        
        view = self.frame.search_bar.get_selected_view()
        if view == 'All borrowings':
            self.frame.table.treeview.configure(displaycolumns=['Book', 'Client', 'From', 'to', 'due'])
        elif view == 'Returned books':
            self.frame.table.treeview.configure(displaycolumns=['Book', 'Client', 'From', 'to'])
        else:            
            self.frame.table.treeview.configure(displaycolumns=['Book', 'Client', 'From', 'due'])
        
        self.frame.table.insert_rows(self.model.lent_model.search_lendings(view, search_column, search_input))
    
    def update_book_table(self):
        self.view.frames['books'].table.clear_rows()

        view = self.view.frames['books'].search_bar.get_selected_view()
        search_input = self.view.frames['books'].search_bar.get_search_input()
        search_column = self.view.frames['books'].search_bar.get_selected_column()

        self.view.frames['books'].table.insert_rows(self.model.book_model.search_books(view, search_column, search_input))
