from .auth import Auth
from .database import Database
from .search import Search
from .book_model import BookModel
from .lent_model import LentModel


class Model:
    """
    A class to manage MVC models
    """

    def __init__(self) -> None:
        self.database = Database()
        self.lent_model = LentModel(self.database)
        self.book_model = BookModel(self.database)
        self.auth = Auth(self.database)
        self.search = Search(self.database)
