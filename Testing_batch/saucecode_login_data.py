# give some data to the web , login credentials
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    username = driver.find_element(By.XPATH,"//input[@id='user-name']")
    username.click()
    username.send_keys("standard_user")

    password= driver.find_element(By.XPATH,"//input[@id='password']")
    password.click()
    password.send_keys("secret_sauce")
    login = driver.find_element(By.XPATH,"//input[@id='login-button']")
    login.click()
    print(driver.title)
    time.sleep(5)
    driver.close()