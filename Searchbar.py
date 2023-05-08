from customtkinter import CTkFrame, CTkEntry, CTkButton 

class SearchBar():
    def __init__(self, master, height, width):
        self.master = master
        self.height = height
        self.width = width

        self.frame = CTkFrame(master, fg_color='blue', height=self.height, width=self.width)
        self.entry = CTkEntry(self.frame, placeholder_text="What are you searching for?", corner_radius=0, height=self.height, width=self.width*(5/6), font=('calibri', height/2))
        self.button = CTkButton(self.frame, text='find', corner_radius=0, height=self.height, width=self.width*(1/6), font=('calibri', height/2))

        self.frame.place(relx=0.5, rely=0.2, anchor='center')
        self.entry.place(relx=0, anchor='nw')
        self.button.place(relx=1, anchor='ne')