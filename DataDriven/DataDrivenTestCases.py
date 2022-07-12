import time
import unittest
import ExcelUtil
from selenium import webdriver
from selenium.webdriver.common.by import By

#set the path of the web driver
driver = webdriver.Firefox(executable_path="C:\\Users\\Shiva\\Downloads\\geckodriver-v0.31.0-win64\\geckodriver.exe")

#open the url
driver.get("https://www.trivago.in/")

#set the path of the excel file
path = ("C:\\Users\\Shiva\\OneDrive\\Desktop\\capgemini training\\Automation testing\\selenium\\sprint _2\\Book1.xlsx")

#access the row count method
rows = ExcelUtil.getRowCount(path,"Sheet2")
print(rows)

#access Readdata method to get the inputs from excel file and pass in to the application using for loop

for r in range(2,rows+1):
    driver.implicitly_wait(3)
    Location = ExcelUtil.ReadData(path,"Sheet2",r,1)
    driver.find_element(by=By.ID, value="input-auto-complete").clear()
    driver.find_element(by=By.ID, value="input-auto-complete").send_keys(Location)
    driver.find_element(by=By.XPATH,value="//li[@id='react-autowhatever-1--item-0']//div[@data-testid='ssg-element']//div[@class='flex items-center']").click()  # click any where
    driver.find_element(by=By.XPATH, value="//button[@aria-label='Search']").click()  #

    driver.get("https://www.trivago.in/")