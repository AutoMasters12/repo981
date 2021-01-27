from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
class Flights:
    def performSearchFlights(self,driver):
        driver.find_element_by_xpath("//input[@id='OneWay']").click()
        driver.find_element_by_xpath("//input[@id='FromTag']").send_keys("Bangalore, IN - Kempegowda International Airport (BLR)")
        driver.find_element_by_xpath("//input[@id='ToTag']").send_keys("Hyderabad, IN - Rajiv Gandhi International (HYD)")
        driver.find_element_by_xpath("//body/section[@id='Home']/div[1]/div[1]/div[1]/form[1]/div[4]/section[2]/div[1]/dl[1]/dd[1]/div[1]/a[1]/i[1]").click()
        driver.find_element_by_xpath("//body[1]/div[2]/div[1]/table[1]/tbody[1]/tr[4]/td[5]/a[1]").click()
        dd=Select(driver.find_element_by_xpath("//select[@id='Adults']"))
        dd.select_by_index(2)
        driver.find_element_by_xpath("//input[@id='SearchBtn']").click()
        time.sleep(10)
