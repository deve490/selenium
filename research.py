from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from login import login
from logout import logout
import os
from dotenv import load_dotenv
from time import sleep
import requests

def research(driver) -> int:
    elem = driver.find_elements(By.XPATH, "//a")
    for el in elem:
        if el.text == "Programar":
            el.click()
            elem = None
            break
            
    sleep(2)
    closecnd = driver.find_elements(By.CLASS_NAME, "bi-x-circle")
    sleep(.5)
    for c in closecnd:
        c.click()

    def is_site_available():
        sleep(10)        
        cards= driver.find_elements(By.CLASS_NAME, "card")
        return len(cards) > 0

    def manage_found_disponibility():
        print("YEAAA WE GOT A SITE")
        try:
            resp = requests.get(os.getenv("API_SUCCESS"))
            if resp.status_code != 200:
                raise Exception({"errors": ["bad_request", resp.content.decode()]})
            print(resp.content.decode())
            with open(os.getenv("PATH_SUCCESS"), "a") as p:
                p.write("CITE AVAILABLE")

        except Exception as e:
            print(e)
            manage_found_disponibility()


    def main_reasearch(state):
        closecnd = driver.find_elements(By.CLASS_NAME, "v-select")
        for c in closecnd:
            if c.get_attribute("data-vv-as") == "Estado":
                c.click()
                li = c.find_elements(By.XPATH, "//li")
                gto = list(filter(lambda l: l.text == state, li))[0]
                gto.click()
                if is_site_available():
                    manage_found_disponibility()
                    return 0
                else:
                    print("By now the site is not available")
                    return 1

        
    main_reasearch(os.getenv("SITE1"))
    main_reasearch(os.getenv("SITE2"))
    sleep(1)
    