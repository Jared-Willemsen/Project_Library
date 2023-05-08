import customtkinter as ctk
import tkinter.messagebox as messagebox
import os
from PIL import Image
from src.enums.frames import Frame


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Library Manager')
        self.minsize(1280, 720)
        self.after(0, lambda: self.state('zoomed'))  # BUGFIX - Do not delete
        ctk.set_appearance_mode('light')
        ctk.set_default_color_theme('blue')

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self._create_gui()

    def _create_gui(self):
        # create authentication page
        self.login_page = LoginFrame(self)

        # create main page
        self.sidebar = Sidebar(self)
        self.overview_frame = OverviewFrame(self)
        self.books_frame = BooksFrame(self)
        self.clients_frame = ClientsFrame(self)
        self.lent_frame = LentFrame(self)
        self.reservation_frame = ReservationFrame(self)

        # grid frames
        self.login_page.grid(row=0, column=0, rowspan=2, columnspan=2)
        self.sidebar.grid(row=0, column=0, sticky='nsew')
        self.overview_frame.grid(row=0, column=1, sticky='nsew')
        self.books_frame.grid(row=0, column=1, sticky='nsew')
        self.clients_frame.grid(row=0, column=1, sticky='nsew')
        self.lent_frame.grid(row=0, column=1, sticky='nsew')
        self.reservation_frame.grid(row=0, column=1, sticky='nsew')

        # select default frame
        self.select_frame_by_name(Frame.Login)

    def select_frame_by_name(self, name):
        self.hide_frames()

        # show selected frame
        if name == Frame.Login:
            self.login_page.grid()
            self.sidebar.grid_remove()
        elif name == Frame.ForgotPassword:
            pass
        else:
            # show sidebar
            self.sidebar.grid()

            # show sidebar selected item
            self.sidebar.overview_button.configure(
                fg_color=('gray75', 'gray25') if name == Frame.Overview else 'transparent')
            self.sidebar.books_button.configure(fg_color=('gray75', 'gray25') if name == Frame.Books else 'transparent')
            self.sidebar.clients_button.configure(
                fg_color=('gray75', 'gray25') if name == Frame.Clients else 'transparent')
            self.sidebar.lent_button.configure(fg_color=('gray75', 'gray25') if name == Frame.Lent else 'transparent')
            self.sidebar.reservation_button.configure(
                fg_color=('gray75', 'gray25') if name == Frame.Reservation else 'transparent')

            if name == Frame.Overview:
                self.overview_frame.grid()
            if name == Frame.Books:
                self.books_frame.grid()
            if name == Frame.Clients:
                self.clients_frame.grid()
            if name == Frame.Lent:
                self.lent_frame.grid()
            if name == Frame.Reservation:
                self.reservation_frame.grid()

    def hide_frames(self):
        self.login_page.grid_remove()
        self.overview_frame.grid_remove()
        self.books_frame.grid_remove()
        self.clients_frame.grid_remove()
        self.lent_frame.grid_remove()
        self.reservation_frame.grid_remove()


class LoginFrame(ctk.CTkFrame):
    def __init__(self, master: App):
        super().__init__(master, corner_radius=5, fg_color='#D9D9D9')
        self.master: App = master
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images
        self.logo_image = ctk.CTkImage(Image.open(os.path.join('src', 'images', 'customtkinter_logo_single.png')),
                                       size=(26, 26))

        # create widgets
        self.login_label = ctk.CTkLabel(self, text='  Login your Account', text_color='gray25',
                                        font=ctk.CTkFont(size=35, weight='bold'), image=self.logo_image,
                                        compound='left')
        self.login_label.grid(row=0, column=1, padx=20, pady=25, columnspan=2)

        self.username_entry = ctk.CTkEntry(self, width=300, placeholder_text='Username',
                                           font=ctk.CTkFont(size=15))
        self.username_entry.grid(row=1, column=1, padx=20, pady=15)
        # self.username_entry.focus_set()

        self.password_entry = ctk.CTkEntry(self, width=300, placeholder_text='Password', show='•',
                                           font=ctk.CTkFont(size=15))
        self.password_entry.grid(row=2, column=1, padx=20, pady=15)

        self.show_password = ctk.BooleanVar()
        self.toggle_password_button = ctk.CTkCheckBox(self, text='Show', text_color='gray30',
                                                      font=ctk.CTkFont(size=15), variable=self.show_password,
                                                      command=self.toggle_password_visibility)
        self.toggle_password_button.grid(row=2, column=2)

        self.forgot_password = ctk.CTkLabel(self, text='Forgot password?', text_color='#0074cc',
                                            font=ctk.CTkFont(size=15, underline=True), anchor='w', cursor='hand2')
        self.forgot_password.grid(row=3, column=1, padx=20, pady=10, columnspan=2, sticky='w')
        self.forgot_password.bind("<Button-1>", lambda e: master.select_frame_by_name(Frame.ForgotPassword))

        self.login_button = ctk.CTkButton(self, height=40, width=200, border_spacing=10, text='Login',
                                          text_color='#ffffff', font=ctk.CTkFont(size=20, weight='bold'),
                                          anchor='n', command=self.login_button_event)
        self.login_button.grid(row=4, column=1, columnspan=2, pady=20)

    def login_button_event(self):
        # perform login validation
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == 'admin' and password == '1234':
            self.clear_login_page()
            self.master.select_frame_by_name(Frame.Overview)
        elif username == '' and password == '':
            messagebox.showwarning(title='Required fields', message='Please enter username and password')
        elif username == '':
            messagebox.showwarning(title='Required fields', message='Please enter username')
        elif password == '':
            messagebox.showwarning(title='Required fields', message='Please enter password')
        else:
            messagebox.showwarning(title='Unable to login', message='Invalid username or password')
            self.password_entry.delete(0, ctk.END)
        # TODO: This should be replaced with proper database validation in the future.
        # TODO: Secure from SQL injection

    def clear_login_page(self):
        self.password_entry.delete(0, ctk.END)
        self.username_entry.delete(0, ctk.END)
        # self.username_entry.focus_set()
        self.show_password.set(False)
        self.toggle_password_visibility()

    def toggle_password_visibility(self):
        if self.show_password.get():
            self.toggle_password_button.configure(text='Hide')
            self.password_entry.configure(show='')
        else:
            self.toggle_password_button.configure(text='Show')
            self.password_entry.configure(show='•')


class Sidebar(ctk.CTkFrame):
    def __init__(self, master: App):
        super().__init__(master, corner_radius=0)
        self.master = master
        self.grid_rowconfigure(6, weight=1)  # NOTE: change it when adding more buttons

        # load images
        self.logo_image = ctk.CTkImage(Image.open(os.path.join('src', 'images', 'customtkinter_logo_single.png')),
                                       size=(26, 26))
        self.overview_image = ctk.CTkImage(light_image=Image.open(os.path.join('src', 'images', 'overview_dark.png')),
                                           size=(20, 20))
        self.clients_image = ctk.CTkImage(light_image=Image.open(os.path.join('src', 'images', 'clients_dark.png')),
                                          size=(25, 25))
        self.books_image = ctk.CTkImage(light_image=Image.open(os.path.join('src', 'images', 'books_dark.png')),
                                        size=(25, 25))
        self.logout_image = ctk.CTkImage(light_image=Image.open(os.path.join('src', 'images', 'logout_dark.png')),
                                         size=(25, 25))
        self.lent_image = ctk.CTkImage(light_image=Image.open(os.path.join('src', 'images', 'lent_dark.png')),
                                       size=(25, 25))
        self.reservation_image = ctk.CTkImage(
            light_image=Image.open(os.path.join('src', 'images', 'reservation_dark.png')), size=(20, 20))

        # create widgets
        self.label = ctk.CTkLabel(self, text='  Library Manager',
                                  image=self.logo_image,
                                  compound='left', font=ctk.CTkFont(size=15, weight='bold'))
        self.label.grid(row=0, column=0, padx=20, pady=20)

        self.overview_button = ctk.CTkButton(self, corner_radius=0, height=40, border_spacing=10,
                                             text='Overview', fg_color='transparent', text_color=('gray10', 'gray90'),
                                             hover_color=('gray70', 'gray30'), image=self.overview_image, anchor='w',
                                             command=lambda: master.select_frame_by_name(Frame.Overview))
        self.overview_button.grid(row=1, column=0, sticky='ew')

        self.books_button = ctk.CTkButton(self, corner_radius=0, height=40, border_spacing=10,
                                          text='Books', fg_color='transparent', text_color=('gray10', 'gray90'),
                                          hover_color=('gray70', 'gray30'), image=self.books_image, anchor='w',
                                          command=lambda: master.select_frame_by_name(Frame.Books))
        self.books_button.grid(row=2, column=0, sticky='ew')

        self.clients_button = ctk.CTkButton(self, corner_radius=0, height=40, border_spacing=10,
                                            text='Clients', fg_color='transparent', text_color=('gray10', 'gray90'),
                                            hover_color=('gray70', 'gray30'), image=self.clients_image, anchor='w',
                                            command=lambda: master.select_frame_by_name(Frame.Clients))
        self.clients_button.grid(row=3, column=0, sticky='ew')

        self.lent_button = ctk.CTkButton(self, corner_radius=0, height=40, border_spacing=10,
                                         text='Lent', fg_color='transparent', text_color=('gray10', 'gray90'),
                                         hover_color=('gray70', 'gray30'), image=self.lent_image, anchor='w',
                                         command=lambda: master.select_frame_by_name(Frame.Lent))
        self.lent_button.grid(row=4, column=0, sticky='ew')

        self.reservation_button = ctk.CTkButton(self, corner_radius=0, height=40, border_spacing=10,
                                                text='Reservation', fg_color='transparent',
                                                text_color=('gray10', 'gray90'), hover_color=('gray70', 'gray30'),
                                                image=self.reservation_image, anchor='w',
                                                command=lambda: master.select_frame_by_name(Frame.Reservation))
        self.reservation_button.grid(row=5, column=0, sticky='ew')

        self.logout_button = ctk.CTkButton(self, corner_radius=0, height=40, border_spacing=10,
                                           text='Logout', font=ctk.CTkFont(size=15, weight='bold'),
                                           image=self.logout_image, anchor='w',
                                           command=lambda: master.select_frame_by_name(Frame.Login))
        self.logout_button.grid(row=6, column=0, sticky='wes', pady=(0, 20))


class OverviewFrame(ctk.CTkFrame):
    def __init__(self, master: App):
        super().__init__(master, fg_color='transparent')
        self.master = master
        self.grid_columnconfigure(0, weight=1)

        self.overview_label = ctk.CTkLabel(self, text='Library overview',
                                           font=ctk.CTkFont(size=25, weight='bold'))
        self.overview_label.grid(row=0, column=0, padx=20, pady=20)


class BooksFrame(ctk.CTkFrame):
    def __init__(self, master: App):
        super().__init__(master, fg_color='transparent')
        self.master = master
        self.grid_columnconfigure(0, weight=1)

        self.books_label = ctk.CTkLabel(self, text='Manage books', font=ctk.CTkFont(size=25, weight='bold'))
        self.books_label.grid(row=0, column=0, padx=20, pady=20)


class ClientsFrame(ctk.CTkFrame):
    def __init__(self, master: App):
        super().__init__(master, fg_color='transparent')
        self.master = master
        self.grid_columnconfigure(0, weight=1)

        self.clients_label = ctk.CTkLabel(self, text='Manage clients',
                                          font=ctk.CTkFont(size=25, weight='bold'))
        self.clients_label.grid(row=0, column=0, padx=20, pady=20)


class LentFrame(ctk.CTkFrame):
    def __init__(self, master: App):
        super().__init__(master, fg_color='transparent')
        self.master = master
        self.grid_columnconfigure(0, weight=1)

        self.lent_label = ctk.CTkLabel(self, text='Lent books', font=ctk.CTkFont(size=25, weight='bold'))
        self.lent_label.grid(row=0, column=0, padx=20, pady=20)


class ReservationFrame(ctk.CTkFrame):
    def __init__(self, master: App):
        super().__init__(master, fg_color='transparent')
        self.master = master
        self.grid_columnconfigure(0, weight=1)

        self.reservation_label = ctk.CTkLabel(self, text='Reserve books',
                                              font=ctk.CTkFont(size=25, weight='bold'))
        self.reservation_label.grid(row=0, column=0, padx=20, pady=20)