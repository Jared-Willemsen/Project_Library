import customtkinter as ctk
import tkinter as ttk

class ComfirmationFrame(ctk.CTkFrame):
    def __init__(self, parent, headers):
        super().__init__(parent)
        self.labels = [] 

        self.header = ctk.CTkLabel(self, font=ctk.CTkFont(size=20, weight='bold'))
        self.header.grid(row=0, column=0, columnspan=6, pady=10) 

        for i, heading in enumerate(headers):
            column_label = ctk.CTkLabel(self, text=heading)
            value_label = ctk.CTkLabel(self)
            self.labels.append(value_label)
            column_label.grid(row=i+1, column=0, columnspan=3, padx=20, pady=10)
            value_label.grid(row=i+1, column=3, columnspan=3,padx=20, pady=10)       
        
        self.confirm_button = ctk.CTkButton(self, text='confirm', width=20)
        self.cancel_button = ctk.CTkButton(self, text='cancel', width=20)
        self.confirm_button.grid(row=len(headers)+2, column=5, pady=10)
        self.cancel_button.grid(row=len(headers)+2, column=1, pady=10)

        self.place(relx=0.5, rely=0.5, anchor='center')
    
    def change_labels(self, values):
        for i, label in enumerate(self.labels):
            label.configure(text=values[i])
    
