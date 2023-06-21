import customtkinter as ctk
from PIL import Image
import os

from .widgets.searchbar import SearchBar
from .widgets.custom_table import CustomTable
from .widgets.data_form import DataForm
from src.resources.config import IMAGES_DIR


class BooksView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color='transparent')
        self.grid_columnconfigure(0, weight=1)
        column_names = ['title', 'author', 'genre', 'language']

        # load images
        self.add_image = ctk.CTkImage(Image.open(os.path.join(IMAGES_DIR, 'add_light.png')),
                                      size=(24, 24))
        self.edit_image = ctk.CTkImage(Image.open(os.path.join(IMAGES_DIR, 'edit_light.png')),
                                       size=(24, 24))
        self.remove_image = ctk.CTkImage(Image.open(os.path.join(IMAGES_DIR, 'remove_light.png')),
                                         size=(24, 24))

        # create widgets
        self.header = ctk.CTkLabel(self, text='Manage books',
                                   font=ctk.CTkFont(size=25, weight='bold'))
        self.search_bar = SearchBar(self, column_names, 35, 700)
        self.table = CustomTable(self, column_names, [600, 600, 600, 600])
        self.data_form = DataForm(self, column_names, [''] * len(column_names))

        self.control_buttons = ctk.CTkFrame(self, fg_color='transparent')
        self.add_button = ctk.CTkButton(self.control_buttons, corner_radius=0, text='Add',
                                        text_color='#ffffff', font=ctk.CTkFont(size=15),
                                        anchor='n', image=self.add_image, compound=ctk.RIGHT)

        self.edit_button = ctk.CTkButton(self.control_buttons, corner_radius=0, text='Edit',
                                         text_color='#ffffff', font=ctk.CTkFont(size=15),
                                         anchor='n', image=self.edit_image, compound=ctk.RIGHT)

        self.remove_button = ctk.CTkButton(self.control_buttons, corner_radius=0, text='Remove',
                                           text_color='#ffffff', font=ctk.CTkFont(size=15),
                                           anchor='n', image=self.remove_image, compound=ctk.RIGHT)

        self.add_button.pack(side=ctk.LEFT, padx=10)
        self.edit_button.pack(side=ctk.LEFT, padx=10)
        self.remove_button.pack(side=ctk.LEFT, padx=10)

        self.show_widgets()
        self.hide_form()

    def show_form(self, header):
        self.data_form.header.configure(text=header)
        self.data_form.place(relx=0.5, rely=0.5, anchor='center')

    def hide_form(self):
        self.data_form.place_forget()
        self.data_form.empty_entries()

    def hide_widgets(self):
        self.header.grid_forget()
        self.search_bar.grid_forget()
        self.table.grid_forget()
        self.control_buttons.grid_forget()


    def show_widgets(self):
        self.header.grid(row=0, column=0, columnspan=2, pady=20)
        self.search_bar.grid(row=1, column=0, pady=20)
        self.table.grid(row=2, column=0, pady=20)
        self.control_buttons.grid(row=3, column=0, pady=20)
