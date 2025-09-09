import time
from selenium import webdriver




def fun_login3(url):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    return driver

def fun_login4(driver):
    time.sleep(5)
    driver.quit()