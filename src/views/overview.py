import customtkinter as ctk
from src.models.database import Database
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class OverviewView(ctk.CTkFrame):

    def __init__(self, master) -> None:
        super().__init__(master, fg_color='transparent')
        self.grid_columnconfigure(0, weight=1)

        self.header = ctk.CTkLabel(self, text='Library overview',
                                   font=ctk.CTkFont(size=25, weight='bold'))
        self.header.grid(row=0, column=0, padx=20, pady=20)

        self.container = ctk.CTkFrame(self, corner_radius=20)
        self.container.grid(row=1, column=0)

        database = Database()
        pie_data = database.execute_query("select genre, count(title) from books GROUP BY genre LIMIT 5;")
        bar_data = database.execute_query("select a.title, count(b.borrowed_id) from books a INNER JOIN borrowings b on a.book_id = b.borrowed_id GROUP BY a.title;")
        
        # iterate through pie_data and append to lists to make it usable for plt functions
        self.pgenres = []
        self.pbooks = []
        for row in pie_data:
            self.pgenres.append(row[0])
            self.pbooks.append(row[1])

        pie_fig = Figure (figsize=(4,4), dpi = 100)
        ax_pgenres = pie_fig.add_subplot ()
        ax_pgenres.pie (self.pbooks, labels=self.pgenres)
        # making it a circle
        plt.axis ('equal')  
        f_canvas = FigureCanvasTkAgg (pie_fig, master=self.container)
        f_canvas.draw ()
        f_canvas.get_tk_widget().grid(row=2,column=1, padx=20, pady=20)




        self.genres = []
        self.num_books = []

        for row in bar_data:
            self.genres.append (row[0])
            self.num_books.append (row[1])
        print (self.num_books)

        bargraph_fig = Figure(figsize=(15,4), dpi=100)
        ax_genres = bargraph_fig.add_subplot(111)

        ax_genres.bar (self.genres, self.num_books)

        f_canvas = FigureCanvasTkAgg (bargraph_fig, master=self.container)
        f_canvas.draw ()
        f_canvas.get_tk_widget().grid(row=2,column=3, padx=20, pady=20)

        history_frame = ctk.CTkFrame(self)
        history_frame.grid (row=2, column=0, padx=20, pady=20, sticky='w')
        history = 'Long ago, in the town of Alexandria, Ms. El Abodi and Mr. Brandse birthed a library. Alexandria was small, few craved books, and the library held but a handful.Yet, time wove its magic, transforming the town into a metropolis. The library flourished, embraced eager readers, and amassed a bountiful collection.'
        history_text = ctk.CTkLabel (history_frame, text=history, wraplength=300)
        history_text.pack(padx=20, pady=20)











        
