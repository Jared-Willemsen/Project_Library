from .login import LoginController
from .forgot_password import ForgotPasswordController
from .sidebar import SidebarController
from .books import BooksController
from .clients import ClientsController
from .lent import LentController
# from .calendar_controller import CalendarController

class Controller:
    """
    A class to manage MVC controllers
    """

    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view

        self.loginin_controller = LoginController(model, view)
        self.forgot_password_controller = ForgotPasswordController(model, view)
        self.sidebar_controller = SidebarController(model, view)
        self.books_controller = BooksController(model, view)
        self.clients_controller = ClientsController(model, view)
        self.lent_controller = LentController(model, view)
        # self.calendar_controller = CalendarController(model, view)

    def start(self):
        self.view.start_mainloop()
