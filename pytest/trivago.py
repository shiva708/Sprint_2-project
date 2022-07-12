import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains


def test_setup():
    global driver
    driver = webdriver.Firefox(executable_path="C:\\Users\\Shiva\\Downloads\\geckodriver-v0.31.0-win64\\geckodriver.exe")
    driver.maximize_window()


def test_homePageTitle():
    driver.get("https://www.trivago.in/")
    driver.implicitly_wait(10)
    actual = driver.title
   # assertEqual("trivago.in - Compare hotel prices worldwide", actual, "web page title is not matching")
    print("test 2 completed")

def tearDownClass(cls):
    cls.driver.close()
    print("Test Completed...!")