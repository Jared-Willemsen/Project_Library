from tkinter import *

login_window = Tk()

login_window.title ('Lazy Librarians')
# making the login_window full screened
## 1. function that retrieve size of the current window and so also the screen size of the laptop
width= login_window.winfo_screenwidth()               
height= login_window.winfo_screenheight()  

## 2. geometry sets the window size to the previously acquired information
login_window.geometry("%dx%d" % (width, height))

# log_in_window.attributes ('-fullscreen', True)

# creating the username bar
username = (login_window, text="Username")

login_window.mainloop()
