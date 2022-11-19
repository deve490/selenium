from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


from time import sleep
def login(driver, email, password):
    sleep(1)
    elem = driver.find_elements(By.XPATH, "//button")
    for el in elem:
        if el.text == "Territorio Nacional":
            el.click()
            elem = None
            break

    sleep(2)
    elem = driver.find_elements(By.XPATH, "//button")
    for el in elem:
        if el.text == "Continuar":
            el.click()
            elem = None
            break

    elem = driver.find_elements(By.XPATH, "//button")
    for el in elem:
        if el.text == "Continuar":
            el.click()
            elem = None
            break

    elem = driver.find_elements(By.XPATH, "//input")

    for el in elem:
        if el.get_property("name")== "email":
            el.send_keys(email)
        elif el.get_property("name") == "password":
            el.send_keys(password)

    condi = driver.find_elements(By.XPATH, "//a")

    for c in condi:
        if "".join(c.text.split(" ")) == "términosycondiciones":
            c.click()
            break

    closecnd = driver.find_elements(By.CLASS_NAME, "bi-x-circle")
    sleep(.5)
    for c in closecnd:
        c.click()

    sleep(2)

    elem = driver.find_elements(By.CLASS_NAME,  "pull-right")
    elem[0].click()

    sleep(2)
    closecnd = driver.find_elements(By.CLASS_NAME, "bi-x-circle")
    sleep(.5)
    for c in closecnd:
        c.click()
    print("Success login")
    