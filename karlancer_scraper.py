import time
import selenium.common
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from unidecode import unidecode
import pandas as pd
from scipy import stats

class KarlancerScraper :
    def __init__(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        # service = Service(executable_path="E:\Python projects\Chrome webriver\chromedriver.exe")
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        search_word = "tensorflow"
        url = f"https://www.karlancer.com/search?q={search_word}"
        self.driver.get(url=url)
        self.page_counter = 1                                                                            

    def crawl(self):
        reload_reference_xpath = '//*[@id="parentContent"]/app-project/div/app-search-card/div[7]/div[3]/div[1]/div[1]/app-project-card/div/div/div[1]/div[1]/div[1]/span/a/h4'
        while True:
            self.get_projects_info() 
            self.page_counter += 1
            reload_ref = self.driver.find_element(By.XPATH, reload_reference_xpath)

            # check if there is another page
            if len(self.driver.find_elements(By.ID, 'navigatePage_next')) == 0:
                break
            # go to next page
            next_button = self.self.driver.find_element(By.ID, 'navigatePage_next')
            webdriver.ActionChains(self.driver).move_to_element(next_button).click(next_button).perform()
            # driver.execute_script("arguments[0].click();", next_button) # another way to click
            
            # check if next page is fully loaded
            new_reload_ref = self.driver.find_element(By.XPATH, reload_reference_xpath)
            while reload_ref == new_reload_ref:
                time.sleep(0.1)
                print("waiting")
                new_reload_ref = self.driver.find_element(By.XPATH, reload_reference_xpath)

    def get_projects_info(self):
        table_xpath = '//*[@id="parentContent"]/app-project/div/app-search-card/div[7]/div[3]'
        table = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, table_xpath)))
        containers = table.find_elements(By.CSS_SELECTOR, 'div.border-1-transparent')
        print(f"\npage: {self.page_counter}")
        for container in containers:
            title_obj = container.find_element(By.CSS_SELECTOR, 'h4.font-weight-bold')
            to_search_obj = container
            price_obj = container.find_element(By.CSS_SELECTOR, 'div.align-items-center div')
            deadline_obj = container.find_element(By.CSS_SELECTOR, 'div.mt-3 div')
            print(title_obj.text)
            
            
