
cep = driver.find_element_by_css_selector(jsonObject['cep'])
cep.send_keys('05407-002')
driver.find_element_by_css_selector(jsonObject['aplicarCEP']).click()

