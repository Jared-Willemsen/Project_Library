import customtkinter as ctk
import tkinter as ttk

class DataForm(ctk.CTkFrame):
    def __init__(self, parent, form_headings, entry_values):
        super().__init__(parent)
        self.entry_values = entry_values
        self.entries = [] 

        title = ctk.CTkLabel(self, text='Form', font=ctk.CTkFont(size=20, weight='bold'))
        title.grid(row=0, column=0, columnspan=6, pady=10) 

        for i, heading in enumerate(form_headings):
            label = ctk.CTkLabel(self, text=heading)
            entry = ctk.CTkEntry(self)
            self.entries.append(entry)
            label.grid(row=i+1, column=0, columnspan=3, padx=20, pady=10)
            entry.grid(row=i+1, column=3, columnspan=3,padx=20, pady=10)       
            entry.insert(0, entry_values[i])     
        
        accept_button = ctk.CTkButton(self, text='accept', width=20)
        reset_button = ctk.CTkButton(self, text='reset', width=20, command=self.reset_entries)
        cancel_button = ctk.CTkButton(self, text='cancel', width=20)
        accept_button.grid(row=len(form_headings)+2, column=5, pady=10)
        reset_button.grid(row=len(form_headings)+2, column=0, pady=10, padx=20)
        cancel_button.grid(row=len(form_headings)+2, column=4, pady=10)

        self.place(relx=0.5, rely=0.5, anchor='center')

    def reset_entries(self):
        for i, entry in enumerate(self.entries):
            entry.delete(0, ctk.END)
            entry.insert(0, self.entry_values[i])

mainwindow = ttk.Tk()
form = DataForm(mainwindow, ['1', '2', '3', '4'], ['1', '2', '3', '4'])
mainwindow.mainloop()

