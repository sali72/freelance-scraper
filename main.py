from karlancer_scraper import KarlancerScraper

scraper = KarlancerScraper()
projects = scraper.crawl()
for project in projects:
    print(project.title)