class LoginController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames['login']
        self._bind()

    def _bind(self):
        self.frame.login_button.configure(command=self.login)
        self.frame.toggle_password_button.configure(command=self.frame.toggle_password_visibility)
        self.frame.forgot_password.bind("<Button-1>", lambda e: self.view.select_frame_by_name('forgot_password'))

    def login(self):
        email = self.frame.email_entry.get()
        password = self.frame.password_entry.get()
        self.frame.clear_form()

        if self.model.auth.login(email, password):
            self.view.select_frame_by_name('overview')
        elif email == '' and password == '':
            self.frame.show_messagebox(title='Required fields', message='Please enter email and password', header=True,
                                       icon='warning')
        elif email == '':
            self.frame.show_messagebox(title='Required fields', message='Please enter email', header=True,
                                       icon='warning')
        elif password == '':
            self.frame.show_messagebox(title='Required fields', message='Please enter password', header=True,
                                       icon='warning')
        else:
            self.frame.show_messagebox(title='Unable to login', message='Invalid email or password', header=True,
                                       icon='warning')
