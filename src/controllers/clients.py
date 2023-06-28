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
        self.frame.search_bar.entry.bind('<Return>', lambda e: self.update_client_table())
        self.frame.search_bar.button.configure(command=self.update_client_table)
        self.frame.search_bar.view_dropdown.configure(command= lambda _: self.update_client_table())

        self.frame.add_button.configure(command=self.show_add_form)
        self.frame.edit_button.configure(command=self.show_edit_form)
        self.frame.delete_button.configure(command=self.show_conformation_frame)
        self.frame.conformation_frame.confirm_button.configure(command=self.delete_client)
        self.frame.data_form.cancel_button.configure(command=self.cancel_form)
        self.frame.conformation_frame.cancel_button.configure(command=self.cancel_frame)

    def cancel_form(self):
        self.frame.hide_form()
        self.frame.show_widgets()

    def cancel_frame(self):
        self.frame.hide_frame()
        self.frame.show_widgets()

    def show_add_form(self):
        self.frame.data_form.entry_values = ['','','']
        self.frame.hide_widgets()
        self.frame.show_form('Add client')
        self.frame.data_form.confirm_button.configure(command=self.add_client)

    def show_edit_form(self):
        # get selection
        client = self.frame.table.get_selection()
        self.frame.data_form.entry_values = client['values'][0:3]

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
    
    def show_conformation_frame(self):
        client = self.frame.table.get_selection()
        # check selection
        if client == 'no selection':
            self.view.show_messagebox(self.frame, title='Required fields', message='Please select a client to remove',
                                      icon='warning')
            return
        
        self.frame.hide_widgets()
        self.frame.show_frame('Confirm Removal')
        self.frame.conformation_frame.change_labels(client['values'][0:3])
        self.frame.conformation_frame.confirm_button.configure(command=lambda: self.delete_client())

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
        self.update_client_table()
        self.cancel_form()

    def edit_client(self):
        # gets imputted data from the user and the id from the client that is to be edited
        client_data = self.frame.data_form.get_data_from_entries()
        client_id = self.frame.table.get_selection()['values'][3]

        # edits client in the database
        self.model.client_model.edit_client(client_data, client_id)

        # update tables and return close form
        self.update_client_table()
        self.update_lent_table()
        self.cancel_form()

    def delete_client(self):
        client_id = self.frame.table.get_selection()['values'][3]

        #delete client from database
        self.model.client_model.delete_client(client_id)
        
        # update tables and close frame
        self.update_client_table()
        self.update_lent_table()
        self.cancel_frame()

    def update_client_table(self):
        self.frame.table.clear_rows()
        
        search_column = self.frame.search_bar.get_selected_column()
        search_input = self.frame.search_bar.get_search_input()
        view = self.frame.search_bar.get_selected_view()

        self.frame.table.insert_rows(self.model.client_model.search_clients(view, search_column, search_input))
    
    def update_lent_table(self):
        self.view.frames['lent'].table.clear_rows()

        search_input = self.view.frames['lent'].search_bar.get_search_input()
        search_column = self.view.frames['lent'].search_bar.get_selected_column()
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
        
        view = self.view.frames['lent'].search_bar.get_selected_view()
        if view == 'All borrowings':
            self.view.frames['lent'].table.treeview.configure(displaycolumns=['Book', 'Client', 'From', 'to', 'due'])
        elif view == 'Returned books':
            self.view.frames['lent'].table.treeview.configure(displaycolumns=['Book', 'Client', 'From', 'to'])
        else:            
            self.view.frames['lent'].table.treeview.configure(displaycolumns=['Book', 'Client', 'From', 'due'])

        self.view.frames['lent'].table.insert_rows(self.model.lent_model.search_lendings(view, search_column, search_input))