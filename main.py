from src.models.main import Model
from src.views.main import View
from src.controllers.main import Controller


def main():
    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.start()


if __name__ == '__main__':
    main()
