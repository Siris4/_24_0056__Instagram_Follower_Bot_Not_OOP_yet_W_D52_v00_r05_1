import sys
import time
import re
import threading
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException

def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} - {message}")

def click_not_now_button(driver):
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Not now']")))
        log_message("Popup 'Not now' button appeared.")
    except TimeoutException:
        log_message("No 'Not now' popup within 3 seconds.")
        return

    selectors = [
        {"by": By.XPATH, "value": "//div[text()='Not now']"},
        {"by": By.XPATH, "value": "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div"},
        {"by": By.CSS_SELECTOR, "value": "#mount_0_0_i\\+ > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > section > main > div > div > div > div > div"},
        {"by": By.CLASS_NAME, "value": "x1i10hfl"}
    ]

    for selector in selectors:
        try:
            element = driver.find_element(selector["by"], selector["value"])
            element.click()
            log_message(f"'Not now' button clicked using {selector['by']}='{selector['value']}'")
            break
        except NoSuchElementException:
            log_message(f"'Not now' button not found using {selector['by']}='{selector['value']}'")
        except Exception as e:
            log_message(f"Error clicking 'Not now' button using {selector['by']}='{selector['value']}': {e}")

INSTAGRAM_EMAIL = "YOUR_EMAIL"
INSTAGRAM_PASSWORD = "YOUR_PASSWORD"
URL_FOR_INSTAGRAM = "https://www.instagram.com/"

options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

def login_instagram(driver, email, password):
    log_message("Starting login process")
    driver.get(URL_FOR_INSTAGRAM)
    time.sleep(5)

    # Layered Catch Mechanism for locating the username field
    selectors = [
        (By.NAME, "username"),
        (By.XPATH, "//input[@aria-label='Phone number, username, or email']"),
        (By.CLASS_NAME, "_aa4b"),
        (By.CSS_SELECTOR, "input[name='username']"),
        (By.CSS_SELECTOR, "#loginForm > div > div:nth-child(1) > div > label > input"),
        (By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input"),
        (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
    ]

    username_field = None
    for by, value in selectors:
        try:
            username_field = driver.find_element(by, value)
            log_message(f"Attempting to find username field using {by}='{value}'")
            if username_field:
                log_message("Username field found")
                break
        except NoSuchElementException:
            log_message(f"Failed to find username field using {by}='{value}'")

    if username_field is None:
        log_message("Username field not found after trying all selectors.")
        raise Exception("Username field not found after trying all selectors.")

    username_field.send_keys(email)
    log_message("Email entered")
    time.sleep(2)

    password_field = driver.find_element(By.NAME, "password")
    log_message("Attempting to find password field")
    password_field.send_keys(password)
    log_message("Password entered")
    time.sleep(2)

    password_field.send_keys(Keys.RETURN)
    log_message("Login submitted")
    time.sleep(5)

try:
    login_instagram(driver, INSTAGRAM_EMAIL, INSTAGRAM_PASSWORD)
    click_not_now_button(driver)  # Ensure this function is called right after login
    log_message("Login process completed. Browser will remain open until manually closed.")
except Exception as e:
    log_message(f"An error occurred during login: {str(e)}")

log_message("Login process completed. Checking for 'Not now' button.")








def click_second_not_now_button(driver):
    time.sleep(3)  # Wait for 3 seconds before looking for the second button
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Not Now']")))
        log_message("Second 'Not now' button appeared.")
    except TimeoutException:
        log_message("No second 'Not now' popup within 3 seconds.")
        return

    selectors = [
        {"by": By.XPATH, "value": "//button[text()='Not Now']"},
        {"by": By.XPATH, "value": "/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]"},
        {"by": By.CSS_SELECTOR, "value": "button._a9--._ap36._a9_1"},
        {"by": By.CLASS_NAME, "value": "_a9--"}
    ]

    for selector in selectors:
        try:
            element = driver.find_element(selector["by"], selector["value"])
            element.click()
            log_message(f"Second 'Not now' button clicked using {selector['by']}='{selector['value']}'")
            break
        except NoSuchElementException:
            log_message(f"Second 'Not now' button not found using {selector['by']}='{selector['value']}'")
        except Exception as e:
            log_message(f"Error clicking second 'Not now' button using {selector['by']}='{selector['value']}': {e}")

try:
    login_instagram(driver, INSTAGRAM_EMAIL, INSTAGRAM_PASSWORD)
    click_not_now_button(driver)  # Click the first 'Not Now' button
    click_second_not_now_button(driver)  # Click the second 'Not Now' button after waiting
    log_message("Login process completed. Browser will remain open until manually closed.")
except Exception as e:
    log_message(f"An error occurred during login: {str(e)}")

log_message("Login process completed. Checking for 'Not now' button.")

input("Press Enter to close the browser...")
driver.quit()




input("Press Enter to close the browser...")
driver.quit()
