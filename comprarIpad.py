from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.keys import Keys
import json

with open("elements.json") as jsonFile:
    jsonObject = json.load(jsonFile)

driver = webdriver.Chrome(executable_path=r'./chromedriver')
#driver = webdriver.Chrome(executable_path=r'C:\Tools\webdrivers\chromedriver.exe')
driver.get("https://www.apple.com/br/")