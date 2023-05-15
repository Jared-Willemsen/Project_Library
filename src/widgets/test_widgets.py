import customtkinter as ctk
from src.widgets.custom_table import CustomTable
from src.widgets.searchbar import SearchBar

root = ctk.CTk()
ctk.set_appearance_mode('dark')

# Create searchbar
searchbar = SearchBar(root, 30, 400)
searchbar.pack(pady=20, anchor='w')

# Create table
treeview_frame = CustomTable(root, headings=["id", "title", "author", "genre", "language"],
                             column_widths=[60, 400, 300, 300, 300])
treeview_frame.pack()

# Insert data into table
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "t_Vo(+ra]=",
    "database": "library"
}
treeview_frame.insert_from_mysql(db_config, "books")

root.mainloop()
