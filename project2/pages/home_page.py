from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

class HomePage:
    def verifyHomepage(self,driver):
        if driver.find_element_by_xpath("//h1[contains(text(),'Search flights')]").is_displayed():
            print("i am into home ppage of app")
        else:
            assert 1==0,"i am anot into home page of application"