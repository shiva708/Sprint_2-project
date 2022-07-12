import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class homepage_Test01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path="C:\\Users\\Shiva\\Downloads\\geckodriver-v0.31.0-win64\\geckodriver.exe")
        cls.driver.maximize_window()

    def test_homePage(self):
        self.driver.get("https://www.trivago.in/")
        self.driver.implicitly_wait(30)
        self.driver.find_element(by=By.XPATH, value="//label[contains(text(),'Hotel')]").click()  #
        self.driver.find_element(by=By.ID, value="input-auto-complete").clear()  #
        self.driver.find_element(by=By.ID, value="input-auto-complete").send_keys("Hyderabad")  #
        # self.driver.find_element(by=By.XPATH,value="//body/div[@id='__next']/div[1]/main[1]/div[3]").click() #click any where
        self.driver.find_element(by=By.XPATH,value="//li[@id='react-autowhatever-1--item-0']//div[@data-testid='ssg-element']//div[@class='flex items-center']").click()  # click any where
        # self.driver.find_element(by=By.XPATH,value="//span[contains(text(),'Check in')]").click()  #
        print("entering the locations on fields is tested...!")


    def test_searchButton(self):
        self.driver.get("https://www.trivago.in/")
        self.driver.find_element(by=By.XPATH, value="//button[@aria-label='Search']").click()  #
        print("Action on click search is tested...!")



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Test Completed...!")

if __name__=="__main__":
    unittest.main()