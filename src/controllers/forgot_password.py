class ForgotPasswordController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames['forgot_password']
        self._bind()

    def _bind(self):
        self.frame.back_button.configure(command=lambda: self.view.select_frame_by_name('login'))
        self.frame.login_button.configure(command=self.reset_password)

    def reset_password(self):
        email = self.frame.email_entry.get()
        self.frame.clear_form()

        if email == '':
            self.frame.show_messagebox(title='Required fields', message='Please enter email',
                                       cancel_button='cross', icon='warning')
        else:
            self.frame.show_messagebox(title='Info', message='Password reset successfully!',
                                       cancel_button='cross', icon='info')
            # TODO: add logic and email_notification
