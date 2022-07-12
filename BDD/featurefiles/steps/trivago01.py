from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'user launch the trivago browser')
def launch_browser(context):
    context.driver=webdriver.Firefox(executable_path="C:\\Users\\Shiva\\Downloads\\geckodriver-v0.31.0-win64\\geckodriver.exe")
    context.driver.get("https://www.trivago.in/")

@given(u'user maximize the window')
def maximizeWindow(context):
    context.driver.maximize_window()


@given(u'user verify the title')
def step_impl(context):
    context.driver.implicitly_wait(10)
    actual = context.driver.title
    assert("trivago.in - Compare hotel prices worldwide", actual, "web page title is not matching")


@then(u'user close the browser')
def closeBrowser(context):
    context.driver.close()
