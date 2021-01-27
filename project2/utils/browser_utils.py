from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

class BrowserUtils:
    def openBrower(self):
        path="C:\\Users\\ADMIN\\Desktop\\red\\workspace0123456\\project2\\drivers\\chromedriver.exe"
        driver=webdriver.Chrome(executable_path=path)
        return driver
    
    def invokeApp(self,driver):
        driver.maximize_window()
        driver.get("https://www.cleartrip.com/")
        
    def killBrowser(self,driver):
        driver.quit()