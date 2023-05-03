import tkinter
from Searchbar import *

client_page = tkinter.Tk()
client_page.attributes('-fullscreen', True)

client_seachbar = SearchBar(client_page, 50, 1200)

client_page.mainloop()