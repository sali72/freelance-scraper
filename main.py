import pandas as pd
from sqlalchemy import create_engine
from tkinter import *
from karlancer_scraper import KarlancerScraper
from storage import Storage
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from data_presenter import DataPresenter
import matplotlib.pyplot as plt


engine = create_engine("sqlite:///projects.db", echo=True)
# Base.metadata.create_all(engine) # create the tables

# storage = Storage()
# projects = storage.read_all(engine)
# dp = DataPresenter()
# df = dp.scalars_to_df(projects)
# print(df)


# ---------------------------- Scrape data & save to db ------------------------------- #
def scrape():
    # scrape
    search_word = "tensorflow"
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
    plt.xticks(fontsize=14,rotation=50)
    plt.yticks(fontsize=14)
    plt.xlabel('Tag', fontsize=14)
    plt.ylabel('Number of projects', fontsize=14)

    plt.plot(data[0], data[1])

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master = window)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().grid(column=1, row=3)
  
    # creating the Matplotlib toolbar
    # toolbar = NavigationToolbar2Tk(canvas,window)
    # added a frame so I can grid it, it also shows the toolbar, can get rid of it by removing grid
    toolbarFrame = Frame(master=window)
    toolbarFrame.grid(column=1,row=5)
    toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().grid(column=1, row=4)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Freelancer's buddy")
window.config(padx=60, pady=60)

# canvas = Canvas(width=200, height=200)
# image = PhotoImage(file="logo.png")
# canvas.create_image(100, 100, image=image)
# canvas.grid(column=1, row=0)

# labels
# label_1 = Label(text="Website: ", font=15)
# label_1.grid(column=0, row=1)


# entries
# entry_site = Entry(width=32)
# entry_site.focus()
# entry_site.grid(column=1, row=1)
# entry_email = Entry(width=51)
# entry_email.insert(0, string="YourEmailName@email.com")
# entry_email.grid(column=1, row=2, columnspan=2)


# buttons
button_gen = Button(text="Scrape from karlancer", width=30, command=scrape)
button_gen.grid(column=1, row=1)
button_add = Button(text="Plot", width=30, command=plot)
button_add.grid(column=1, row=2)


window.mainloop()

