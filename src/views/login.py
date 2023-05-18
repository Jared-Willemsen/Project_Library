import customtkinter as ctk
from PIL import Image
import os
from CTkMessagebox import CTkMessagebox

from src.config import IMAGES_DIR


class LoginView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=5, fg_color=('gray85', 'gray10'))

        # load images
        self.logo_image = ctk.CTkImage(Image.open(os.path.join(IMAGES_DIR, 'customtkinter_logo_single.png')),
                                       size=(30, 30))

        # populate frame
        self.header = ctk.CTkLabel(self, text='  Login your Account', text_color='gray25',
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

        self.password_label = ctk.CTkLabel(self, text='Password', text_color='gray25', font=ctk.CTkFont(size=15),
                                           anchor='sw')
        self.password_label.grid(row=3, column=1, sticky='nw', padx=25)
        self.password_entry = ctk.CTkEntry(self, width=300, show='•', placeholder_text='••••••••',
                                           font=ctk.CTkFont(size=15))
        self.password_entry.grid(row=4, column=1, padx=20, pady=(0, 15))

        self.show_password = ctk.BooleanVar()
        self.toggle_password_button = ctk.CTkCheckBox(self, text='Show', text_color='gray30',
                                                      font=ctk.CTkFont(size=15), variable=self.show_password)
        self.toggle_password_button.grid(row=4, column=2, pady=(0, 15))

        self.forgot_password = ctk.CTkLabel(self, text='Forgot your password?', text_color='#0074cc',
                                            font=ctk.CTkFont(size=15, underline=True), anchor='w', cursor='hand2')
        self.forgot_password.grid(row=5, column=1, padx=25, pady=10, columnspan=2, sticky='w')

        self.login_button = ctk.CTkButton(self, height=40, width=200, border_spacing=10, text='Login',
                                          text_color='#ffffff', font=ctk.CTkFont(size=20, weight='bold'),
                                          anchor='n')
        self.login_button.grid(row=6, column=1, columnspan=2, pady=20)

    def show_messagebox(self, **kwargs):
        CTkMessagebox(self, **kwargs)

    def clear_form(self):
        if self.password_entry.get():
            self.password_entry.delete(0, ctk.END)
        self.focus_set()
        self.show_password.set(False)
        self.toggle_password_visibility()

    def toggle_password_visibility(self):
        if self.show_password.get():
            self.toggle_password_button.configure(text='Hide')
            self.password_entry.configure(show='')
        else:
            self.toggle_password_button.configure(text='Show')
            self.password_entry.configure(show='•')
