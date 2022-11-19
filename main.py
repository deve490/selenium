import sys
from datetime import datetime
import os
from dotenv import load_dotenv

d = datetime.now()
try:
    import requests
    path = os.getenv("PATH_SUCCESS")
    with open(path , "r") as p:
        r =p.readline()
        print(r)
        print("If yet you dont get an appoiment please remove success.txt file")
        requests.get(os.getenv("API_SUCCESS"))
        sys.exit(0)
except Exception as e:
    pass

print("\n##########################################################\n")
print("Loading dependences")


from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from login import login
from logout import logout
from time import sleep
from research import research


print("dependences loaded")
service = Service(os.getenv("PATH_DRIVER"))
options = Options()
# options.binary_location = '/opt/headless-chromium'
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--single-process')
options.add_argument('--disable-dev-shm-usage')
load_dotenv()
print("Configuration done")

def loggError(e):
    with open(os.getenv("PATH_ERRORS"), "a") as p:
        p.write("\n############################################n")
        p.write(str(e))
        p.write(f"\nAt {d.hour}:{d.minute}")
        p.write("\n·········································\n")



def automatation() -> bool:
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), 
        chrome_options=options
        )
    driver.get(os.getenv("WEB_SITE"))
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    try: login(driver, email, password)
    except Exception as e:
        print("Login Error")
        loggError(e)
        driver.quit()
        return False

    try: 
        research(driver)
    except Exception as e:
        print("Searching ERROR")
        loggError(e)
        try:
            logout(driver)
        except Exception as e:
            pass
        driver.quit()
        return False

    try:
        logout(driver)
        driver.quit()
        return True
    except Exception as e:
        loggError(e)
        print("Logout error")
        sleep(20)
        driver.quit() 
        return False
    
    


if __name__ == "__main__":
    print("Initializing automatiotion")
    correct = False
    intent = 1
    while (not correct) and intent < 4:
        correct = automatation()
        intent+=1
    print("End of automation")        

print(f"Executed at {d.hour}: {d.minute}")