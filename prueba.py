from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randrange
import secrets

salario = randrange(100000000)
driver = webdriver.Safari()
driver.get("https://www.metrocuadrado.com/calculadora-credito-hipotecario-vivienda/")
driver.maximize_window()
element = driver.find_element_by_name("monthlyIncome")
element.send_keys(salario)
select = driver.find_element_by_xpath("//select[@ng-model='termInYears']")
# alert = driver.find_element_by_xpath('/html/body/div[12]/div/div/div/div/form/div[1]/div[2]/div/label[2]/input')
# alert.click()
options = [x for x in select.find_elements_by_tag_name("option")]
values = []
for elements in options:
    values.append(elements.get_attribute("text"))

print('valor al azar ' + secrets.choice(values))
for option in options:
    print('las opciones son: ' + option.get_attribute("text"))
select.click()
print('primer click')
select.click()
print('segundo click')
select.click()
print('tercer click')
select.click()
segundo_link = driver.find_elements_by_class_name("opcion_cuotas")
# driver.quit()
# scrrenshot = select.screenshot_as_png
# with open('canvas.png', 'wb') as f:
#     f.write(scrrenshot)
