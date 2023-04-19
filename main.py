from karlancer_scraper import KarlancerScraper
from storage import Storage
import pandas as pd
from sqlalchemy import create_engine
from project import Base



# scraper = KarlancerScraper()
# projects = scraper.crawl()

engine = create_engine("sqlite:///projects.db", echo=True)
Base.metadata.create_all(engine)

# storage = Storage()
# storage.store_all(projects)


