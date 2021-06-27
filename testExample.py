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
driver.find_element_by_css_selector(jsonObject['comprar']).click()

driver.find_element_by_css_selector(jsonObject['selecionarAparelho']).click()
driver.find_element_by_css_selector (jsonObject['selecionarCor']).click()
sleep(5)
driver.find_element_by_css_selector(jsonObject['selecionarCapacidade']).click()
sleep(5)
driver.find_element_by_css_selector(jsonObject['colocarSacola']).click()
sleep(5)
driver.find_element_by_css_selector(jsonObject['verSacola']).click()
#Pagar
sleep(5)
driver.find_element_by_css_selector(jsonObject['pagar']).click()
#Finalizar Convidade
sleep(5)
driver.find_element_by_css_selector('#signIn\.guestLogin\.guestLogin').click()

sleep(5)
cep = driver.find_element_by_css_selector('#recon-0-7')
cep.send_keys('05407-002')
driver.find_element_by_css_selector('#checkout-container > div > div.rs-checkout > div:nth-child(1) > div.rs-module-loader > div > div > div:nth-child(1) > div > div > div > div > div:nth-child(1) > div > div:nth-child(2) > div > div:nth-child(1) > div:nth-child(1) > div > div > button > span > span:nth-child(1)').click()

