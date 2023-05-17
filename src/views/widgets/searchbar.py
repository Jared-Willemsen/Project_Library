from customtkinter import CTkFrame, CTkEntry, CTkButton 


class SearchBar(CTkFrame):
    def __init__(self, parent, height: int, width: int):
        super().__init__(parent, height=height, width=width)

        self.entry = CTkEntry(self, placeholder_text="What are you searching for?", corner_radius=0, height=height, width=int(width*(5/6)), font=('Calibri', height/2))
        self.button = CTkButton(self, text='find', corner_radius=0, height=height, width=int(width*(1/6)), font=('Calibri', height/2))

        self.entry.place(relx=0, anchor='nw')
        self.button.place(relx=1, anchor='ne')
