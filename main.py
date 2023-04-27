import pandas as pd
from sqlalchemy import create_engine
from tkinter import *
from tkinter import ttk
from karlancer_scraper import KarlancerScraper
from storage import Storage
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from data_presenter import DataPresenter
import matplotlib.pyplot as plt


engine = create_engine("sqlite:///projects.db", echo=True)
# Base.metadata.create_all(engine) # create the tables

# ---------------------------- Scrape data & save to db ------------------------------- #
def scrape(search_word):
    # scrape
    scraper = KarlancerScraper(search_word)
    projects = scraper.crawl()
    # save
    storage = Storage()
    storage.store_all(engine ,projects)

# ---------------------------- Draw the figure ------------------------------- #
def plot():
    # get data from database & draw figure
    storage = Storage()
    projects = storage.read_all(engine)
    dp = DataPresenter()
    data = dp.generate_axis_data(projects)

    # plotting the graph
    fig = plt.figure(figsize=(8,6))
    plt.xticks(fontsize=14, rotation=50)
    plt.yticks(fontsize=14)
    plt.xlabel('Tag', fontsize=14)
    plt.ylabel('Number of projects', fontsize=14)
    # ax = plt.axes()
    # ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
    # ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
    fig.tight_layout()
    plt.plot(data[0], data[1])

    # creating the Tkinter canvas containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master = second_frame)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().grid(column=1, row=3)
  
    # creating the Matplotlib toolbar
    # toolbar = NavigationToolbar2Tk(canvas,window)
    # added a frame so I can grid it, it also shows the toolbar, can get rid of it by removing grid
    toolbarFrame = Frame(master=second_frame)
    toolbarFrame.grid(column=1,row=5)
    toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().grid(column=1, row=4)


# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.title("Freelancer's buddy")
root.config(padx=20, pady=20)
root.geometry("700x500")

# canvas = Canvas(width=200, height=200)
# image = PhotoImage(file="logo.png")
# canvas.create_image(100, 100, image=image)
# canvas.grid(column=1, row=0)

# Create A Main Frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# Create A Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add A Scrollbar To The Canvas
my_scrollbar_y = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar_y.pack(side=RIGHT, fill=Y)

# Configure The Canvas
my_canvas.configure(yscrollcommand=my_scrollbar_y.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

# Create ANOTHER Frame INSIDE the Canvas
second_frame = Frame(my_canvas)

# Add that New frame To a Window In The Canvas
my_canvas.create_window((0,0), window=second_frame, anchor="nw")

# labels
label_1 = Label(second_frame, text="Keyword: ", font=15)
label_1.grid(column=0, row=1)


# entries
entry_keyword = Entry(second_frame, width=30)
entry_keyword.grid(column=1, row=1)
# entry_site.focus()
# entry_email = Entry(width=51)
# entry_email.insert(0, string="YourEmailName@email.com")
# entry_email.grid(column=1, row=2, columnspan=2)


# buttons
button_gen = Button(second_frame, text="Scrape from karlancer", width=30, command= lambda: scrape(entry_keyword.get()))
button_gen.grid(column=2, row=1, padx=20, pady=20)
button_add = Button(second_frame, text="Chart", width=30, command=plot)
button_add.grid(column=1, row=2)


root.mainloop()

