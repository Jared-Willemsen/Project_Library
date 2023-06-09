class LentController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.frames['lent'].table.insert_rows(
            self.model.database.execute_query('SELECT a.title, CONCAT(b.name, " ", b.surname), c.from_date, c.to_date, c.to_date FROM books a, clients b, borrowings c WHERE a.book_id=c.book_id and b.client_id=c.client_id'))
        
        self._bind()

    def _bind(self):
        # Add keyboard/button controls for entries
        self.view.frames['lent'].search_bar.entry.bind(
            '<Return>', lambda e: self.find(self.view.frames['lent'].search_bar.get_search_input()))
        self.view.frames['lent'].search_bar.button.configure(
            command=lambda: self.find(self.view.frames['lent'].search_bar.get_search_input()))

        self.view.frames['lent'].add_button.configure(command=self.show_add_form)
        self.view.frames['lent'].data_form.confirm_button.configure(command=self.add_borrowing)
        self.view.frames['lent'].data_form.cancel_button.configure(command=self.cancel_form)

    def cancel_form(self):
        self.view.frames['lent'].hide_form()
        self.view.frames['lent'].show_widgets()

    def show_add_form(self):
        self.view.frames['lent'].hide_widgets()
        self.view.frames['lent'].show_form('Add borrowing')

    def add_borrowing(self):
        book_data = self.view.frames['lent'].data_form.get_data_from_entries()
        '''add to the table'''
        self.cancel_form()

    def find(self, search_input):
        self.view.frames['lent'].table.clear_rows()
        search_column = self.view.frames['lent'].search_bar.get_selected_column()
        if search_column == 'Book':
            search_column = 'a.title'
        elif search_column == 'Client':
            search_column = 'CONCAT(b.name, " ", b.surname)'
        elif search_column == 'From':
            search_column = 'c.from_date'
        elif search_column == 'To':
            search_column  = 'c.to_date'
        self.view.frames['lent'].table.insert_rows(self.model.search.search_lendings(search_column, search_input))
    