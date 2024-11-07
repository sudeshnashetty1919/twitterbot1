import time
import unittest
from _ast import And

from behave import *
from pages.BasePage import BasePage
from pages.Loginpage import LoginPage, generate_random_text


@when('user types note {account} to tag')
def enter_content_for_post(context, account):
    # Generate a random message of length 5
    random_message = generate_random_text(5)
    context.login_page.enter_content(random_message +" " + account)


@when('user clicks on post to tag')
def step_user_clicks_post(context):
    time.sleep(5)
    context.login_page.click_on_post()

@then('user should get a toast {message} after tagging')
def step_user_gets_toast_message(context, message):
    toast_messages = context.login_page.toast_message_check()
    assert toast_messages == message

@then('user clicks on logout after tagging')
def step_user_clicks_logout(context):
    context.login_page.click_on_user_name()
    time.sleep(5)
    context.login_page.click_log_out()
    time.sleep(5)
    context.login_page.click_on_logout_confirm()
    BasePage.quit_driver()