from karlancer_scraper import KarlancerScraper
from storage import Storage
import pandas as pd
from sqlalchemy import create_engine
from project import Base
from tkinter import *




engine = create_engine("sqlite:///projects.db", echo=True)
# Base.metadata.create_all(engine)

# ---------------------------- Scrape data & save to db ------------------------------- #
def scrape():
    # scrape
    scraper = KarlancerScraper()
    projects = scraper.crawl()
    # save
    storage = Storage()
    storage.store_all(engine ,projects)


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
# label_2 = Label(text="Email/Username: ", font=15)
# label_2.grid(column=0, row=2)
# label_3 = Label(text="Password: ", font=15)
# label_3.grid(column=0, row=3)

# entries
# entry_site = Entry(width=32)
# entry_site.focus()
# entry_site.grid(column=1, row=1)
# entry_email = Entry(width=51)
# entry_email.insert(0, string="YourEmailName@email.com")
# entry_email.grid(column=1, row=2, columnspan=2)
# entry_pass = Entry(width=32)
# entry_pass.grid(column=1, row=3)

# buttons
button_gen = Button(text="Scrape", width=30, command=scrape)
button_gen.grid(column=1, row=1)
# button_add = Button(text="Add", width=44, command=save_content)
# button_add.grid(column=1, row=4, columnspan=2)
# button_gen = Button(text="Search", command=search, width=14)
# button_gen.grid(column=2, row=1)

window.mainloop()

