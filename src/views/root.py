import customtkinter as ctk
import os

from ..resources.config import IMAGES_DIR


class Root(ctk.CTk):
    """
    The main window for the GUI.
    """

    def __init__(self):
        super().__init__()

        self.title('Library Manager')
        self.minsize(1280, 720)
        self.after(0, lambda: self.state('zoomed'))  # BUGFIX - Customtkinter fix full screen
        self.bind('<Map>', lambda event: self.update())  # BUGFIX - Minimize window redraw glitch

        # load icon
        self.iconbitmap(True, os.path.join(IMAGES_DIR, 'icon.ico'))

        # configure customtkinter
        ctk.set_appearance_mode('light')
        ctk.set_default_color_theme('blue')

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
