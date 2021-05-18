import time
import datetime
import os
from login import login_handler
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

path = os.path.join(os.getcwd(), "chromedriver_win32\\chromedriver.exe")

driver = webdriver.Chrome(executable_path=path)

url = "INSERT YOUR URL HERE"

check_attempt_counter = 1

def get_time_stamp():
    time_stamp = datetime.datetime.now()
    formatted_time_stamp = time_stamp.strftime("%H:%M:%S")
    return formatted_time_stamp

def check_availability():
    full = True
    while full:
        try:
            time_stamp = get_time_stamp()
            slots = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.with-hint.push")))
            slots_text = slots.text.strip()
            available_slots  = False if slots_text.find("0") != -1 else True
            if not available_slots:
                print(f'{time_stamp} - Study is full. There\'s {slots_text[0]} slots available.')
                time.sleep(1)
                driver.refresh()
            else:
                print(f'{time_stamp} - Study is available. There\'s {slots_text[0]} slots available.')
                break
        except TimeoutException:
            global check_attempt_counter
            if check_attempt_counter <= 3:
                print(f"Couldn't load the element properly. Trying again. This is attempt {check_attempt_counter}/3")
                check_attempt_counter += 1
                driver.refresh()
                return check_availability()


def main():
    login_handler(driver, url)
    check_availability()

main()




