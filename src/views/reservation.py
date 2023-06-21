import customtkinter as ctk

from .widgets.searchbar import SearchBar
from .widgets.custom_table import CustomTable
from .widgets.confirmation_frame import ComfirmationFrame

class ReservationView(ctk.CTkFrame):
    def __init__(self, master) -> None:
        super().__init__(master, fg_color='transparent')
        self.grid_columnconfigure(0, weight=1)
        column_names = ['Book', 'Client', 'From', 'To']

        self.header = ctk.CTkLabel(self, text='Book reservation',
                                   font=ctk.CTkFont(size=25, weight='bold'))
        self.search_bar = SearchBar(self, column_names, 35, 700)
        self.table = CustomTable(self, column_names, [600, 600, 600, 600])
        self.add_button = ctk.CTkButton(self, text='add')
        self.conformation_frame = ComfirmationFrame(self, ['Book', 'Client'])

        self.show_widgets()
        self.hide_form()

    def show_form(self, header):
        self.conformation_frame.header.configure(text=header)
        self.conformation_frame.place(relx=0.5, rely=0.5, anchor='center')

    def hide_form(self):
        self.conformation_frame.place_forget()
        
    def show_widgets(self):
        self.header.grid(row=0, column=0, padx=20, pady=20)
        self.search_bar.grid(row=1, column=0, padx=20, pady=20)
        self.table.grid(row=2, column=0, padx=20, pady=20)
        self.add_button.grid(row=3, column=0)

    def hide_widgets(self):
        self.header.grid_forget()
        self.search_bar.grid_forget()
        self.table.grid_forget()
        self.add_button.grid_forget()