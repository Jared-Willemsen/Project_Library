class ClientsController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames['clients']

        self.frame.table.insert_rows(
            self.model.database.execute_query('SELECT name, surname, email, client_id FROM clients WHERE client_id != 1'))

        self._bind()

    def _bind(self):
        # Add keyboard/button controls for entries
        self.frame.search_bar.entry.bind(
            '<Return>', lambda e: self.update_client_table(self.frame.search_bar.get_search_input()))
        self.frame.search_bar.button.configure(
            command=lambda: self.update_client_table(self.frame.search_bar.get_search_input()))

        self.frame.add_button.configure(command=self.show_add_form)
        self.frame.edit_button.configure(command=self.show_edit_form)
        self.frame.data_form.cancel_button.configure(command=self.cancel_form)

    def cancel_form(self):
        self.frame.hide_form()
        self.frame.show_widgets()

    def show_add_form(self):
        self.frame.hide_widgets()
        self.frame.show_form('Add client')
        self.frame.data_form.confirm_button.configure(command=self.add_client)

    def show_edit_form(self):
        # get selection
        client = self.frame.table.get_selection()

        # check selection
        if client == 'no selection':
            self.view.show_messagebox(self.frame, title='Required fields', message='Please select a client to edit',
                                      icon='warning')
            return

        # switch widgets
        self.frame.data_form.fill_entries(client['values'][0:3])
        self.frame.data_form.confirm_button.configure(command=self.edit_client)
        self.frame.hide_widgets()
        self.frame.show_form('Edit client')

    '''
    ===========================
    MODEL FUNCTIONS
    ===========================
    '''

    def add_client(self):
        # gets imputted data from the user
        client_data = self.frame.data_form.get_data_from_entries()

        # adds client to database
        self.model.client_model.add_client(client_data)

        # update the table and return to it
        self.update_client_table(self.frame.search_bar.get_search_input())
        self.cancel_form()

    def edit_client(self):
        # gets imputted data from the user and the id from the client that is to be edited
        client_data = self.frame.data_form.get_data_from_entries()
        client_id = self.frame.table.get_selection()['values'][3]

        # edits client in the database
        self.model.client_model.edit_client(client_data, client_id)

        # update tables and return close form
        self.update_client_table(self.frame.search_bar.get_search_input())
        self.update_client_table(self.view.frames['lent'].search_bar.get_search_input())
        self.cancel_form()

    def update_client_table(self, search_input):
        self.frame.table.clear_rows()
        search_column = self.frame.search_bar.get_selected_column()
        self.frame.table.insert_rows(self.model.client_model.search_clients(search_column, search_input))