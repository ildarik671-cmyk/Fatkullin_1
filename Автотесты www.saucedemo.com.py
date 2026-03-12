import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com')
input_log_field = driver.find_element( "xpath", "// input[@id ='user-name']")
input_log_field.clear()
time.sleep(3)
input_log_field.send_keys("standard_user")
time.sleep(2)
assert input_log_field.get_attribute("value") == "standard_user", "Ошибка данных логина"
input_pass_field = driver.find_element( "xpath", "//input[@id='password']")
input_pass_field.clear()
input_pass_field.send_keys("secret_sauce")
time.sleep(2)
assert input_pass_field.get_attribute("value") == "secret_sauce", "Ошибка данных пароля"
action_filed = driver.find_element ("xpath", "// input[@class ='submit-button btn_action']")
action_filed.send_keys(Keys.ENTER)
driver.get('https://www.saucedemo.com/inventory.html')
time.sleep(1)