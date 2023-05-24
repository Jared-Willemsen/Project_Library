class ClientsController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.frames['clients'].table.insert_rows(
            self.model.database.execute_query('SELECT name, surname, email FROM clients'))
        
        self._bind()

    def _bind(self):
        # Add keyboard/button controls for entries
        self.view.frames['clients'].search_bar.entry.bind(
            '<Return>', lambda e: self.find(self.view.frames['clients'].search_bar.get_search_input()))
        self.view.frames['clients'].search_bar.button.configure(
            command=lambda: self.find(self.view.frames['clients'].search_bar.get_search_input()))

    def find(self, search_input):
        self.view.frames['clients'].table.clear_rows()
        search_column = self.view.frames['clients'].search_bar.get_selected_column()
        self.view.frames['clients'].table.insert_rows(self.model.search.search_clients(search_column, search_input))
