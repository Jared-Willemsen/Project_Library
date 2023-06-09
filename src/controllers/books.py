class BooksController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.frames['books'].table.insert_rows(
            self.model.database.execute_query('SELECT title, author, genre, language, book_id FROM books'))
        self._bind()

    def _bind(self):
        # Add keyboard/button controls for entries
        self.view.frames['books'].search_bar.entry.bind(
            '<Return>', lambda e: self.find(self.view.frames['books'].search_bar.get_search_input()))
        self.view.frames['books'].search_bar.button.configure(
            command=lambda: self.find(self.view.frames['books'].search_bar.get_search_input()))
        
        self.view.frames['books'].add_button.configure(command=self.show_add_form)
        self.view.frames['books'].data_form.confirm_button.configure(command=self.add_book)
        self.view.frames['books'].data_form.cancel_button.configure(command=self.cancel_form)

    def cancel_form(self):
        self.view.frames['books'].hide_form()
        self.view.frames['books'].show_widgets()

    def show_add_form(self):
        self.view.frames['books'].hide_widgets()
        self.view.frames['books'].show_form('Add book')

    def add_book(self):
        book_data = self.view.frames['books'].data_form.get_data_from_entries()
        '''add to the table'''
        self.cancel_form()

    def find(self, search_input):
        self.view.frames['books'].table.clear_rows()
        search_column = self.view.frames['books'].search_bar.get_selected_column()
        self.view.frames['books'].table.insert_rows(self.model.search.search_books(search_column, search_input))
    

        
 