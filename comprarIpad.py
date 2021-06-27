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
sleep(3)
driver.find_element_by_css_selector(jsonObject['selecionarCapacidade']).click()
sleep(3)
driver.find_element_by_css_selector(jsonObject['colocarSacola']).click()
sleep(3)
driver.find_element_by_css_selector(jsonObject['verSacola']).click()
#Pagar
sleep(3)
driver.find_element_by_css_selector(jsonObject['pagar']).click()
#Finalizar Convidade
sleep(3)
driver.find_element_by_css_selector(jsonObject['continuarComoCovidado']).click()
sleep(3)
cep = driver.find_element_by_css_selector(jsonObject['cep'])
cep.send_keys('05407-002')
driver.find_element_by_css_selector(jsonObject['aplicarCEP']).click()

