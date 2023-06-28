import customtkinter as ctk
from PIL import Image
import os
from CTkMessagebox import CTkMessagebox

from src.resources.config import IMAGES_DIR


class LoginView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=5, fg_color='transparent')

        # load images
        self.logo_image = ctk.CTkImage(Image.open(os.path.join(IMAGES_DIR, 'libraryicon.png')),
                                       size=(400, 117))

        # populate frame
        self.logo_label = ctk.CTkLabel(self, text='', image=self.logo_image)
        self.logo_label.grid(row=0, column=1, padx=20, pady=25)

        self.container = ctk.CTkFrame(self, fg_color=('gray85', 'gray10'))
        self.container.grid(row=1, column=1)

        self.header = ctk.CTkLabel(self.container, text='Login', text_color='gray25',
                                   font=ctk.CTkFont(size=25, weight='bold'))
        self.header.grid(row=1, column=1, padx=20, pady=15, columnspan=2)

        self.email_label = ctk.CTkLabel(self.container, text='Email', text_color='gray25', font=ctk.CTkFont(size=15),
                                        anchor='sw')
        self.email_label.grid(row=2, column=1, sticky='nw', padx=25)
        self.email_entry = ctk.CTkEntry(self.container, width=300, font=ctk.CTkFont(size=15),
                                        placeholder_text='name.surname@example.com')
        self.email_entry.grid(row=3, column=1, padx=20, pady=(0, 15))
        # self.username_entry.after(230, self.username_entry.focus_set)  # BUGFIX - Customtkinter fix focus_set

        self.password_label = ctk.CTkLabel(self.container, text='Password', text_color='gray25', font=ctk.CTkFont(size=15),
                                           anchor='sw')
        self.password_label.grid(row=4, column=1, sticky='nw', padx=25)
        self.password_entry = ctk.CTkEntry(self.container, width=300, show='•', placeholder_text='••••••••',
                                           font=ctk.CTkFont(size=15))
        self.password_entry.grid(row=5, column=1, padx=20, pady=(0, 15))

        self.show_password = ctk.BooleanVar()
        self.toggle_password_button = ctk.CTkCheckBox(self.container, text='Show', text_color='gray30',
                                                      font=ctk.CTkFont(size=15), variable=self.show_password)
        self.toggle_password_button.grid(row=5, column=2, pady=(0, 15))

        self.forgot_password = ctk.CTkLabel(self.container, text='Forgot your password?', text_color='#0074cc',
                                            font=ctk.CTkFont(size=15, underline=True), anchor='w', cursor='hand2')
        self.forgot_password.grid(row=6, column=1, padx=25, pady=(10, 5), columnspan=2, sticky='w')

        self.guest_login_button = ctk.CTkLabel(self.container, text='Continue as guest', text_color='#0074cc',
                                            font=ctk.CTkFont(size=15, underline=True), anchor='w', cursor='hand2')
        self.guest_login_button.grid(row=7, column=1, padx=25, pady=(5, 10), columnspan=2, sticky='w')
        # TODO: add guest login access level

        self.login_button = ctk.CTkButton(self.container, height=40, width=200, border_spacing=10, text='Login',
                                          text_color='#ffffff', font=ctk.CTkFont(size=20, weight='bold'),
                                          anchor='n')
        self.login_button.grid(row=8, column=1, columnspan=2, pady=20)

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
