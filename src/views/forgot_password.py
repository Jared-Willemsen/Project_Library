import customtkinter as ctk
from PIL import Image
import os

from src.resources.config import IMAGES_DIR


class ForgotPasswordView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=5, fg_color=('gray85', 'gray10'))

        # load images
        self.arrow_back_image = ctk.CTkImage(Image.open(os.path.join(IMAGES_DIR, 'back_light.png')),
                                             size=(20, 20))

        # populate frame
        self.header = ctk.CTkLabel(self, text='Forgot your password?', text_color='gray25',
                                   font=ctk.CTkFont(size=25, weight='bold'))
        self.header.grid(row=0, column=0, padx=20, pady=25, columnspan=2)

        self.back_button = ctk.CTkButton(self, text='', image=self.arrow_back_image, width=40, height=30)
        self.back_button.grid(row=1, column=0, sticky='w', padx=20, pady=(0, 20))

        # Step 1: forgot your password?
        self.email_text = "Please enter the email you use to sign in to Alexandria Library."
        self.email_textlabel = ctk.CTkLabel(self, text=self.email_text,
                                            text_color='gray25', font=ctk.CTkFont(size=15), wraplength=350,
                                            anchor="w",
                                            justify="left")
        self.email_textlabel.grid(row=2, column=0, sticky='w', padx=15, pady=10)
        self.email_label = ctk.CTkLabel(self, text='Email', text_color='gray25', font=ctk.CTkFont(size=15),
                                        anchor='sw')
        self.email_label.grid(row=3, column=0, sticky='nw', padx=25)
        self.email_entry = ctk.CTkEntry(self, width=300, font=ctk.CTkFont(size=15),
                                        placeholder_text='name.surname@example.com')
        self.email_entry.grid(row=4, column=0, padx=20, pady=(0, 15))

        self.email_button = ctk.CTkButton(self, height=40, width=200, border_spacing=10, text='Request password reset',
                                          text_color='#ffffff', font=ctk.CTkFont(size=20, weight='bold'),
                                          anchor='n')
        self.email_button.grid(row=5, column=0, columnspan=2, pady=20)

        # Step 2: reset token password
        self.stored_email = ""
        self.reset_token_text = f"""You have requested a password reset. To get a new password, please check your Inbox from Alexandria Library and enter the Password reset code we have sent to: {self.stored_email}"""  # nopep8
        self.reset_token_textlabel = ctk.CTkLabel(self, text=self.reset_token_text,
                                                  text_color='gray25', font=ctk.CTkFont(size=15), wraplength=350,
                                                  anchor="w",
                                                  justify="left")
        self.reset_token_textlabel.grid(row=2, column=0, sticky='w', padx=15, pady=10)
        self.reset_token_label = ctk.CTkLabel(self, text='Password reset token', text_color='gray25',
                                              font=ctk.CTkFont(size=15), anchor='sw')
        self.reset_token_label.grid(row=3, column=0, sticky='nw', padx=25)
        self.reset_token_entry = ctk.CTkEntry(self, width=300, font=ctk.CTkFont(size=15),
                                              placeholder_text='000 000')
        self.reset_token_entry.grid(row=4, column=0, padx=20, pady=(0, 15))

        # Validate the reset_token_entry input
        vcmd = (self.register(self.validate_token_entry), '%P')
        self.reset_token_entry.configure(validate="key", validatecommand=vcmd)

        # Format the input on focus out
        self.reset_token_entry.bind("<KeyRelease>", lambda event: self.format_token_entry())

        self.reset_token_textlabel.grid_remove()
        self.reset_token_label.grid_remove()
        self.reset_token_entry.grid_remove()

        self.reset_token_button = ctk.CTkButton(self, height=40, width=200, border_spacing=10, text='Confirm',
                                                text_color='#ffffff', font=ctk.CTkFont(size=20, weight='bold'),
                                                anchor='n')
        self.reset_token_button.grid(row=5, column=0, columnspan=2, pady=20)
        self.reset_token_button.grid_remove()

        # Step 3: new password
        self.new_password_text = "Here you can set new password for signing in to Alexandria Library. Make sure you remember this password and keep it in a safe place."  # nopep8
        self.new_password_textlabel = ctk.CTkLabel(self, text=self.new_password_text,
                                                   text_color='gray25', font=ctk.CTkFont(size=15), wraplength=350,
                                                   anchor="w",
                                                   justify="left")
        self.new_password_textlabel.grid(row=2, column=0, sticky='w', padx=15, pady=10)
        self.new_password_label = ctk.CTkLabel(self, text='New password', text_color='gray25',
                                               font=ctk.CTkFont(size=15),
                                               anchor='sw')
        self.new_password_label.grid(row=3, column=0, sticky='nw', padx=25)
        self.new_password_entry = ctk.CTkEntry(self, width=300, font=ctk.CTkFont(size=15),
                                               placeholder_text='8 characters minimum', show='•')
        self.new_password_entry.grid(row=4, column=0, padx=20, pady=(0, 15))
        self.show_password = ctk.BooleanVar()
        self.toggle_password_button = ctk.CTkCheckBox(self, text='Show', text_color='gray30',
                                                      font=ctk.CTkFont(size=15), variable=self.show_password)
        self.toggle_password_button.grid(row=4, column=1, pady=(0, 15))
        self.new_password_textlabel.grid_remove()
        self.toggle_password_button.grid_remove()
        self.new_password_label.grid_remove()
        self.new_password_entry.grid_remove()

        self.confirm_password_label = ctk.CTkLabel(self, text='Confirm new password', text_color='gray25',
                                                   font=ctk.CTkFont(size=15),
                                                   anchor='sw')
        self.confirm_password_label.grid(row=5, column=0, sticky='nw', padx=25)
        self.confirm_password_entry = ctk.CTkEntry(self, width=300, font=ctk.CTkFont(size=15),
                                                   placeholder_text='8 characters minimum', show='•')
        self.confirm_password_entry.grid(row=6, column=0, padx=20, pady=(0, 15))
        self.confirm_password_label.grid_remove()
        self.confirm_password_entry.grid_remove()

        self.new_password_button = ctk.CTkButton(self, height=40, width=200, border_spacing=10, text='Set new password',
                                                 text_color='#ffffff', font=ctk.CTkFont(size=20, weight='bold'),
                                                 anchor='n')
        self.new_password_button.grid(row=7, column=0, columnspan=2, pady=20)
        self.new_password_button.grid_remove()

    def ungrid_all(self):
        self.email_textlabel.grid_remove()
        self.email_label.grid_remove()
        self.email_entry.grid_remove()
        self.email_button.grid_remove()
        self.reset_token_textlabel.grid_remove()
        self.reset_token_entry.grid_remove()
        self.reset_token_label.grid_remove()
        self.reset_token_button.grid_remove()
        self.new_password_textlabel.grid_remove()
        self.new_password_label.grid_remove()
        self.new_password_entry.grid_remove()
        self.confirm_password_label.grid_remove()
        self.confirm_password_entry.grid_remove()
        self.new_password_button.grid_remove()
        self.toggle_password_button.grid_remove()

    def reset_form(self):
        """Set form to state 1: enter email"""
        self.ungrid_all()
        self.show_password.set(False)
        self.toggle_password_visibility()
        self.email_textlabel.grid()
        self.email_label.grid()
        self.email_entry.grid()
        self.email_button.grid()

    def submit_email(self):
        """Set form to state 2: enter token"""
        self.email_label.grid_remove()
        self.email_entry.grid_remove()
        self.email_button.grid_remove()
        self.reset_token_textlabel.grid()
        self.reset_token_label.grid()
        self.reset_token_entry.grid()
        self.reset_token_button.grid()

    def validate_token_entry(self, text):
        # Check if the input consists of digits and spaces only
        if all(char.isdigit() or char.isspace() for char in text) and len(''.join(filter(str.isdigit, text))) <= 6:
            return True
        else:
            return False

    def format_token_entry(self):
        # Get the current entry text
        entry_text = self.reset_token_entry.get()

        # Remove any non-digit and non-space characters from the text
        entry_text = ''.join(filter(str.isdigit, entry_text))

        # Insert a space after every third character
        formatted_text = ' '.join([entry_text[i:i + 3] for i in range(0, len(entry_text), 3)])

        # Update the entry text with the formatted version
        self.reset_token_entry.delete(0, ctk.END)
        self.reset_token_entry.insert(0, formatted_text)

    def get_token_entry(self):
        # Get the current entry text
        entry_text = self.reset_token_entry.get()

        # Remove any non-digit and non-space characters from the text
        entry_text = ''.join(filter(str.isdigit, entry_text))

        return entry_text

    def submit_reset_token(self):
        """Set form to state 3: enter new password"""
        self.reset_token_textlabel.grid_remove()
        self.reset_token_entry.grid_remove()
        self.reset_token_label.grid_remove()
        self.reset_token_button.grid_remove()
        self.new_password_textlabel.grid()
        self.new_password_label.grid()
        self.new_password_entry.grid()
        self.confirm_password_label.grid()
        self.confirm_password_entry.grid()
        self.new_password_button.grid()
        self.toggle_password_button.grid()

    def clear_form(self):
        if self.email_entry.get():
            self.email_entry.delete(0, ctk.END)
        if self.reset_token_entry.get():
            self.reset_token_entry.delete(0, ctk.END)
        if self.new_password_entry.get():
            self.new_password_entry.delete(0, ctk.END)
        if self.confirm_password_entry.get():
            self.confirm_password_entry.delete(0, ctk.END)

    def toggle_password_visibility(self):
        if self.show_password.get():
            self.toggle_password_button.configure(text='Hide')
            self.new_password_entry.configure(show='')
            self.confirm_password_entry.configure(show='')
        else:
            self.toggle_password_button.configure(text='Show')
            self.new_password_entry.configure(show='•')
            self.confirm_password_entry.configure(show='•')
