from .auth import Auth
from .database import Database


class Model:
    """
    A class to manage MVC models
    """

    def __init__(self) -> None:
        self.database = Database()
        self.auth = Auth(self.database)
