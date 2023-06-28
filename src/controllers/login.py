import sys

class LoginController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames['login']
        self._bind()

    def _bind(self):
        # Add keyboard controls for entries
        self.frame.email_entry.bind('<Return>', lambda e: self.frame.password_entry.focus()) 
        self.frame.password_entry.bind('<Return>', lambda e: self.login())

        self.frame.login_button.configure(command=self.login)
        self.frame.toggle_password_button.configure(command=self.frame.toggle_password_visibility)
        self.frame.forgot_password.bind("<Button-1>", lambda e: self.view.select_frame_by_name('forgot_password'))
        self.frame.guest_login_button.bind("<Button-1>", lambda e: self.view.hidden_frame_by_name('books'))

    def login(self):
        email = self.frame.email_entry.get()
        password = self.frame.password_entry.get()
        self.frame.clear_form()
        access = [None,'Manager','Librarian','Clerk','Janitor','Security Guard']

        if email == '' and password == '':
            self.frame.show_messagebox(title='Required fields', message='Please enter email and password',
                                       cancel_button='cross', icon='warning')
        elif email == '':
            self.frame.show_messagebox(title='Required fields', message='Please enter email', cancel_button='cross',
                                       icon='warning')
        elif password == '':
            self.frame.show_messagebox(title='Required fields', message='Please enter password', cancel_button='cross',
                                       icon='warning')
        else:
            if self.model.auth.login(email, password):

                level_of_access = self.model.auth.levelOfAccessStaff(email, password)

                if not level_of_access:
                    self.frame.show_messagebox(title='Access denied', message='Your account is suspended. Please report to the nearest librarian', cancel_button='cross',
                                       icon='warning')
                    return

                for index, access_level in enumerate(access):
                    if level_of_access == access_level:
                        print(access[index])
                        break  
                    
                self.view.select_frame_by_name('overview')
            else:
                
                if self.model.auth.levelOfAccessClient(email, password):
                    self.view.hidden_frame_by_name('books')
                else:
                    self.frame.show_messagebox(title='Unable to login', message='Invalid email or password',
                                            cancel_button='cross', icon='warning')
