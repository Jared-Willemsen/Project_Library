import customtkinter as ctk

from .widgets.searchbar import SearchBar
from .widgets.custom_table import CustomTable


class BooksView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color='transparent')
        self.grid_columnconfigure(0, weight=1)

        self.header = ctk.CTkLabel(self, text='Manage books',
                                   font=ctk.CTkFont(size=25, weight='bold'))
        self.header.grid(row=0, column=0, padx=20, pady=20)

        column_names = ['title', 'author', 'genre', 'language']
        self.search_bar = SearchBar(self, column_names, 35, 700)
        self.search_bar.grid(row=1, column=0, padx=20, pady=20)
        self.table = CustomTable(self, column_names, [400, 400, 300, 300])
        self.table.grid(row=2, column=0, padx=20, pady=20)
