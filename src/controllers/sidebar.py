class SidebarController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.sidebar
        self._bind()

    def _bind(self):
        self.frame.overview_button.configure(command=lambda: self.view.select_frame_by_name('overview'))
        self.frame.books_button.configure(command=lambda: self.view.select_frame_by_name('books'))
        self.frame.clients_button.configure(command=lambda: self.view.select_frame_by_name('clients'))
        self.frame.lent_button.configure(command=lambda: self.view.select_frame_by_name('lent'))
        self.frame.logout_button.configure(command=lambda: self.view.select_frame_by_name('login'))
