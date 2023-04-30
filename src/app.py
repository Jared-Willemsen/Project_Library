import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import os
from PIL import Image
from src.enums.frames import Frame


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Library Manager")

        self.minsize(1280, 700)
        self.after(0, lambda: self.state('zoomed'))  # BUGFIX - Do not delete

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets')
        self.logo_image = ctk.CTkImage(Image.open(os.path.join(image_path, "customtkinter_logo_single.png")),
                                       size=(26, 26))
        self.home_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")), size=(20, 20))
        self.chat_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")), size=(20, 20))
        self.add_user_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                           size=(20, 20))

    def run(self):
        self._create_gui()
        self.mainloop()

    def _create_gui(self):
        # create login menu
        self.login_form = ctk.CTkFrame(self, corner_radius=10, fg_color="#707070")
        self.login_form.grid(row=0, column=0, rowspan=2, columnspan=2)
        self.login_form.grid_rowconfigure(1, weight=1)
        self.login_form.grid_columnconfigure(1, weight=1)

        self.login_label = ctk.CTkLabel(self.login_form, text="Log into your Account", text_color='#ffffff',
                                        font=('Arial', 35, 'bold'))
        self.login_label.grid(row=0, column=1, padx=20, pady=25, columnspan=2)

        self.username_entry = ctk.CTkEntry(self.login_form, width=300, placeholder_text="Username", font=('Arial', 15))
        self.username_entry.grid(row=1, column=1, padx=20, pady=15)

        self.show_password = ctk.BooleanVar()
        self.password_entry = ctk.CTkEntry(self.login_form, width=300, placeholder_text="Password", show='•',
                                           font=('Arial', 15))
        self.password_entry.grid(row=2, column=1, padx=20, pady=15)

        self.toggle_password = ctk.CTkCheckBox(self.login_form, text="Show", text_color='#ffffff',
                                               variable=self.show_password, command=self.toggle_password_visibility)
        self.toggle_password.grid(row=2, column=2)

        self.forgot_password = ctk.CTkLabel(self.login_form, text="Forgot password?", text_color='#A9A9A9',
                                            font=('Arial', 15, 'underline'), anchor='w', cursor='hand2')
        self.forgot_password.grid(row=3, column=1, padx=20, pady=10, columnspan=2, sticky='w')

        self.login_button = ctk.CTkButton(self.login_form, height=40, border_spacing=10, text="Login",
                                          text_color="#ffffff", font=('Arial', 20, 'bold'),
                                          hover_color=("gray70", "gray30"),
                                          anchor="n", command=self.login_button_event)
        self.login_button.grid(row=4, column=1, columnspan=2, pady=20)

        # create navigation sidebar
        self.navigation_sidebar = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_sidebar.grid(row=0, column=0, sticky="nsew")
        self.navigation_sidebar.grid_rowconfigure(6, weight=1)  # NOTE: change it when adding more buttons

        self.navigation_sidebar_label = ctk.CTkLabel(self.navigation_sidebar, text="  Library Manager",
                                                     image=self.logo_image,
                                                     compound="left", font=ctk.CTkFont(size=15, weight="bold"))
        self.navigation_sidebar_label.grid(row=0, column=0, padx=20, pady=20)

        self.overview_button = ctk.CTkButton(self.navigation_sidebar, corner_radius=0, height=40, border_spacing=10,
                                             text="Overview",
                                             fg_color="transparent", text_color=("gray10", "gray90"),
                                             hover_color=("gray70", "gray30"),
                                             image=self.home_image, anchor="w",
                                             command=lambda: self.select_frame_by_name(Frame.Overview))
        self.overview_button.grid(row=1, column=0, sticky="ew")

        self.books_button = ctk.CTkButton(self.navigation_sidebar, corner_radius=0, height=40, border_spacing=10,
                                          text="Books",
                                          fg_color="transparent", text_color=("gray10", "gray90"),
                                          hover_color=("gray70", "gray30"),
                                          image=self.chat_image, anchor="w",
                                          command=lambda: self.select_frame_by_name(Frame.Books))
        self.books_button.grid(row=2, column=0, sticky="ew")

        self.clients_button = ctk.CTkButton(self.navigation_sidebar, corner_radius=0, height=40, border_spacing=10,
                                            text="Clients",
                                            fg_color="transparent", text_color=("gray10", "gray90"),
                                            hover_color=("gray70", "gray30"),
                                            image=self.add_user_image, anchor="w",
                                            command=lambda: self.select_frame_by_name(Frame.Clients))
        self.clients_button.grid(row=3, column=0, sticky="ew")

        self.lent_button = ctk.CTkButton(self.navigation_sidebar, corner_radius=0, height=40, border_spacing=10,
                                         text="Lent",
                                         fg_color="transparent", text_color=("gray10", "gray90"),
                                         hover_color=("gray70", "gray30"),
                                         image=self.chat_image, anchor="w",
                                         command=lambda: self.select_frame_by_name(Frame.Lent))
        self.lent_button.grid(row=4, column=0, sticky="ew")

        self.reservation_button = ctk.CTkButton(self.navigation_sidebar, corner_radius=0, height=40, border_spacing=10,
                                                text="Reservation",
                                                fg_color="transparent", text_color=("gray10", "gray90"),
                                                hover_color=("gray70", "gray30"),
                                                image=self.add_user_image, anchor="w",
                                                command=lambda: self.select_frame_by_name(Frame.Reservation))
        self.reservation_button.grid(row=5, column=0, sticky="ew")

        # create first frame
        self.overview_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.overview_frame.grid_columnconfigure(0, weight=1)

        self.overview_label = ctk.CTkLabel(self.overview_frame, text="Library overview", font=('Arial', 20))
        self.overview_label.grid(row=0, column=0, padx=20, pady=10)

        # create second frame
        self.books_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.books_frame.grid_columnconfigure(0, weight=1)

        self.books_label = ctk.CTkLabel(self.books_frame, text="Manage books", font=('Arial', 20))
        self.books_label.grid(row=0, column=0, padx=20, pady=10)

        # create third frame
        self.clients_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.clients_frame.grid_columnconfigure(0, weight=1)

        self.clients_label = ctk.CTkLabel(self.clients_frame, text="Manage clients", font=('Arial', 20))
        self.clients_label.grid(row=0, column=0, padx=20, pady=10)

        # create fourth frame
        self.lent_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.lent_frame.grid_columnconfigure(0, weight=1)

        self.lent_label = ctk.CTkLabel(self.lent_frame, text="Lent books", font=('Arial', 20))
        self.lent_label.grid(row=0, column=0, padx=20, pady=10)

        # create fifth frame
        self.reservation_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.reservation_frame.grid_columnconfigure(0, weight=1)

        self.reservation_label = ctk.CTkLabel(self.reservation_frame, text="Reserve books", font=('Arial', 20))
        self.reservation_label.grid(row=0, column=0, padx=20, pady=10)

        # select default frame
        self.select_frame_by_name(Frame.Login)
        # NOTE: change Frame.Login to Frame.Overview for testing purposes

    def login_button_event(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.password_entry.delete(0, ctk.END)  # clear the password

        # perform login validation
        if username == "admin" and password == "1234":
            self.select_frame_by_name(Frame.Overview)
        elif username == '' or password == '':
            CTkMessagebox(title="Required fields", message="Please include all fields")
        else:
            CTkMessagebox(title="Unable to login", message="Invalid username or password")
        # TODO: This should be replaced with proper database validation in the future.
        # TODO: Secure from SQL injection

    def toggle_password_visibility(self):
        if self.show_password.get():
            self.toggle_password.configure(text="Hide")
            self.password_entry.configure(show="")
        else:
            self.toggle_password.configure(text="Show")
            self.password_entry.configure(show="•")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.overview_button.configure(fg_color=("gray75", "gray25") if name == "overview" else "transparent")
        self.books_button.configure(fg_color=("gray75", "gray25") if name == "books" else "transparent")
        self.clients_button.configure(fg_color=("gray75", "gray25") if name == "clients" else "transparent")
        self.lent_button.configure(fg_color=("gray75", "gray25") if name == "lent" else "transparent")
        self.reservation_button.configure(fg_color=("gray75", "gray25") if name == "reservation" else "transparent")

        # show selected frame
        if name == Frame.Login:
            self.login_form.grid(row=0, column=0, rowspan=2, columnspan=2)
            self.navigation_sidebar.grid_forget()
        else:
            self.navigation_sidebar.grid(row=0, column=0, sticky="nsew")
            self.login_form.grid_forget()
        if name == Frame.Overview:
            self.overview_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.overview_frame.grid_forget()
        if name == Frame.Books:
            self.books_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.books_frame.grid_forget()
        if name == Frame.Clients:
            self.clients_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.clients_frame.grid_forget()
        if name == Frame.Lent:
            self.lent_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.lent_frame.grid_forget()
        if name == Frame.Reservation:
            self.reservation_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.reservation_frame.grid_forget()
