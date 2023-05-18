from .auth import Auth
from .database import Database
from .Search import Search

class Model:
    def __init__(self) -> None:
        self.database = Database()
        self.auth = Auth(self.database)
        self.search = Search(self.database)