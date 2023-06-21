class ClientsController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.frames['clients'].table.insert_rows(
            self.model.database.execute_query('SELECT name, surname, email, client_id FROM clients'))
        
        self._bind()

    def _bind(self):
        # Add keyboard/button controls for entries
        self.view.frames['clients'].search_bar.entry.bind(
            '<Return>', lambda e: self.find(self.view.frames['clients'].search_bar.get_search_input()))
        self.view.frames['clients'].search_bar.button.configure(
            command=lambda: self.find(self.view.frames['clients'].search_bar.get_search_input()))
        
        self.view.frames['clients'].add_button.configure(command=self.show_add_form)
        self.view.frames['clients'].edit_button.configure(command=self.show_edit_form)
        self.view.frames['clients'].data_form.cancel_button.configure(command=self.cancel_form)

    def cancel_form(self):
        self.view.frames['clients'].hide_form()
        self.view.frames['clients'].show_widgets()

    def show_add_form(self):
        self.view.frames['clients'].hide_widgets()
        self.view.frames['clients'].show_form('Add client') 
        self.view.frames['clients'].data_form.confirm_button.configure(command=self.add_client)

    def show_edit_form(self):
        #get selection
        client = self.view.frames['clients'].table.get_selection()
        
        #check selection
        if client == 'no selection':
            self.view.give_error_message('please select a client to edit')
            return

        #switch widgets
        self.view.frames['clients'].data_form.fill_entries(client['values'][0:3])
        self.view.frames['clients'].data_form.confirm_button.configure(command=self.edit_client)
        self.view.frames['clients'].hide_widgets()
        self.view.frames['clients'].show_form('Edit client')


    def add_client(self):
        client_data = self.view.frames['clients'].data_form.get_data_from_entries()
        '''add to the table'''
        self.cancel_form()

    def edit_client(self):
        '''edit table'''
        self.cancel_form()

    def find(self, search_input):
        self.view.frames['clients'].table.clear_rows()
        search_column = self.view.frames['clients'].search_bar.get_selected_column()
        self.view.frames['clients'].table.insert_rows(self.model.search.search_clients(search_column, search_input))
