import time
import unittest
from _ast import And

from behave import *
from behave import after_all

from pages.BasePage import BasePage
from pages.Loginpage import LoginPage, generate_random_text

@given('user is on login page')
def step_user_on_login_page(context):
    context.login_page = LoginPage(BasePage.initialize_web_driver())

@when('user enters {username} and clicks on next')
def step_user_enters_credentials(context, username):
    time.sleep(5)
    context.login_page.enter_email(username)
    context.login_page.click_on_next()

@when('user enter {phone_or_username} and clicks on next')
def step_user_enters_phone_or_user_name(context, phone_or_username):
    # Wait for the input field to be ready if necessary (use explicit waits instead of time.sleep)
    if context.login_page.is_phone_or_user_name_asked():
        context.login_page.enter_phone_or_user_name(phone_or_username)
        context.login_page.click_on_next()


@when('user puts {password}')
def enter_password(context, password):
    context.login_page.enter_pass(password)

@when('user clicks on login')
def step_user_clicks_login(context):
    context.login_page.click_on_log_in()