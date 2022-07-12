import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC



class homepage_Test02(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path="C:\\Users\\Shiva\\Downloads\\geckodriver-v0.31.0-win64\\geckodriver.exe")
        cls.driver.maximize_window()


    def test_clickOnlogin(self):
        self.driver.get("https://www.trivago.in/")
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.XPATH,value="//span[contains(text(),'Log in')]").click()
        #self.driver.find_element(by=By,value="//span[contains(text(),'Log in')]").click()
        print("clickonlogin is tested...!")

    def test_cursorOnmenu(self):
        self.driver.get("https://www.trivago.in/")
        #this part is mouse over actions
        menu = self.driver.find_element(by=By.XPATH,value="//div[@class='h-full']")
        actions = ActionChains(self.driver)
        actions.move_to_element(menu).click().perform()
        print("mouseOverAction is tested...!")

    def test_clickOnINR(self):
        self.driver.get("https://www.trivago.in/")
        self.driver.find_element(by=By.ID,value="currency-selector").click()
        print("selecting on INR is tested...!")



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Test Completed...!")


if __name__ == "__main__":
    unittest.main()
