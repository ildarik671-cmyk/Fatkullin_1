import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://demoqa.com/upload-download')
download_field = driver.find_element("xpath", "//input[@id = 'uploadFile']")
download_field.send_keys(r"D:\PycharmProjects\Fatkullin\PEP 8")
time.sleep(20)


