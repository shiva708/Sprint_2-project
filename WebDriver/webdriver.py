import time
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

class trivagoTest(unittest.TestCase):
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\\Users\\Shiva\\Downloads\\chromedriver_win32\\chromedriver.exe")
        cls.driver.maximize_window()

    def test_homePageTitle(self):
        self.driver.get("https://www.trivago.in/")
        self.driver.implicitly_wait(10)
        actual = self.driver.title
        self.assertEqual("trivago.in - Compare hotel prices worldwide",actual,"web page title is not matching")

    def test_homePage(self):
        self.driver.get("https://www.trivago.in/")
        self.driver.find_element(by=By.XPATH, value="//label[contains(text(),'Hotel')]").click() #
        self.driver.find_element(by=By.ID,value="input-auto-complete").clear() #
        self.driver.find_element(by=By.ID, value="input-auto-complete").send_keys("M") #
        self.driver.find_element(by=By.XPATH,value="//body[1]/div[1]/div[1]/main[1]/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/form[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[4]/td[3]/time[1]/button[1]/span[1]").click() #
        self.driver.find_element(by=By.XPATH,value="//body[1]/div[1]/div[1]/main[1]/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/form[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[4]/td[5]/time[1]/button[1]/span[1]").click() #

        self.driver.find_element(by=By.XPATH,value="//body/div[@id='__next']/div[1]/main[1]/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/form[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[2]/span[1]").click()  #selecting the adults

        self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[1]/main/div[3]/div[2]/div/div[3]/div/div/form/div[4]/div/div/div[2]/div/div[2]/div/button[2]").click() # adding child plus 2
        self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[1]/main/div[3]/div[2]/div/div[3]/div/div/form/div[4]/div/div/div[2]/div/div[2]/div/button[2]").click()

        self.driver.find_element(by=By.XPATH,value="//strong[contains(text(),'Apply')]").click() # apply button

        self.driver.find_element(by=By.XPATH,value="//div[@class='SearchFormFlyout_searchButtonWrapperSingleLine__EnPdo flex-grow']//button[@type='submit']").click()  # search button

        wait = WebDriverWait(self.driver, 10)  # too wait the driver for perticuler sec
        hotle = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/main/div[2]/div[2]/div/div/div/div[2]/div/ul/li[2]/div/label")))
        hotle.click()
        print(self.driver.current_url)
        #time.sleep(40)
        # mouse over actions
        moreFilters = self.driver.find_element(by=By.NAME, value="more_filters")
        actions = ActionChains(self.driver)
        actions.move_to_element(moreFilters).perform()

        wifi = self.driver.find_element(by=By.ID, value="filter-checkbox-3")
        actions = ActionChains(self.driver)
        actions.move_to_element(wifi).click().perform()

        pool = self.driver.find_element(by=By.ID, value="filter-checkbox-2")
        actions.move_to_element(pool).click().perform()

        resturent = self.driver.find_element(by=By.ID, value="filter-checkbox-8")
        actions.move_to_element(resturent).click().perform()

        # sorting
        self.driver.find_element(by=By.XPATH, value="//select[@id='sorting-selector']").click()
        #time.sleep(2)
        self.driver.find_element(by=By.XPATH, value="//option[@value='6']").click()




        '''Select(self.driver.find_element(by=By.ID, value="select-id22")).select_by_visible_text("Rating only")
        time.sleep(25)
        self.driver.save_screenshot("C:\\Users\\win10\\Desktop\\ScreenShot\\rating1.png")
        self.driver.execute_script("window.scrollBy(0,1000)", "")
        time.sleep(10)
        self.driver.save_screenshot("C:\\Users\\win10\\Desktop\\ScreenShot\\rating2.png")
        self.driver.execute_script("window.scrollBy(0,1000)", "")
        time.sleep(10)
        self.driver.save_screenshot("C:\\Users\\win10\\Desktop\\ScreenShot\\rating3.png")
        self.driver.execute_script("window.scrollBy(0,3000)", "")
        time.sleep(10)'''

    def tearDownClass(cls):
        cls.driver.close()
        print("test completed...!")

if __name__=="__main__":
    unittest.main()
