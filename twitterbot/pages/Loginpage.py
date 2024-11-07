import os
import string
import time
from datetime import datetime
from random import random

from selenium.common import WebDriverException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage
import random
import string

def generate_random_text(length):
    """Generate a random string of fixed length."""
    letters = string.ascii_letters + string.digits + string.punctuation
    random_text = ''.join(random.choice(letters) for _ in range(length))
    return random_text


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.js_executor = driver
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.screenshot_name = f"screenshot_{self.timestamp}.png"
        self.img_upload_locator = (By.XPATH, "//input[@type='file']")
        self.toast_message_locator = (By.XPATH, "//span[contains(text(),'Your post was sent.')]")  # Adjust XPath as necessary
        self.post_button = (By.XPATH, "//button[@data-testid='tweetButtonInline' and .//span[text()='Post']]")
        self.email = (By.XPATH, "//input[@name='text']")
        self.next_button = (By.XPATH, "//span[contains(text(),'Next')]")
        self.pass_input = (By.XPATH, "//input[@type='password']")
        self.log_in = (By.XPATH, "//span[contains(text(),'Log in')]")
        self.log_out = (By.XPATH, "//span[contains(text(),'Log out @')]")
        self.toast_message = (By.XPATH, "//span[contains(text(),'Your post was sent.')]")
        self.post_content = (By.XPATH, "//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']")
        self.user_name = (By.XPATH, "//div[@class='css-175oi2r r-1adg3ll r-bztko3']")
        self.logout_confirm = (By.XPATH, "//button[@data-testid='confirmationSheetConfirm']")
        self.notifications = (By.XPATH, "(//div[@class='css-175oi2r'])[4]")
        self.tagger_name = (By.XPATH, "//a[contains(@class, 'r-dnmrzs')]/div/span")
        self.screen_for_shot = (By.XPATH, "(//div[@class='css-175oi2r'])[16]")
        self.reply_button = (By.XPATH, "//button[@data-testid='reply']")
        self.img_upload = (By.XPATH, "//input[@type='file']")
        self.back_from_profile = (By.XPATH, "//button[@aria-label='Back']")
        self.reply_post = (By.XPATH, "//button[@data-testid='tweetButton']")
        self.phone_number_user_name=(By.XPATH,"//input[@data-testid='ocfEnterTextTextInput']")
        self.pop_up=(By.XPATH, "//button[@aria-label='Close']")

    def enter_email(self, email_id):
        wait = WebDriverWait(self.driver, 10)
        email_element = wait.until(EC.presence_of_element_located(self.email))  # Use the locator here
        email_element.send_keys(email_id)

    def enter_pass(self, password):
        wait = WebDriverWait(self.driver, 10)
        pass_element = wait.until(EC.presence_of_element_located(self.pass_input))  # Use the locator here
        pass_element.send_keys(password)

    def click_on_log_in(self):
        log_in_element = self.driver.find_element(*self.log_in)
        log_in_element.click()

    def enter_content(self, content):
        content_element = self.driver.find_element(*self.post_content)
        content_element.send_keys(content)
        content_element.send_keys(Keys.SPACE)

    def click_on_post(self):
        wait = WebDriverWait(self.driver, 30)
        post_button_element = wait.until(EC.element_to_be_clickable(self.post_button))
        post_button_element.click()

    def click_on_next(self):
        next_button_element = self.driver.find_element(*self.next_button)
        next_button_element.click()

    def toast_message_check(self):
        wait = WebDriverWait(self.driver, 10)
        toast_element = wait.until(EC.visibility_of_element_located(self.toast_message))
        return toast_element.text

    def click_on_user_name(self):
        wait = WebDriverWait(self.driver, 10)
        user_name_element = wait.until(EC.presence_of_element_located(self.user_name))
        self.driver.execute_script("arguments[0].scrollIntoView();", user_name_element)
        user_name_element.click()

    def click_log_out(self):
        wait = WebDriverWait(self.driver, 10)
        log_out_element = wait.until(EC.element_to_be_clickable(self.log_out))
        log_out_element.click()

    def click_on_logout_confirm(self):
        logout_confirm_element = self.driver.find_element(*self.logout_confirm)
        logout_confirm_element.click()

    def click_on_notifications(self):
        notifications_element = self.driver.find_element(*self.notifications)
        notifications_element.click()

    def click_on_tagger_name(self):
        tagger_name_element = self.driver.find_element(*self.tagger_name)
        tagger_name_element.click()

    def click_on_back(self):
        back_element = self.driver.find_element(*self.back_from_profile)
        back_element.click()

    def click_on_reply(self):
        reply_element = self.driver.find_element(*self.reply_button)
        reply_element.click()

    def upload_screenshot(self):
        destination_file = os.path.join(os.getcwd(), "twitterBot", "screenshots", self.screenshot_name)
        wait = WebDriverWait(self.driver, 10)
        img_upload_element = wait.until(EC.presence_of_element_located(self.img_upload_locator))

        # Now you can call send_keys on the WebElement
        img_upload_element.send_keys(destination_file)

    def click_on_reply_post(self):
        wait = WebDriverWait(self.driver, 30)
        reply_post_element = wait.until(EC.element_to_be_clickable(self.reply_post))
        reply_post_element.click()

    def take_screenshot(self):
        try:
            # Assuming 'screenForShot' is a WebElement you want to take a screenshot of
            element = self.driver.find_element(*self.screen_for_shot)  # Replace with your actual element locator
            element_screenshot = element.screenshot_as_png  # Take screenshot as PNG

            # Create the destination directory if it doesn't exist
            screenshots_dir = os.path.join(os.getcwd(), "twitterBot", "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            # Define the full path for the screenshot
            destination_file = os.path.join(screenshots_dir, self.screenshot_name)

            # Write the screenshot to the file
            with open(destination_file, 'wb') as file:
                file.write(element_screenshot)

            print(f"Screenshot saved as: {destination_file}")

        except WebDriverException as e:
            print("An error occurred while taking the screenshot:")
            print(e)
    def enter_phone_or_user_name(self, content):
        phone_number_element = self.driver.find_element(*self.phone_number_user_name)
        phone_number_element.send_keys(content)

    def close_pop_up(self):
        popup_element = self.driver.find_element(*self.pop_up)
        popup_element.click()

    def is_phone_or_user_name_asked(self):
        wait = WebDriverWait(self.driver, 30)
        try:
            # Wait for the element to be clickable
            phone_or_username_element = wait.until(EC.visibility_of_element_located(self.phone_number_user_name))
            return True
        except TimeoutException:
            print("Element not clickable within the timeout")
            return False  # Element wasn't clickable within the timeout, return False
