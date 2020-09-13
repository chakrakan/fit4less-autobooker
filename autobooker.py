from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from selenium import webdriver
import logging
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

load_dotenv()
start_url = "https://myfit4less.gymmanager.com/portal/login.asp"
booking_date = str(datetime.now().date() + timedelta(days=int(os.getenv("DAYS")) or 2))
driver = None

chrome_options = Options()

if os.getenv("ENVIRONMENT") == "dev":
    chrome_options.add_argument("--window-size=1920,1080")
else:
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(os.getenv("WEBDRIVER_PATH"), options=chrome_options)
driver.get(start_url)

try:
    # Login
    email_input = driver.find_element_by_id("emailaddress")
    password_input = driver.find_element_by_id("password")
    driver.implicitly_wait(5)
    email_input.send_keys(os.getenv("F4L_LOGIN"))
    password_input.send_keys(os.getenv("F4L_PASSWORD"))
    driver.implicitly_wait(5)
    password_input.send_keys(Keys.ENTER)
    driver.implicitly_wait(5)
    logging.info("Logged In!")

    date_select = driver.find_element_by_id("btn_date_select")

    if not date_select.is_displayed():
        logging.info("Already booked max slots")
        driver.quit()

    date_select.click()  # day selector
    driver.implicitly_wait(3)
    driver.find_element_by_id("date_" + booking_date).click()  # select 2 days ahead from now
    driver.implicitly_wait(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.implicitly_wait(3)

    # check available_slots class 2nd index -> see if child elements exist
    available_slots = driver.find_elements_by_class_name("available-slots")[1].find_elements_by_class_name(
        "time-slot-box")

    for slot in available_slots:
        if str(os.getenv("TIME_SLOT")) in slot.text:
            logging.info("Time slot found: ", slot.text)
            slot.find_element_by_xpath('..').click()
            driver.implicitly_wait(3)
            driver.find_element_by_id("dialog_book_yes").click()
            driver.implicitly_wait(5)
            logging.info("Reservation done!")
            break
        else:
            logging.info("Skipping slot:", slot.text)

except Exception as err:
    logging.warning(str(err))
finally:
    driver.quit()
