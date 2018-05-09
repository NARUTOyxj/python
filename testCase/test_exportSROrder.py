# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from time import sleep
import unittest, time, re

class ExportSr(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'e:\\downloads'}
        options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(30)
        self.base_url = "http://scmpcapp.loongjoy.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_export_sr(self):
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url + "/#/user/login#zh")
        driver.find_element_by_link_text("English").click()
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("plat_yxj")
        driver.find_element_by_xpath("//input[@type='password']").send_keys("123456")
        driver.find_element_by_css_selector("button.submit.ng-scope").click()
        driver.find_element_by_css_selector("i.icon-finance").click()
        driver.find_element_by_xpath("(//a[contains(text(),'SR Report')])[2]").click()
        Select(driver.find_element_by_xpath("//body[@id='body']/div/div/div/div/div/div/div/div[2]/form/div[3]/div/select")).select_by_visible_text("Xiaomi")
        Select(driver.find_element_by_xpath("//body[@id='body']/div/div/div/div/div/div/div/div[2]/form/div[3]/div[2]/select")).select_by_visible_text("Phone")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(5)
        driver.find_element_by_link_text("Export Report").click()
        sleep(30)
        driver.close()
        # ERROR: Caught exception [ERROR: Unsupported command [waitForPopUp |  | 30000]]
    
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
