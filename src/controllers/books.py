class BooksController():
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.frames['books'].table.insert_rows(self.model.database.execute_query('SELECT title, author, genre, language FROM books'))
        self._bind()
    
    def _bind(self):
        self.view.frames['books'].search_bar.button.configure(command=lambda: self.find(self.view.frames['books'].search_bar.get_search_input()))
    
    def find(self, search_input):
        self.view.frames['books'].table.clear_rows()
        self.view.frames['books'].table.insert_rows(self.model.search.search_books('title', search_input))
    