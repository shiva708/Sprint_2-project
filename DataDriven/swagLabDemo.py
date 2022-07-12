import time
import ExcelUtil
from selenium import webdriver
from selenium.webdriver.common.by import By

#set the path of the web driver
driver = webdriver.Firefox(executable_path="C:\\Users\\Shiva\\Downloads\\geckodriver-v0.31.0-win64\\geckodriver.exe")

#open the url
driver.get("https://www.saucedemo.com/")

#set the path of the excel file
path = ("C:\\Users\\Shiva\\OneDrive\\Desktop\\capgemini training\\Automation testing\\selenium\\sprint _2\\Book2.xlsx")

#access the row count method
rows = ExcelUtil.getRowCount(path,"Sheet1")
print(rows)

#access Readdata method to get the inputs from excel file and pass in to the application using for loop


for r in range(2,rows+1):
    username = ExcelUtil.ReadData(path,"Sheet1",r,1)
    password = ExcelUtil.ReadData(path,"Sheet1",r,2)
    driver.find_element(by=By.NAME,value="user-name").send_keys(username)
    driver.find_element(by=By.NAME,value="password").send_keys(password)
    time.sleep(10)
    driver.find_element(by=By.ID,value="login-button").click()
    if driver.title=="Swag Labs":
        print("Successfully Login.. ")
        ExcelUtil.WriteData(path,"Sheet1",r,3,"Successfully logined...!")
    else:
        print("incorrect UserName or Password")
        ExcelUtil.WriteData(path,"Sheet1",r,3,"Wrong Password")


    driver.get("https://www.saucedemo.com/")

driver.close()

