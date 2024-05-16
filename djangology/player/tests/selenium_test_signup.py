from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()


def wait_for_clickable(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )


def wait_for_visible(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )


try:
    driver.get("http://ec2-18-226-166-86.us-east-2.compute.amazonaws.com:8080/auth/signup_nav/")

    username_input = wait_for_visible(driver, (By.ID, "username"))
    password_input = wait_for_visible(driver, (By.ID, "password"))
    display_name_input = wait_for_visible(driver, (By.ID, "displayname"))
    signup_button = wait_for_visible(driver, (By.ID, "signup-button"))

    username_input.send_keys("testuser")
    time.sleep(2)
    password_input.send_keys("password")
    time.sleep(2)
    display_name_input.send_keys("Test User")
    time.sleep(2)

    signup_button.click()
    time.sleep(2)


except Exception as e:
    print("An error occurred:", e)

finally:
    driver.quit()
