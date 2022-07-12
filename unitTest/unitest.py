import unittest
import time

from selenium import webdriver
import HtmlTestRunner
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains



class trivagoTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path="C:\\Users\\Shiva\\Downloads\\geckodriver-v0.31.0-win64\\geckodriver.exe")
        cls.driver.maximize_window()

    def test_homePageTitle(self):
        self.driver.get("https://www.trivago.in/")
        self.driver.implicitly_wait(10)
        actual = self.driver.title
        self.assertEqual("trivago.in - Compare hotel prices worldwide",actual,"web page title is not matching")

    def test_homePage(self):
        self.driver.get("https://www.trivago.in/")
        self.driver.implicitly_wait(30)
        self.driver.find_element(by=By.XPATH, value="//label[contains(text(),'Hotel')]").click()  #
        self.driver.find_element(by=By.ID, value="input-auto-complete").clear()  #
        self.driver.find_element(by=By.ID, value="input-auto-complete").send_keys("Hyderabad")  #
        #self.driver.find_element(by=By.XPATH,value="//body/div[@id='__next']/div[1]/main[1]/div[3]").click() #click any where
        self.driver.find_element(by=By.XPATH,value="//li[@id='react-autowhatever-1--item-0']//div[@data-testid='ssg-element']//div[@class='flex items-center']").click() #click any where
        #self.driver.find_element(by=By.XPATH,value="//span[contains(text(),'Check in')]").click()  #
        #self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[1]/main/div[3]/div[2]/div/div[3]/div/div/form/fieldset/div/div[1]/button").click()  #
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.XPATH,value="//time[@datetime='2022-07-25']//button[@type='button']//span[@class='absolute inset-0 flex justify-center items-center overflow-hidden -mt-px -ml-px border-transparent'][contains(text(),'25')]").click()  #
        self.driver.find_element(by=By.XPATH,value="//time[@datetime='2022-07-28']//button[@type='button']//span[@class='absolute inset-0 flex justify-center items-center overflow-hidden -mt-px -ml-px border-transparent'][contains(text(),'28')]").click()  #
        self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[1]/main/div[3]/div[2]/div/div[3]/div/div/form/div[4]/div/div/div[2]/div/div[1]/div/button[2]").click()  #
        self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[1]/main/div[3]/div[2]/div/div[3]/div/div/form/div[4]/div/div/div[2]/div/div[2]/div/button[2]").click()  #
        self.driver.find_element(by=By.XPATH,value="//strong[contains(text(),'Apply')]").click()  #
        self.driver.find_element(by=By.XPATH,value="//button[@aria-label='Search']").click()  #

        '''self.driver.get("https://www.trivago.in/")
        self.driver.implicitly_wait(5)
        self.driver.find_element(by=By.XPATH,value="//label[contains(text(),'Hotel')]").click()  #
        self.driver.find_element(by=By.ID,value="input-auto-complete").clear()  #
        self.driver.find_element(by=By.ID,value="input-auto-complete").send_keys("Hyderabad")  #
        time.sleep(5)
        #self.driver.find_element(by=By.XPATH,value="//body/div[@id='__next']/div[1]/main[1]/div[3]").click()  # click any where
        self.driver.find_element(by=By.XPATH,value="//li[@id='react-autowhatever-1--item-0']//div[@data-testid='ssg-element']//div[@class='flex items-center']").click()  # click any where

        #self.driver.find_element(by=By.XPATH,value="//button[@class='block px-2 bg-white text-left disabled:opacity-50 disabled:cursor-default w-full 2xl:rounded-l-sm flex items-center border-r-0 h-11']").click()  #
        self.driver.find_element(by=By.XPATH,value="//time[@datetime='2022-07-22']//button[@type='button']//span[@class='absolute inset-0 flex justify-center items-center overflow-hidden -mt-px -ml-px border-transparent'][contains(text(),'22')]").click()  #
        self.driver.find_element(by=By.XPATH,value="//time[@datetime='2022-07-25']//button[@type='button']//span[@class='absolute inset-0 flex justify-center items-center overflow-hidden -mt-px -ml-px border-transparent'][contains(text(),'25')]").click()  #
        self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[1]/main/div[3]/div[2]/div/div[3]/div/div/form/div[4]/div/div/div[2]/div/div[1]/div/button[2]").click()  #
        self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[1]/main/div[3]/div[2]/div/div[3]/div/div/form/div[4]/div/div/div[2]/div/div[2]/div/button[2]").click()  #
        self.driver.find_element(by=By.XPATH,value="//strong[contains(text(),'Apply')]").click()  #
        self.driver.find_element(by=By.XPATH,value="//button[@aria-label='Search']").click()  #
'''
        time.sleep(3)
        self.driver.save_screenshot("C:\\Users\\Shiva\\OneDrive\\Desktop\\capgemini training\\Automation testing\\selenium\\sprint _2\\screenShorts\\ss1.png")
        self.driver.execute_script("window.scrollBy(0,1000)", "")
        #self.time.sleep(10)'''

    def test_hotelsPage(self):

        self.driver.get("https://www.trivago.in/en-IN/lm/hotels-Hyderabad-india?search=200-64981;dr-20220720-20220722;rc-1-3-6-6")
        #time.sleep(40)
        #self.driver.implicitly_wait(40)
        self.driver.implicitly_wait(40)
        self.driver.find_element(by=By.XPATH,value="//span[@class='inline-flex leading-none Icon_sIcon__5F7YL transform']").click()
        self.driver.implicitly_wait(40)

        self.driver.find_element(by=By.XPATH,value="//input[@id='input-auto-complete']").send_keys("Hyderabad")
        #self.driver.find_element(by=By.XPATH,value="//body[@class='font-body text-grey-900']/div[@id='__next']/div/div/main/div[contains(@class,'bg-grey-100 top-0 sticky z-10 transition-transform duration-400 transform SearchAndRefinements_willChangeTransform___3jJP')]/div[contains(@class,'fresnel-container fresnel-greaterThanOrEqual-2xl')]/div[@class='bg-grey-100']/div[1]").click()
        self.driver.find_element(by=By.XPATH,value="//li[@id='react-autowhatever-1--item-0']//div[@data-testid='ssg-element']//div[@class='flex items-center']").click()
        self.driver.find_element(by=By.XPATH,value="//span[contains(text(),'Check in')]").click()
        self.driver.find_element(by=By.XPATH,value="//time[@datetime='2022-07-25']//button[@type='button']//span[@class='absolute inset-0 flex justify-center items-center overflow-hidden -mt-px -ml-px border-transparent'][contains(text(),'25')]").click()
        self.driver.find_element(by=By.XPATH,value="//time[@datetime='2022-07-28']//button[@type='button']//span[@class='absolute inset-0 flex justify-center items-center overflow-hidden -mt-px -ml-px border-transparent'][contains(text(),'28')]").click()
        #self.driver.find_element(by=By.XPATH,value="//div[@class='SearchFormFlyout_roomSelector__b6ynD']//button[@type='button']").click()
        #self.driver.find_element(by=By.XPATH,value="//button[@data-testid='guest-selector']//span[@class='flex items-center']").click()
        time.sleep(0)
        #self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div[1]/main/div[1]/div[4]/div/form/div[4]/div/div/div[2]/div/div[1]/div/button[2]").click()
        #self.driver.find_element(by=By.XPATH,value="//button[@data-testid='adults-amount-plus-button']//span[@class='inline-flex leading-none transform self-center']").click()
        #self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div[1]/main/div[1]/div[4]/div/form/div[4]/div/div/div[2]/div/div[1]/div/button[2]").click()
        self.driver.find_element(by=By.XPATH,value="//div[@class='SearchFormFlyout_searchButtonWrapperSingleLine__EnPdo ml-2']//button[@type='submit']").click()
        time.sleep(20)
        #time.sleep(25)
        self.driver.save_screenshot("C:\\Users\\Shiva\\OneDrive\\Desktop\\capgemini training\\Automation testing\\selenium\\sprint _2\\screenShorts\\ssH1.png")
        self.driver.execute_script("window.scrollBy(0,1000)", "")


    def test_mouseOverActionsAndCheckBox(self):
        self.driver.get("https://www.trivago.in/en-IN/lm/hotels-Hyderabad-india?search=200-64981;dr-20220720-20220722;rc-1-3-6-6")
        #waitMethod
        time.sleep(40)
        self.driver.find_element(by=By.XPATH,value="//span[@class='inline-flex leading-none Icon_xsIcon__3GJOL transform text-grey-700']").click()
        time.sleep(10)
        self.driver.implicitly_wait(10)
        wait = WebDriverWait(self.driver, 10)  # too wait the driver for perticuler sec
        Hotle = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/main/div[2]/div[2]/div/div/div/div[2]/div/ul/li[2]/div/label")))
        Hotle.click()
        time.sleep(40)
        #mouseOverActions
        moreFilters = self.driver.find_element(by=By.NAME, value="more_filters")
        actions = ActionChains(self.driver)
        actions.move_to_element(moreFilters).perform()
        #selectingTheCheckBox_DuringMouseOverActions
        wifi = self.driver.find_element(by=By.ID, value="filter-checkbox-3")
        actions = ActionChains(self.driver)
        actions.move_to_element(wifi).click().perform()
        pool = self.driver.find_element(by=By.ID, value="filter-checkbox-2")
        actions.move_to_element(pool).click().perform()
        resturent = self.driver.find_element(by=By.ID, value="filter-checkbox-8")
        actions.move_to_element(resturent).click().perform()
        time.sleep(25)
        self.driver.save_screenshot("C:\\Users\\Shiva\\OneDrive\\Desktop\\capgemini training\\Automation testing\\selenium\\sprint _2\\screenShorts\\ssM_O_A&C_B.png")
        self.driver.execute_script("window.scrollBy(0,1000)", "")
        #selectingTheCheckBox_DuringMouseOverActions----01
        # mouse over action for location
        location = self.driver.find_element(by=By.NAME, value="location_filters")
        actions.move_to_element(location).perform()
        cityCenter = self.driver.find_element(by=By.ID,value="poiselect")
        actions.move_to_element(cityCenter).click().perform()
        time.sleep(25)
        self.driver.save_screenshot("C:\\Users\\Shiva\\OneDrive\\Desktop\\capgemini training\\Automation testing\\selenium\\sprint _2\\screenShorts\\ssM_O_A&C_B-01.png")
        self.driver.execute_script("window.scrollBy(0,1000)", "")
        #mouseOverActionOn_GuestRating
        guest_Rating = self.driver.find_element(by=By.XPATH,value="//button[@name='guest_rating_filters']")
        actions.move_to_element(guest_Rating).perform()
        guest_Rating_8 = self.driver.find_element(by=By.XPATH,value="//button[@data-testid='8.5-rating-hotels-filter']")
        actions.move_to_element(guest_Rating_8).click().perform()
        time.sleep(25)
        self.driver.save_screenshot("C:\\Users\\Shiva\\OneDrive\\Desktop\\capgemini training\\Automation testing\\selenium\\sprint _2\\screenShorts\\ssM_O_A&C_B-02.png")
        self.driver.execute_script("window.scrollBy(0,1000)", "")
        #sort By
        self.driver.find_element(by=By.ID,value="sorting-selector").click()
        self.driver.find_element(by=By.XPATH,value="//select[@id='sorting-selector']//option[@value='6']").click()
        time.sleep(25)
        self.driver.save_screenshot("C:\\Users\\Shiva\\OneDrive\\Desktop\\capgemini training\\Automation testing\\selenium\\sprint _2\\screenShorts\\ssM_O_A&C_B-03.png")
        self.driver.execute_script("window.scrollBy(0,1000)", "")





    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Test Completed...!")

if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\Shiva\\OneDrive\\Desktop\\capgemini training\\Automation testing\\selenium\\sprint _2\\Reports"))