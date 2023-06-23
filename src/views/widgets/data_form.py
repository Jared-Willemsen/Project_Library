import customtkinter as ctk
import tkinter as ttk

class DataForm(ctk.CTkFrame):
    def __init__(self, parent, form_headings, entry_values):
        super().__init__(parent)
        self.entry_values = entry_values
        self.entries = [] 

        self.header = ctk.CTkLabel(self, font=ctk.CTkFont(size=20, weight='bold'))
        self.header.grid(row=0, column=0, columnspan=6, pady=10) 

        for i, heading in enumerate(form_headings):
            label = ctk.CTkLabel(self, text=heading)
            entry = ctk.CTkEntry(self)
            self.entries.append(entry)
            label.grid(row=i+1, column=0, columnspan=3, padx=20, pady=10)
            entry.grid(row=i+1, column=3, columnspan=3,padx=20, pady=10)       
            entry.insert(0, entry_values[i])     
        
        self.confirm_button = ctk.CTkButton(self, text='confirm', width=20)
        self.reset_button = ctk.CTkButton(self, text='reset', width=20, command=self.reset_entries)
        self.cancel_button = ctk.CTkButton(self, text='cancel', width=20)
        self.confirm_button.grid(row=len(form_headings)+2, column=5, pady=10)
        self.reset_button.grid(row=len(form_headings)+2, column=0, pady=10, padx=20)
        self.cancel_button.grid(row=len(form_headings)+2, column=4, pady=10)

        self.place(relx=0.5, rely=0.5, anchor='center')
    
    def reset_entries(self):
        for i, entry in enumerate(self.entries):
            entry.delete(0, ctk.END)
            entry.insert(0, self.entry_values[i])
    
    def empty_entries(self):
        for entry in self.entries:
            entry.delete(0, ctk.END)
    
    def fill_entries(self, values):
        for i, entry in enumerate(self.entries):
            entry.insert(0, values[i])

    def get_data_from_entries(self):
        data_input = []
        for entry in self.entries:
            data_input.append(entry.get())
        return data_input
