'''from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'user launch the trivago broswer')
def launchBrowser(context):
    context.driver = webdriver.Firefox(executable_path="C:\\Users\\Shiva\\Downloads\\geckodriver-v0.31.0-win64\\geckodriver.exe")
    context.driver.get("https://www.trivago.in/")


@given(u'user should select on hotels')
def selectHotel(context):
    context.driver.find_element(by=By.XPATH, value="//label[contains(text(),'Hotel')]").click()



@when(u'User click on search location bar and enter the location as "hyderabad"')
def step_impl(context):
    context.driver.implicitly_wait(10)
    context.driver.find_element(by=By.ID, value="input-auto-complete").clear()
    context.driver.find_element(by=By.ID, value="input-auto-complete").send_keys("Hyderabad")
    #context.driver.find_element(by=By.XPATH,value="//li[@id='react-autowhatever-1--item-0']//div[@data-testid='ssg-element']//div[@class='flex items-center']").click()  # click any where
    context.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[1]/main/div[2]/div/div/svg/path[2]").click() #click any where
    context.driver.implicitly_wait(10)


@when(u'give the checkin and checkout dates')
def dates(context):
    context.driver.implicitly_wait(10)
    context.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[1]/main/div[3]/div[2]/div/div[3]/div/div/form/fieldset/div/div[1]/button").click()
    context.driver.find_element(by=By.XPATH,value="//time[@datetime='2022-07-25']//button[@type='button']//span[@class='absolute inset-0 flex justify-center items-center overflow-hidden -mt-px -ml-px border-transparent'][contains(text(),'25')]").click()  #
    context.driver.find_element(by=By.XPATH,value="//time[@datetime='2022-07-28']//button[@type='button']//span[@class='absolute inset-0 flex justify-center items-center overflow-hidden -mt-px -ml-px border-transparent'][contains(text(),'28')]").click()  #


@when(u'select the No of adults and childs and apply')
def noOfpersons(context):
    context.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[1]/main/div[3]/div[2]/div/div[3]/div/div/form/div[4]/div/div/div[2]/div/div[1]/div/button[2]").click()  #
    context.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[1]/main/div[3]/div[2]/div/div[3]/div/div/form/div[4]/div/div/div[2]/div/div[2]/div/button[2]").click()  #
    context.driver.find_element(by=By.XPATH,value="//strong[contains(text(),'Apply')]").click()  #


@then(u'user search the hotels and it will display')
def search(context):
    context.driver.find_element(by=By.XPATH, value="//button[@aria-label='Search']").click()'''