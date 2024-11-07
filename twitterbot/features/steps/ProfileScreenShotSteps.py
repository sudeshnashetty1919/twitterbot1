import time
import unittest
from _ast import And

from behave import *
from pages.BasePage import BasePage
from pages.Loginpage import LoginPage, generate_random_text

@when('user types {content}')
def enter_content_for_post(context, content):
    # Generate a random message of length 5
    random_message = generate_random_text(5)
    print(f"Generated random message: {random_message}")

    # Enter the random message
    context.login_page.enter_content(random_message)

    # Enter the content from the feature file
    context.login_page.enter_content(content)

@when('user clicks on post')
def step_user_clicks_post(context):
    time.sleep(5)
    context.login_page.click_on_post()

@then('user should get a toast {message}')
def step_user_gets_toast_message(context, message):
    toast_messages = context.login_page.toast_message_check()
    assert toast_messages == message

@then('user clicks on logout')
def step_user_clicks_logout(context):
    context.login_page.click_on_user_name()
    time.sleep(5)
    context.login_page.click_log_out()
    time.sleep(5)
    context.login_page.click_on_logout_confirm()
    BasePage.quit_driver()

@when("user clicks on notifications and opens the account")
def step_user_clicks_notifications_and_opens_account(context):
    time.sleep(5)
    context.login_page.click_on_notifications()  # Use the correct attribute
    time.sleep(5)
    context.login_page.click_on_tagger_name()  # Use the correct method

@when("user takes a screenshot")
def step_user_takes_screenshot(context):
    time.sleep(5)
    context.login_page.take_screenshot()


@when("click back")
def step_click_back(context):
    context.login_page.click_on_back() # Assuming you have defined this method in your LoginPage class

@when("posts the screenshot")
def step_user_posts_screenshot(context):
    time.sleep(5)
    context.login_page.click_on_reply_post()

@when("clicks on reply")
def step_clicks_on_reply(context):
    time.sleep(5)
    context.login_page.click_on_reply()  # Assuming you have defined this method in your LoginPage class
    context.login_page.upload_screenshot()  # Assuming you have defined this method in your LoginPage class
    time.sleep(5)  # Wait for 5 seconds (consider using WebDriverWait instead)
@then("close the popup if opened")
def step_user_closes_popup(context):
    time.sleep(5)
    context.login_page.close_pop_up()



