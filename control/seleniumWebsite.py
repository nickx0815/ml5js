import os
from selenium import webdriver


class seleniumWebsite:

    def open(self):
        filePath = os.path.dirname(os.path.dirname(__file__))
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        webdriverPosenet = webdriver.Chrome(chrome_options=options, executable_path=filePath + "\driver\chromedriver.exe")
        options.add_argument("--start-maximized")
        webdriverBrowser = webdriver.Chrome(chrome_options=options, executable_path=filePath + "\driver\chromedriver.exe")
        webdriverBrowser.get("https://www.google.de/")
        webdriverPosenet.get(filePath + '/website/index.html')
        return webdriverBrowser, webdriverPosenet

