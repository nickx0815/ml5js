import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


filePath = os.path.dirname(os.path.dirname(__file__ ))
sys.path.insert(0,filePath+'server\\chromedriver')
driver = webdriver.Chrome()
driver.get(filePath+'/website/index.html')