import customtkinter as ctk


class LentController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames['lent']

        self.frame.table.insert_rows(
            self.model.database.execute_query('SELECT a.title, CONCAT(b.name, " ", b.surname), c.from_date, '
                                              'c.to_date, c.borrowed_id FROM books a, clients b, borrowings c WHERE '
                                              'a.book_id=c.book_id and b.client_id=c.client_id'))

        self._bind()

    def _bind(self):
        # Add keyboard/button controls for entries
        self.frame.search_bar.entry.bind(
            '<Return>', lambda e: self.change_lent_table(self.frame.search_bar.get_search_input()))
        self.frame.search_bar.button.configure(
            command=lambda: self.change_lent_table(self.frame.search_bar.get_search_input()))

        self.frame.add_button.configure(command=self.show_add_conformation)
        self.frame.conformation_frame.cancel_button.configure(command=self.cancel_form)
        self.frame.return_button.configure(command=self.show_return_conformation)

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
        print(unavailable_books, book_id)
        for book in unavailable_books:
            if book_id in book:
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

    def show_return_conformation(self):
        # get selected borrowing
        borrowing = self.frame.table.get_selection()['values']

        if borrowing[3] != 'None':
            self.view.show_messagebox(self.frame, title='Required fields', message='Please select a current borrowing',
                                      icon='warning')
            return

        # set confirm button
        self.frame.conformation_frame.confirm_button.configure(command=self.add_return_date)

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
        self.change_lent_table(self.frame.search_bar.get_search_input())
        self.cancel_form()

    def add_return_date(self):
        #
        self.cancel_form()

    def change_lent_table(self, search_input):
        self.frame.table.clear_rows()
        search_column = self.frame.search_bar.get_selected_column()
        if search_column == 'Book':
            search_column = 'a.title'
        elif search_column == 'Client':
            search_column = 'CONCAT(b.name, " ", b.surname)'
        elif search_column == 'From':
            search_column = 'c.from_date'
        elif search_column == 'To':
            search_column = 'c.to_date'
        self.frame.table.insert_rows(self.model.search.search_lendings(search_column, search_input))
