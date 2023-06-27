import customtkinter as ctk
import tkinter.ttk as ttk


class CustomTable(ctk.CTkFrame):
    def __init__(self, parent, column_names: list[str], column_widths: list[int], height: int = 20):
        super().__init__(parent)

        # Create Treeview widget for the table
        self.treeview = ttk.Treeview(self, columns=column_names, height=height, selectmode="browse")
        self.scrollbar = ctk.CTkScrollbar(self, width=20, command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=self.scrollbar.set)
        self.treeview.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        # Configure column properties
        self.treeview.column("#0", width=0, stretch=False)
        for i, heading in enumerate(column_names):
            width = column_widths[i] if column_widths else None
            if i == 0:
                self.treeview.heading(heading, text=heading.title(), anchor='w', command=lambda _col=heading: self.treeview_sort_column(_col, False))
                self.treeview.column(heading, minwidth=width, width=width, anchor='w', stretch='YES')
            else:
                self.treeview.heading(heading, text=heading.title(), anchor='center', command=lambda _col=heading: self.treeview_sort_column(_col, False))
                self.treeview.column(heading, minwidth=width, width=width, anchor='center', stretch='YES')

        # Configure grid weights
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Apply custom ttk styles
        self.set_ttk_styles()

    def insert(self, parent, index, values):
        self.treeview.insert(parent, index, values=values)

    def delete(self, item):
        self.treeview.delete(item)

    def get_children(self, item):
        return self.treeview.get_children(item)

    def get_selection(self):
        selected_item = self.treeview.focus()
        if selected_item == '':
            return 'no selection'
        return self.treeview.item(selected_item)

    def insert_rows(self, rows):
        for row in rows:
            self.insert("", 0, values=row)

    def clear_rows(self):
        for row in self.treeview.get_children():
            self.treeview.delete(row)

    def treeview_sort_column(self, col, reverse):
        # sort column data
        try:
            data_list = [
                (int(self.treeview.set(k, col)), k) for k in self.treeview.get_children("")
            ]
        except Exception:
            data_list = [(self.treeview.set(k, col), k) for k in self.treeview.get_children("")]

        data_list.sort(reverse=reverse)

        # rearrange items in sorted positions
        for index, (val, k) in enumerate(data_list):
            self.treeview.move(k, "", index)

        # reverse sort next time
        self.treeview.heading(column=col, command=lambda _col=col: self.treeview_sort_column(_col, not reverse))

    @staticmethod
    def set_ttk_styles():
        """Set custom ttk styles based on appearance mode."""
        style = ttk.Style()
        style.theme_use("default")

        appearance_mode = ctk.get_appearance_mode()
        if appearance_mode == 'Light':
            style.configure("Treeview",
                            background="white",
                            foreground="black",
                            rowheight=45,
                            fieldbackground="#343638",
                            bordercolor="#343638",
                            borderwidth=0,
                            font=('Helvetica', 19))
            style.map('Treeview', background=[('selected', '#22559b')])
            style.configure("Treeview.Heading",
                            background="#bfbfbf",
                            foreground="black",
                            padding=10,
                            relief="flat",
                            font=('Helvetica', 20, 'bold'))
            style.map("Treeview.Heading", background=[('active', '#3484F0')])
        elif appearance_mode == 'Dark':
            style.configure("Treeview",
                            background="#2a2d2e",
                            foreground="white",
                            rowheight=45,
                            fieldbackground="#343638",
                            bordercolor="#343638",
                            borderwidth=0,
                            font=('Helvetica', 19))
            style.map('Treeview', background=[('selected', '#22559b')])
            style.configure("Treeview.Heading",
                            background="#565b5e",
                            foreground="white",
                            padding=10,
                            relief="flat",
                            font=('Helvetica', 20, 'bold'))
            style.map("Treeview.Heading", background=[('active', '#3484F0')])
