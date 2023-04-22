import pandas as pd
from sqlalchemy import create_engine
from tkinter import *
from karlancer_scraper import KarlancerScraper
from storage import Storage




engine = create_engine("sqlite:///projects.db", echo=True)
# Base.metadata.create_all(engine)

storage = Storage()
projects = storage.read_all(engine)
for p in projects:
    print(p.title)

# ---------------------------- Scrape data & save to db ------------------------------- #
def scrape():
    # scrape
    search_word = "tensorflow"
    scraper = KarlancerScraper(search_word)
    projects = scraper.crawl()
    # save
    storage = Storage()
    storage.store_all(engine ,projects)


# ---------------------------- UI SETUP ------------------------------- #

# window = Tk()
# window.title("Freelancer's buddy")
# window.config(padx=60, pady=60)

# # canvas = Canvas(width=200, height=200)
# # image = PhotoImage(file="logo.png")
# # canvas.create_image(100, 100, image=image)
# # canvas.grid(column=1, row=0)

# # labels
# # label_1 = Label(text="Website: ", font=15)
# # label_1.grid(column=0, row=1)


# # entries
# # entry_site = Entry(width=32)
# # entry_site.focus()
# # entry_site.grid(column=1, row=1)
# # entry_email = Entry(width=51)
# # entry_email.insert(0, string="YourEmailName@email.com")
# # entry_email.grid(column=1, row=2, columnspan=2)
# # entry_pass = Entry(width=32)
# # entry_pass.grid(column=1, row=3)

# # buttons
# button_gen = Button(text="Scrape from karlancer", width=30, command=scrape)
# button_gen.grid(column=1, row=1)
# # button_add = Button(text="Add", width=44, command=save_content)
# # button_add.grid(column=1, row=4, columnspan=2)


# window.mainloop()

