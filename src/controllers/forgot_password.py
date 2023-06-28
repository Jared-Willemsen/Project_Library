from src.send_email import send_reset_password_request, send_reset_password_confirmation


class ForgotPasswordController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames['forgot_password']
        self._bind()

    def _bind(self):
        # back button
        self.frame.back_button.configure(command=lambda: self.view.select_frame_by_name('login'))
        # email form
        self.frame.email_entry.bind('<Return>', lambda e: self.handle_submit_email())
        self.frame.email_button.configure(command=self.handle_submit_email)
        # reset token form
        self.frame.reset_token_entry.bind('<Return>', lambda e: self.handle_submit_token())
        self.frame.reset_token_button.configure(command=self.handle_submit_token)
        # new password form
        self.frame.new_password_entry.bind('<Return>', lambda e: self.frame.confirm_password_entry.focus())
        self.frame.confirm_password_entry.bind('<Return>', lambda e: self.handle_submit_password())
        self.frame.new_password_button.configure(command=self.handle_submit_password)
        self.frame.toggle_password_button.configure(command=self.frame.toggle_password_visibility)

    def handle_submit_email(self):
        email = self.frame.email_entry.get()
        if not email:
            self.view.show_messagebox(self.frame, title='Required fields', message='Please enter email',
                                      icon='warning')
        elif not self.model.auth.is_valid_email(email):
            self.view.show_messagebox(self.frame, title='Check input', message='Invalid email format',
                                      icon='warning')
        elif not self.model.auth.is_employee(email):
            self.view.show_messagebox(self.frame, title='Check input', message="We are not able to identify you",
                                      icon='warning')
        else:
            token = self.model.auth.generate_token()
            self.model.auth.insert_token_to_db(email, token)
            if send_reset_password_request(self.model.database, email, token):
                self.frame.stored_email = email
                self.frame.submit_email()
            else:
                self.view.show_messagebox(self.frame, title='Check input', message='Please check email',
                                          icon='warning')

    def handle_submit_token(self):
        email = self.frame.email_entry.get()
        token = self.frame.get_token_entry()
        print(token)
        if not token:
            self.view.show_messagebox(self.frame, title='Required fields', message='Please enter token',
                                      icon='warning')
        else:
            if self.model.auth.redeem_token(token, email):
                self.frame.submit_reset_token()
            else:
                self.view.show_messagebox(self.frame, title='Check input', message='Invalid/outdated token',
                                          icon='warning')

    def handle_submit_password(self):
        email = self.frame.email_entry.get()
        new_password = self.frame.new_password_entry.get()
        confirm_password = self.frame.confirm_password_entry.get()
        if not (new_password and confirm_password):
            self.view.show_messagebox(self.frame, title='Required fields', message='Please fill all fields',
                                      icon='warning')
        elif new_password != confirm_password:
            self.view.show_messagebox(self.frame, title='Check input', message='Passwords do not match',
                                      icon='warning')
        elif len(new_password) < 8:
            self.view.show_messagebox(self.frame, title='Check input', message='Password must be at least 8 characters',
                                      icon='warning')
        else:
            self.model.auth.update_password(email, new_password)
            send_reset_password_confirmation(self.model.database, email)
            self.frame.clear_form()
            self.frame.reset_form()
            self.view.select_frame_by_name('login')
            self.view.show_messagebox(self.frame, title='Success', message='Your password has been reset successfully!',
                                      icon='info')
