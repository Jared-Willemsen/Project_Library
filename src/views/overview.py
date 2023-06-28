import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image
import os

from src.models.database import Database
from src.resources.config import IMAGES_DIR


class OverviewView(ctk.CTkFrame):

    def __init__(self, master) -> None:
        super().__init__(master, fg_color='transparent')
        self.grid_columnconfigure(0, weight=1)

        self.header = ctk.CTkLabel(self, text='Library overview',
                                   font=ctk.CTkFont(size=25, weight='bold'))
        self.header.grid(row=0, column=0, padx=20, pady=20)

        # making the big container
        self.container_of_containers = ctk.CTkFrame(self, fg_color='transparent')
        self.container_of_containers.grid(row=1, column=0)
        # making the smaller containers that go in the big container
        self.top_container = ctk.CTkFrame(self.container_of_containers, corner_radius=20, fg_color='white')
        self.top_container.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky='nwe')

        self.bar_container = ctk.CTkFrame(self.container_of_containers, corner_radius=20, fg_color='white')
        self.bar_container.grid(row=2, column=0, padx=20, pady=10, sticky='nw')

        self.line_container = ctk.CTkFrame(self.container_of_containers, corner_radius=20, fg_color='white')
        self.line_container.grid(row=3, column=0, padx=20, pady=10, sticky='nw')

        self.history_frame = ctk.CTkFrame(self.container_of_containers, corner_radius=20, fg_color='white')
        self.history_frame.grid(row=2, column=1, rowspan=2, padx=20, pady=10, sticky='nes')

        # querying to get the data for the analytic function/graphs
        database = Database()
        pie_data = database.execute_query(
            "select genre, count(title) from books GROUP BY genre ORDER BY 2 DESC LIMIT 5;")
        bar_data = database.execute_query(
            "SELECT a.title, COUNT(*) AS borrow_count FROM Books a JOIN Borrowings b ON a.book_id = b.book_id WHERE b.from_date >= DATE_SUB(CURDATE(), INTERVAL 2 YEAR) GROUP BY a.title ORDER BY borrow_count DESC LIMIT 3")
        # SELECT b.title, COUNT(DISTINCT br.borrowed_id) AS borrow_count, SUM(DATEDIFF(IFNULL(b.to_date, CURDATE()), b.from_date)) AS total_borrow_duration, ROUND((SUM(DATEDIFF(IFNULL(b.to_date, CURDATE()), b.from_date)) / DATEDIFF(CURDATE(), '2022-01-01')) * 100, 2) AS borrow_percentage FROM (SELECT MAX(book_id) AS book_id, title FROM Books WHERE from_date >= '2022-01-01' GROUP BY title) AS b JOIN Borrowings AS br ON b.book_id = br.book_id GROUP BY b.title;
        line_data = database.execute_query(
            "SELECT YEAR(from_date) AS year, MONTH(from_date) AS month, count(borrowed_id) as borrow_count from borrowings group by year(from_date), month(from_date) order by year(from_date), month(from_date) LIMIT 12")
        # overdue_data = database.execute_query ("SELECT count(borrowed_id) FROM borrowings WHERE curdate()<due_date")
        overdue_data2 = database.execute_query("select count(*) from overdue_books")
        client_data = database.execute_query("select count(client_id) from clients")
        books_data = database.execute_query("select count(book_id) from books")
        available_books = database.execute_query("select count(*) from available_books")

        # making the line graph
        self.dates = []
        self.books_lent = []
        for row in line_data:
            self.dates.append(F'{row[1]}/{row[0]}')
            self.books_lent.append(row[2])

        line_fig = Figure(figsize=(16, 4), dpi=90)
        ax_dates = line_fig.add_subplot(111)
        ax_dates.plot(self.dates, self.books_lent)
        ax_dates.set_title('Books lent per month', fontsize=19)

        f_canvas3 = FigureCanvasTkAgg(line_fig, master=self.line_container)
        f_canvas3.draw()
        f_canvas3.get_tk_widget().grid(row=0, column=0, padx=20, pady=20)

        # iterate through pie_data and append to lists to make it usable for plt functions
        self.pgenres = []
        self.pbooks = []
        for row in pie_data:
            self.pgenres.append(row[0])
            self.pbooks.append(row[1])

        # making the pie chart
        pie_fig = Figure(figsize=(4, 4), dpi=120)
        ax_pgenres = pie_fig.add_subplot()
        ax_pgenres.pie(self.pbooks, labels=self.pgenres)
        ax_pgenres.set_title('Percentage of books in genres', fontsize=15)

        # making a canvas (container) for the graph and gridding said container
        f_canvas1 = FigureCanvasTkAgg(pie_fig, master=self.top_container)
        f_canvas1.draw()
        f_canvas1.get_tk_widget().grid(row=0, column=5, padx=40, sticky='e')

        empty_label = ctk.CTkLabel(self.top_container, text='')
        empty_label.grid(row=0, column=4, padx=65)

        # making bargraph
        self.titles = []
        self.time_percentages = []

        for row in bar_data:
            self.titles.append(row[0])
            self.time_percentages.append(row[1])

        bargraph_fig = Figure(figsize=(16, 4), dpi=90)
        ax_titles = bargraph_fig.add_subplot(111)

        ax_titles.bar(self.titles, self.time_percentages)
        ax_titles.set_title('Top 3 most popular titles', fontsize=19)

        f_canvas2 = FigureCanvasTkAgg(bargraph_fig, master=self.bar_container)
        f_canvas2.draw()
        f_canvas2.get_tk_widget().grid(row=2, column=3, padx=20, pady=20)

        # making labels/gridding for the history text
        history = 'A long time ago, in the town of Alexandria, Ms. El Abodi and Mr. Brandse founded a quaint library. Alexandria was small, few craved books, and the library held but a handful. Yet, time wove its magic, transforming the town into a metropolis. The library flourished, embraced eager readers, and amassed a bountiful collection.'
        history_text = ctk.CTkLabel(self.history_frame, text=history, wraplength=300, font=ctk.CTkFont(size=15),
                                    fg_color='white')
        history_title = 'The history of Alexandria library'
        history_title_text = ctk.CTkLabel(self.history_frame, text=history_title, wraplength=280,
                                          font=ctk.CTkFont(size=18), fg_color='white')
        history_title_text.grid(row=0, column=0, padx=20, pady=(20, 0), sticky='n')
        history_text.grid(row=1, column=0, padx=20, pady=20, sticky='s')

        self.history_image = ctk.CTkImage(Image.open(os.path.join(IMAGES_DIR, 'libraryicon.png')),
                                          size=(223, 67))
        self.image_label = ctk.CTkLabel(self.history_frame, text='', image=self.history_image)
        self.image_label.grid(row=3, column=0, pady=40)

        # making labels/gridding for the counters
        self.percentage_container = ctk.CTkFrame(self.top_container, corner_radius=20, fg_color='white')
        self.percentage_container.grid(row=0, column=2, padx=40)

        percentage = round((available_books[0][0] / books_data[0][0]) * 100, 2)
        percentage_text = ctk.CTkLabel(self.percentage_container, text='available books', wraplength=100,
                                       fg_color='white', font=ctk.CTkFont(size=14))
        percentage_text.grid(row=0, column=0)
        percentage_counter = ctk.CTkLabel(self.percentage_container, text=f'{percentage}%', fg_color='white',
                                          font=ctk.CTkFont(size=24))
        percentage_counter.grid(row=2, column=0)

        self.overdue_container = ctk.CTkFrame(self.top_container, corner_radius=20, fg_color='white')
        self.overdue_container.grid(row=0, column=1, padx=40)

        overdue_text = ctk.CTkLabel(self.overdue_container, text='overdue books', font=ctk.CTkFont(size=14))
        overdue_text.grid(row=0, column=0)
        overdue_counter = ctk.CTkLabel(self.overdue_container, text=f'{overdue_data2[0][0]}', font=ctk.CTkFont(size=24))
        overdue_counter.grid(row=2, column=0)

        self.client_container = ctk.CTkFrame(self.top_container, corner_radius=20, fg_color='white')
        self.client_container.grid(row=0, column=3, padx=40)

        client_text = ctk.CTkLabel(self.client_container, text='clients', fg_color='white', font=ctk.CTkFont(size=14))
        client_text.grid(row=0, column=0)
        client_counter = ctk.CTkLabel(self.client_container, text=f'{client_data[0][0]}', fg_color='white',
                                      font=ctk.CTkFont(size=24))
        client_counter.grid(row=2, column=0)

        self.books_container = ctk.CTkFrame(self.top_container, corner_radius=20, fg_color='white')
        self.books_container.grid(row=0, column=0, padx=(100, 40))

        books_text = ctk.CTkLabel(self.books_container, text='total books', fg_color='white', font=ctk.CTkFont(size=14))
        books_text.grid(row=0, column=0)
        books_counter = ctk.CTkLabel(self.books_container, text=f'{books_data[0][0]}', fg_color='white',
                                     font=ctk.CTkFont(size=24))
        books_counter.grid(row=2, column=0)
