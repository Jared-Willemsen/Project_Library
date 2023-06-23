

class LentController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.frames['lent'].table.insert_rows(
            self.model.database.execute_query('SELECT a.title, CONCAT(b.name, " ", b.surname), c.from_date, c.to_date, c.borrowed_id FROM books a, clients b, borrowings c WHERE a.book_id=c.book_id and b.client_id=c.client_id'))
        
        self._bind()

    def _bind(self):
        # Add keyboard/button controls for entries
        self.view.frames['lent'].search_bar.entry.bind(
            '<Return>', lambda e: self.find(self.view.frames['lent'].search_bar.get_search_input()))
        self.view.frames['lent'].search_bar.button.configure(
            command=lambda: self.find(self.view.frames['lent'].search_bar.get_search_input()))

        self.view.frames['lent'].add_button.configure(command=self.show_add_conformation)
        self.view.frames['lent'].conformation_frame.cancel_button.configure(command=self.cancel_form)
        self.view.frames['lent'].return_button.configure(command=self.show_return_conformation)

    def cancel_form(self):
        self.view.frames['lent'].hide_form()
        self.view.frames['lent'].show_widgets()

    def show_add_conformation(self):
        #set confirm button
        self.view.frames['lent'].conformation_frame.confirm_button.configure(command=self.add_borrowing)
        
        #get selected book and client
        book = self.view.frames['books'].table.get_selection()
        client = self.view.frames['clients'].table.get_selection()

        #check selection
        if book == 'no selection' or client == 'no selection':
            self.view.give_error_message('please select a book and client')
            return

        #switch widgets
        self.view.frames['lent'].hide_widgets()
        self.view.frames['lent'].show_form('Add borrowing')
        self.view.frames['lent'].conformation_frame.change_labels([book['values'][0], f'{client["values"][0]} {client["values"][1]}'])
    
    def show_return_conformation(self):
        #get selected borrowing
        borrowing = self.view.frames['lent'].table.get_selection()['values']

        if borrowing[3] != 'None':
            self.view.give_error_message('please select a current borrowing')
            return
        
        #set confirm button
        self.view.frames['lent'].conformation_frame.confirm_button.configure(command=self.add_return_date)

        #switch widgets
        self.view.frames['lent'].hide_widgets()
        self.view.frames['lent'].show_form('Return borrowing')
        self.view.frames['lent'].conformation_frame.change_labels([borrowing[0], borrowing[1]])
        

    '''
    ===========================
    MODEL FUNCTIONS
    ===========================
    '''
    
    def add_borrowing(self):
        '''add to the table'''
        self.cancel_form()
    
    def add_return_date(self):
        
        self.cancel_form()

    def find(self, search_input):
        self.view.frames['lent'].table.clear_rows()
        search_column = self.view.frames['lent'].search_bar.get_selected_column()
        if search_column == 'Book':
            search_column = 'a.title'
        elif search_column == 'Client':
            search_column = 'CONCAT(b.name, " ", b.surname)'
        elif search_column == 'From':
            search_column = 'c.borrow_date'
        elif search_column == 'To':
            search_column  = 'c.return_date'
        self.view.frames['lent'].table.insert_rows(self.model.search.search_lendings(search_column, search_input))
    