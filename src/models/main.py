from .auth import Auth
from .database import Database
from .search import Search
from .book_model import BookModel


class Model:
    """
    A class to manage MVC models
    """

    def __init__(self) -> None:
        self.database = Database()
        
        self.book_model = BookModel(self.database)
        self.auth = Auth(self.database)
        self.search = Search(self.database)
