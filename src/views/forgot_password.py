import customtkinter as ctk
from PIL import Image
import os
from CTkMessagebox import CTkMessagebox

from ..resources.config import IMAGES_DIR


class ForgotPasswordView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=5, fg_color=('gray85', 'gray10'))

        # load images
        self.logo_image = ctk.CTkImage(Image.open(os.path.join(IMAGES_DIR, 'customtkinter_logo_single.png')),
                                       size=(26, 26))

        # populate frame
        self.header = ctk.CTkLabel(self, text='  Reset password', text_color='gray25',
                                   font=ctk.CTkFont(size=35, weight='bold'), image=self.logo_image,
                                   compound='left')
        self.header.grid(row=0, column=1, padx=20, pady=25, columnspan=2)

        self.email_label = ctk.CTkLabel(self, text='Email', text_color='gray25', font=ctk.CTkFont(size=15),
                                        anchor='sw')
        self.email_label.grid(row=1, column=1, sticky='nw', padx=25)
        self.email_entry = ctk.CTkEntry(self, width=300, font=ctk.CTkFont(size=15),
                                        placeholder_text='name.surname@example.com')
        self.email_entry.grid(row=2, column=1, padx=20, pady=(0, 15))
        # self.username_entry.after(230, self.username_entry.focus_set)  # BUGFIX - Customtkinter fix focus_set

        self.login_button = ctk.CTkButton(self, height=40, width=200, border_spacing=10, text='Reset',
                                          text_color='#ffffff', font=ctk.CTkFont(size=20, weight='bold'),
                                          anchor='n')
        self.login_button.grid(row=6, column=1, columnspan=2, pady=20)

    def show_messagebox(self, **kwargs):
        CTkMessagebox(self, **kwargs)

    def clear_form(self):
        if self.email_entry.get():
            self.email_entry.delete(0, ctk.END)
