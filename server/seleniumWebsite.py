import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class seleniumWebsite:
    def open(self):
        filePath = os.path.dirname(os.path.dirname(__file__))
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options=options, executable_path=filePath + "\server\chromedriver.exe")
        driver.get(filePath + '/website/index.html')
