from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


from time import sleep
def logout(driver):

    closecnd = driver.find_elements(By.CLASS_NAME, "bi-x-circle")
    sleep(.5)
    for c in closecnd:
        c.click()

    togle = driver.find_element(By.CLASS_NAME, "dropdown-toggle")
    togle.click()

    close_ss = driver.find_elements(By.XPATH, "//a")
    for c  in close_ss:
        if c.text == "Cerrar sesión":
            c.click()

    btn = driver.find_elements(By.CLASS_NAME, "btn-primary")

    for bt in btn:
        bt.click()
        btn = None
        bt=None
        break
    
    print("Success session closed")
    
