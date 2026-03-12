import time
from requests import options
from selenium import webdriver
# options = webdriver.ChromeOptions() # Опции
# options.add_argument("--headless=new")
# options.add_argument("--incognito")
# options.add.argument("--ignore-certificate-errors")
driver = webdriver.Chrome()
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome() #Иниц опций в драйвере (options=options)
driver.get('https://ekg:DOAronYZrd5eHrpLYr6ujU28@vmo-stage.moscow/meetings')
print(driver.title) # Просмотр заголовка
time.sleep(4) # Время для открытия страницы,иначе поля ввода не активны
input_login = driver.find_element("xpath", "//input[@id='login']")
input_login.clear()
input_login.send_keys('10001000005')
assert input_login.get_attribute('value') == "10001000005", "Ошибка при вводе логина"
time.sleep(1)
input_password = driver.find_element("xpath", "//input[@id='password']")
input_password.clear()
input_password.send_keys('sVF7BVRn25Z5Z42S')
time.sleep(1)
assert input_password.get_attribute('value') == "sVF7BVRn25Z5Z42S", "Ошибка при вводе пароля"
button_bind = driver.find_element("xpath", "//button[@id ='bind']")
button_bind.click()
time.sleep(1)
chapter_meeting = driver.find_element("xpath", "//span[text() = 'Заседание']")
chapter_meeting.click()
time.sleep(1)
completed_meeting = driver.find_element("xpath", "//span[text() = 'Завершены']")
completed_meeting.click()
time.sleep(1)
# completed_meeting2 = driver.find_element("xpath", "//h4[text()='ТЕСТ'] ")
# completed_meeting2.click()
driver.get('https://vmo-stage.moscow/meetings/ea2c0478-37ce-4089-b952-6c4c0fbea772/finish')
time.sleep(4)
download_file = driver.find_element("xpath", "//button[@type = 'button']/span[@class = 'ekg-btn-icon']/span[@aria-label = 'download']")
download_file.click()
time.sleep(1)
view_file = driver.find_element("xpath", "//span[@aria-label = 'eye']")
view_file.click()
time.sleep(1)
deputats_list = driver.find_element("xpath", "//svg[@data-icon = 'download']")
time.sleep(1)
download_file.click()

