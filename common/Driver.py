from selenium import webdriver

class Driver:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)