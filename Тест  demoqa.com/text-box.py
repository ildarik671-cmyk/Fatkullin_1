import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get('https://demoqa.com/text-box')
input_username = driver.find_element("xpath", "//input[@id = 'userName']")
time.sleep(2)
input_username.send_keys('Регина')
assert input_username.get_attribute('value') == "Регина", "Ошибка ввода логина"
input_username.send_keys(Keys.TAB)
input_user_email = driver.find_element("xpath", "//input[@id = 'userEmail']")
time.sleep(2)
input_user_email.send_keys('luksus_il@mail.ru')
input_user_email.get_attribute('value') == "luksus_il@mail.ru", "Ошибка ввода email"
time.sleep(2)
input_user_email.send_keys(Keys.TAB)
curren_adress = driver.find_element("xpath", "//textarea[@id = 'currentAddress']")
curren_adress.send_keys("Sterlitamak, street Druchbi 29-105")
assert curren_adress.get_attribute('value') == "Sterlitamak, street Druchbi 29-105", "Ошибка ввода адреса"
time.sleep(2)
curren_adress.send_keys(Keys.TAB)
permanent_adress = driver.find_element("xpath", "//textarea[@id = 'permanentAddress']")
permanent_adress.send_keys("Sterlitamak,street Lenina 15 -48")
assert permanent_adress.get_attribute('value') == "Sterlitamak,street Lenina 15 -48", "Ошибка ввода постоянного адреса"
permanent_adress.send_keys(Keys.ENTER)
time.sleep(2)
button = driver.find_element("xpath", "//div/button[@type = 'button']")
button.click()
time.sleep(10)



