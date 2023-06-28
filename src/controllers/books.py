class BooksController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames['books']

        self.frame.table.insert_rows(
            self.model.database.execute_query('SELECT title, author, genre, language, book_id FROM available_books WHERE book_id != 1' ))
        self._bind()

    def _bind(self):
        # Add keyboard/button controls for entries
        self.frame.search_bar.entry.bind('<Return>', lambda e: self.update_book_table())
        self.frame.search_bar.button.configure(command=self.update_book_table)
        self.frame.search_bar.view_dropdown.configure(command=lambda _: self.update_book_table())

        self.frame.add_button.configure(command=self.show_add_form)
        self.frame.edit_button.configure(command=self.show_edit_form)
        self.frame.delete_button.configure(command=self.show_conformation_frame)
        self.frame.data_form.cancel_button.configure(command=self.cancel_form)
        self.frame.conformation_frame.confirm_button.configure(command=self.delete_book)
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
        self.frame.show_form('Add book')
        self.frame.data_form.confirm_button.configure(command=self.add_book)

    def show_edit_form(self):
        # get selection
        book = self.frame.table.get_selection()
        self.frame.data_form.entry_values = book['values'][0:4]

        # check selection
        if book == 'no selection':
            self.view.show_messagebox(self.frame, title='Required fields', message='Please select a book to edit',
                                      icon='warning')
            return

        # switch widgets
        self.frame.hide_widgets()
        self.frame.show_form('Edit book')
        self.frame.data_form.fill_entries(book['values'][0:4])
        self.frame.data_form.confirm_button.configure(command=lambda: self.edit_book())
    
    def show_conformation_frame(self):
        book = self.frame.table.get_selection()
        if book == 'no selection':
            self.view.show_messagebox(self.frame, title='Required fields', message='Please select a book to remove',
                                      icon='warning')
            return

        self.frame.hide_widgets()
        self.frame.show_frame('Confirm Removal')
        self.frame.conformation_frame.change_labels(book['values'][0:4])
        self.frame.conformation_frame.confirm_button.configure(command=lambda: self.delete_book())
    
    '''
    ===========================
    MODEL FUNCTIONS
    ===========================
    '''

    def add_book(self):
        # gets imputted data from the user
        book_data = self.frame.data_form.get_data_from_entries()

        if book_data == 'empty entry':
            self.view.show_messagebox(self.frame, title='Required fields', message='Please fill all entries',
                                      icon='warning')
            return

        # adds book to database
        self.model.book_model.add_book(book_data)

        # update the table and return to it
        self.update_book_table()
        self.cancel_form()

    def edit_book(self):
        # gets imputted data from the user and the id from the book that is to be edited
        book_data = self.frame.data_form.get_data_from_entries()
        book_id = self.frame.table.get_selection()['values'][4]

        # edits book in the database
        self.model.book_model.edit_book(book_data, book_id)

        # update tables and close form
        self.update_book_table()
        self.update_lent_table()
        self.cancel_form()
    
    def delete_book(self):
        book_id = self.frame.table.get_selection()['values'][4]

        #delete book from database
        self.model.book_model.delete_book(book_id)
        
        # update tables and close frame
        self.update_book_table()
        self.update_lent_table()
        self.cancel_frame()

    def update_book_table(self):
        self.frame.table.clear_rows()

        view = self.frame.search_bar.get_selected_view()
        search_input = self.frame.search_bar.get_search_input()
        search_column = self.frame.search_bar.get_selected_column()

        self.frame.table.insert_rows(self.model.book_model.search_books(view, search_column, search_input))
    
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