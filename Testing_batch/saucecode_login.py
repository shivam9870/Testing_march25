from selenium import webdriver


def test_saucecode_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    print(driver.title)
    driver.quit()