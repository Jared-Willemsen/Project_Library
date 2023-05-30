import customtkinter as ctk

from .widgets.searchbar import SearchBar
from .widgets.custom_table import CustomTable

class ReservationView(ctk.CTkFrame):
    def __init__(self, master) -> None:
        super().__init__(master, fg_color='transparent')
        self.grid_columnconfigure(0, weight=1)

        self.header = ctk.CTkLabel(self, text='Book reservation',
                                   font=ctk.CTkFont(size=25, weight='bold'))
        self.header.grid(row=0, column=0, padx=20, pady=20)

        column_names = ['Book', 'Client', 'From', 'To']
        self.search_bar = SearchBar(self, column_names, 35, 700)
        self.search_bar.grid(row=1, column=0, padx=20, pady=20)
        self.table = CustomTable(self, column_names, [600, 600, 600, 600])
        self.table.grid(row=2, column=0, padx=20, pady=20)