import pandas as pd
from sqlalchemy import create_engine
from tkinter import *
from karlancer_scraper import KarlancerScraper
from storage import Storage
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from data_presenter import DataPresenter


engine = create_engine("sqlite:///projects.db", echo=True)
# Base.metadata.create_all(engine)



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
    # the figure that will contain the plot
    fig = Figure(figsize = (5, 5), dpi = 100)
    
    # adding the subplot
    plot1 = fig.add_subplot(111)

    # get data from database & draw figure
    storage = Storage()
    projects = storage.read_all(engine)
    dp = DataPresenter()
    data = dp.draw_line_chart(projects, fig)

    # plotting the graph
    plot1.plot(data)

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master = window)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().grid(column=1, row=3)
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   window)
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

