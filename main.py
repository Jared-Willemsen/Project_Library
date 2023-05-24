import logging

from src.models.main import Model
from src.views.main import View
from src.controllers.main import Controller


def configure_logging():
    logging.basicConfig(
        level=logging.WARNING,
        filename='logs/app.log',
        format='%(asctime)s | %(levelname)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )


def main():
    configure_logging()

    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.start()


if __name__ == '__main__':
    main()
