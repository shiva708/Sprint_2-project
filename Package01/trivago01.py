import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class homePageTitle_Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path="C:\\Users\\Shiva\\Downloads\\geckodriver-v0.31.0-win64\\geckodriver.exe")
        cls.driver.maximize_window()


    def test_HomepageTitle(self):
        self.driver.get("https://www.trivago.in/")
        self.driver.implicitly_wait(10)
        actual = self.driver.title
        self.assertEqual("trivago.in - Compare hotel prices worldwide", actual, "web page title is not matching")
        print("checking the title is tested...!")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Test Completed...!")


if __name__=="__main__":
    unittest.main()