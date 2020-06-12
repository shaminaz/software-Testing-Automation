import unittest
import time
import pytest
timestr = time.strftime("%y%m%d-%H%M%S")
from selenium import webdriver

class TestCount(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:/webDrivers/chromedriver")
        self.driver.maximize_window()

    def test_alertbox(self):
        self.driver.get("file://C:/Users/shaminaz/Documents/pop1.html")
        button = self.driver.find_element_by_name('alert')
        button.click()
        obj = self.driver.switch_to.alert
        msg = obj.text
        print("Alert shows following message: " + msg)
        time.sleep(2)
        obj.accept()
        print(" Clicked on the OK Button in the Alert Window")
        time.sleep(2);

    def test_confirmbox(self):
        location = "file://C:/Users/shaminaz/Documents/pop2.html"
        self.driver.get(location)
        button= self.driver.find_element_by_name('alert')
        button.click()
        obj = self.driver.switch_to.alert
        message = obj.text
        print("Alert shows following message: " + message)
        time.sleep(2)
        obj.accept()
        txt = self.driver.find_element_by_id('msg')
        print(txt.text)
        time.sleep(2)
        self.driver.refresh()
        button = self.driver.find_element_by_name('alert')
        button.click()
        time.sleep(2)
        obj = self.driver.switch_to.alert
        obj.dismiss()
        txt = self.driver.find_element_by_id('msg')
        print(txt.text)

    def test_promtbox(self):
        location = "file://C:/Users/shaminaz/Documents/pop3.html"
        self.driver.get(location)
        button = self.driver.find_element_by_name('prmp')
        button.click()
        obj = self.driver.switch_to.alert
        time.sleep(2)
        obj.send_keys('shaminaz')
        time.sleep(2)
        obj.accept()
        message = obj.text
        print("Alert shows following message: " + message)
        time.sleep(2)
        obj.accept()
        txt = self.driver.find_element_by_id('msg')
        print(txt.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
        unittest.main()
