# login with invalid data
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

def test_invalid_data():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    username = driver.find_element(By.XPATH, "//input[@id='user-name']")
    username.click()
    username.send_keys("standard_user")

    password = driver.find_element(By.XPATH, "//input[@id='password']")
    password.click()
    password.send_keys("1234")
    login = driver.find_element(By.XPATH, "//input[@id='login-button']")
    login.click()
    print(driver.title)
    time.sleep(5)
    driver.close()