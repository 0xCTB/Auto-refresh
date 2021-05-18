import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def login(driver):
    try:
        email_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='id_username']")))
        email_element.clear()
        email_element.send_keys("INSERT YOUR EMAIL HERE", Keys.ARROW_DOWN)
        time.sleep(1)
        password_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='loginForm']/div[2]/div/div/input")))
        password_element.clear()
        password_element.send_keys("INSERT YOUR PASSWORD HERE", Keys.ARROW_DOWN)
        time.sleep(1)
        driver.find_element_by_id("login").click()
    except TimeoutException as e:
        print(f"Something went wrong while logging in, try again. Error: {e}")

def login_handler(driver, url):
    driver.get(url)
    login(driver)

if __name__ == "__main__":
    login_handler()
