from .auth import Auth
from .database import Database
from .search import Search


class Model:
    """
    A class to manage MVC models
    """

    def __init__(self) -> None:
        self.database = Database()
        self.auth = Auth(self.database)
        self.search = Search(self.database)
