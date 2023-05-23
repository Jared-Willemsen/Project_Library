from .login import LoginController
from .sidebar import SidebarController
from .books import BooksController
from .clients import ClientsController


class Controller:
    """
    A class to manage MVC controllers
    """

    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view

        self.signin_controller = LoginController(model, view)
        self.sidebar_controller = SidebarController(model, view)
        self.books_controller = BooksController(model, view)
        self.clients_controller = ClientsController(model, view)

    def start(self):
        self.view.start_mainloop()
