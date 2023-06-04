import customtkinter as ctk

from .widgets.searchbar import SearchBar
from .widgets.custom_table import CustomTable
from .widgets.data_form import DataForm

class LentView(ctk.CTkFrame):
    def __init__(self, master) -> None:
        super().__init__(master, fg_color='transparent')
        self.grid_columnconfigure(0, weight=1)
        column_names = ['Book', 'Client', 'From', 'To']

        self.header = ctk.CTkLabel(self, text='Lent books',
                                   font=ctk.CTkFont(size=25, weight='bold'))
        self.search_bar = SearchBar(self, column_names, 35, 700)
        self.table = CustomTable(self, column_names, [600, 600, 600, 600])
        self.data_form = DataForm(self, column_names, ['']*len(column_names))

        self.show_widgets()
        self.hide_form()
    
    def show_form(self, header):
        self.data_form.header.configure(text=header)
        self.data_form.place(relx=0.5, rely=0.5, anchor='center')

    def hide_form(self):
        self.data_form.place_forget()
        self.data_form.empty_entries()

    def show_widgets(self):
        self.header.grid(row=0, column=0, padx=20, pady=20)
        self.search_bar.grid(row=1, column=0, padx=20, pady=20)
        self.table.grid(row=2, column=0, padx=20, pady=20)

    def hide_widgets(self):
        self.header.grid_forget()
        self.search_bar.grid_forget()
        self.table.grid_forget()