from typing import TypedDict

from .root import Root
from .login import LoginView
from .forgot_password import ForgotPasswordView
from .sidebar import SidebarView
from .overview import OverviewView
from .books import BooksView
from .clients import ClientsView
from .lent import LentView
from .reservation import ReservationView


class Frames(TypedDict):
    login: LoginView
    forgot_password: ForgotPasswordView
    sidebar: SidebarView
    overview: OverviewView
    books: BooksView
    clients: ClientsView
    lent: LentView
    reservation: ReservationView


class View:
    def __init__(self):
        self.root = Root()
        self.frames = {}
        self._create_frames()

    def _create_frames(self):
        self.frames['login'] = LoginView(self.root)
        self.frames['forgot_password'] = ForgotPasswordView(self.root)
        # self.frames['sidebar'] = SidebarView(self.root)
        self.frames['overview'] = OverviewView(self.root)
        self.frames['books'] = BooksView(self.root)
        self.frames['clients'] = ClientsView(self.root)
        self.frames['lent'] = LentView(self.root)
        self.frames['reservation'] = ReservationView(self.root)
        self.sidebar = SidebarView(self.root)

        # grid frames
        self.frames['login'].grid(row=0, column=0, rowspan=2, columnspan=2)
        self.frames['forgot_password'].grid(row=0, column=0, rowspan=2, columnspan=2)
        # self.frames['sidebar'].grid(row=0, column=0, sticky='nsew')
        self.frames['overview'].grid(row=0, column=1, sticky='nsew')
        self.frames['books'].grid(row=0, column=1, sticky='nsew')
        self.frames['clients'].grid(row=0, column=1, sticky='nsew')
        self.frames['lent'].grid(row=0, column=1, sticky='nsew')
        self.frames['reservation'].grid(row=0, column=1, sticky='nsew')
        self.sidebar.grid(row=0, column=0, sticky='nsew')

        # select default frame
        self.select_frame_by_name('login')

    def select_frame_by_name(self, name: str):
        if name not in self.frames:
            return

        self.hide_frames()
        self.sidebar.highlight_sidebar_selection(name)
        self.frames[name].grid()

        if name in ('login', 'forgot_password'):
            self.sidebar.toggle_visibility(visible=False)
        else:
            self.sidebar.toggle_visibility(visible=True)

    def hide_frames(self):
        for frame in self.frames.values():
            frame.grid_remove()

    def start_mainloop(self):
        self.root.mainloop()