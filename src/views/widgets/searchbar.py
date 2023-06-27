import customtkinter as ctk
from PIL import Image
import os

from src.resources.config import IMAGES_DIR


class SearchBar(ctk.CTkFrame):
    def __init__(self, parent, view_names: list[str], view_index: int, column_names: list[str], height: int, width: int):
        super().__init__(parent, height=height, width=width, fg_color='transparent')

        # Load images
        self.search_image = ctk.CTkImage(Image.open(os.path.join(IMAGES_DIR, 'search_light.png')), size=(24, 24))

        # Prepare view names and set default
        view_names = [h.capitalize() for h in view_names]
        self.selected_view = ctk.StringVar()
        self.selected_view.set(view_names[view_index])

        # Prepare column names and set default
        column_names = [h.capitalize() for h in column_names]
        self.selected_column = ctk.StringVar()
        self.selected_column.set(column_names[0])
        
        # Dropdown menu for selecting table view
        self.view_dropdown = ctk.CTkOptionMenu(self, corner_radius=0, height=int(height), width=int(width*(1/4)),
                                               font=ctk.CTkFont(size=15), variable=self.selected_view, values=view_names)

        # Dropdown menu for selecting search column
        self.search_dropdown = ctk.CTkOptionMenu(self, corner_radius=0, height=int(height), width=int(width*(1/6)),
                                                 font=ctk.CTkFont(size=15), variable=self.selected_column,
                                                 values=column_names)

        # Input field for search query
        self.entry = ctk.CTkEntry(self, placeholder_text="Search", corner_radius=0, height=height,
                                  width=int(width*(4/6)), font=ctk.CTkFont(size=15))

        # Button for initiating the search
        self.button = ctk.CTkButton(self, text='', image=self.search_image, corner_radius=0, height=height,
                                    width=int(width*(1/6)))

        # Pack the widgets
        self.view_dropdown.pack(side=ctk.LEFT, anchor='w', padx=10)
        self.button.pack(side=ctk.RIGHT, anchor='w', padx=2)
        self.entry.pack(side=ctk.RIGHT, anchor='w', padx=2)
        self.search_dropdown.pack(side=ctk.RIGHT, anchor='w', padx=2)
        

    def get_search_input(self):
        """Return current value of search input field"""
        return self.entry.get()

    def get_selected_column(self):
        """Return selected search column from dropdown menu"""
        return self.selected_column.get()

    def get_selected_view(self):
        """Return selected view from dropdown menu"""
        return self.selected_view.get()