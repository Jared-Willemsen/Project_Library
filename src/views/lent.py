import customtkinter as ctk
from PIL import Image
import os

from .widgets.searchbar import SearchBar
from .widgets.custom_table import CustomTable
from .widgets.confirmation_frame import ComfirmationFrame
from src.resources.config import IMAGES_DIR


class LentView(ctk.CTkFrame):
    def __init__(self, master) -> None:
        super().__init__(master, fg_color='transparent')
        self.grid_columnconfigure(0, weight=1)
        view_names = ['all borrowings', 'past borrowings', 'borrowed books', 'overdue books']
        column_names = ['Book', 'Client', 'From', 'to', 'due']

        # load images
        self.add_image = ctk.CTkImage(Image.open(os.path.join(IMAGES_DIR, 'add_light.png')),
                                      size=(24, 24))
        self.time_image = ctk.CTkImage(Image.open(os.path.join(IMAGES_DIR, 'extend_light.png')),
                                       size=(24, 24))
        self.remove_image = ctk.CTkImage(Image.open(os.path.join(IMAGES_DIR, 'return_light.png')),
                                         size=(24, 24))

        self.header = ctk.CTkLabel(self, text='Lent books',
                                   font=ctk.CTkFont(size=25, weight='bold'))
        self.search_bar = SearchBar(self, view_names, 0, column_names, 35, 700)
        self.table = CustomTable(self, column_names, [600, 600, 400, 400, 400])
        self.table.treeview.configure(displaycolumns=['Book', 'Client', 'From', 'to', 'due'])

        self.control_buttons = ctk.CTkFrame(self, fg_color='transparent')
        self.add_button = ctk.CTkButton(self.control_buttons, corner_radius=0, text='Borrow book',
                                        text_color='#ffffff', font=ctk.CTkFont(size=15),
                                        anchor='n', image=self.add_image, compound=ctk.RIGHT)

        self.extend_button = ctk.CTkButton(self.control_buttons, corner_radius=0, text='Extend',
                                           text_color='#ffffff', font=ctk.CTkFont(size=15),
                                           anchor='n', image=self.time_image, compound=ctk.RIGHT)

        self.return_button = ctk.CTkButton(self.control_buttons, corner_radius=0, text='Return',
                                           text_color='#ffffff', font=ctk.CTkFont(size=15),
                                           anchor='n', image=self.remove_image, compound=ctk.RIGHT)

        self.conformation_frame = ComfirmationFrame(self, ['book', 'client'])

        self.add_button.pack(side=ctk.LEFT, padx=10)
        self.extend_button.pack(side=ctk.LEFT, padx=10)
        self.return_button.pack(side=ctk.LEFT, padx=10)

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
        self.control_buttons.grid(row=3, column=0, padx=20, pady=20)

    def hide_widgets(self):
        self.header.grid_forget()
        self.search_bar.grid_forget()
        self.table.grid_forget()
        self.control_buttons.grid_forget()
