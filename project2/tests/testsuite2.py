from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from utils.browser_utils import BrowserUtils
from pages.home_page import HomePage
from components.flights import Flights

driver=BrowserUtils().openBrower()
BrowserUtils().invokeApp(driver)
HomePage().verifyHomepage(driver)
Flights().performSearchFlights(driver)
BrowserUtils().killBrowser(driver)








