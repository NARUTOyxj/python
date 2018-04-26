# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://scmpcapp.loongjoy.com/#/user/login#en")
        selenium.setSpeed("10000")
        driver.maximize_window()
        driver.find_element_by_xpath("//input[@type='text']").click()
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("plat_yxj")
        driver.find_element_by_xpath("//body[@id='body']/div/div/div[2]/div[2]").click()
        driver.find_element_by_xpath("//input[@type='password']").click()
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys("123456")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.implicitly_wait(30)
        driver.find_element_by_link_text("Finance").click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("(//a[contains(text(),'SR Report')])[2]").click()
        driver.find_element_by_xpath("//body[@id='body']/div/div/div/div/div/div/div/div[2]/form/div[3]/div/select").click()
        driver.implicitly_wait(30)
        Select(driver.find_element_by_xpath("//body[@id='body']/div/div/div/div/div/div/div/div[2]/form/div[3]/div/select")).select_by_visible_text("Xiaomi")
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("//option[@value='3']").click()
        driver.find_element_by_xpath("//body[@id='body']/div/div/div/div/div/div/div/div[2]/form/div[3]/div[2]/select").click()
        driver.implicitly_wait(30)
        Select(driver.find_element_by_xpath("//body[@id='body']/div/div/div/div/div/div/div/div[2]/form/div[3]/div[2]/select")).select_by_visible_text("Phone")
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("//option[@value='phone']").click()
        driver.find_element_by_xpath("//body[@id='body']/div/div/div/div/div/div/div/div[2]/form/div[3]/div[5]/select").click()
        driver.implicitly_wait(30)
        Select(driver.find_element_by_xpath("//body[@id='body']/div/div/div/div/div/div/div/div[2]/form/div[3]/div[5]/select")).select_by_visible_text("Create Time")
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("(//option[@value='1'])[3]").click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("//input[@type='text']").click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.implicitly_wait(50)
        driver.find_element_by_link_text("Export Report").click()
        # sel.selectWindow(sel.getAllWindowTitles()[1])
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
        driver.close()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_local | ]]
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
