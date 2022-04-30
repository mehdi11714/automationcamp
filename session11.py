from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
actions = ActionChains(driver=driver)
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("https://material.angular.io/components/input/overview")
#sleep(2)
#el = driver.find_element(By.ID, 'mat-radio-2')
#attr1 = el.get_attribute('class')
#assert 'checked'  not in attr1
#el.click()
#attr2 = el.get_attribute('class')
#assert 'checked' in attr2
input =  driver.find_element(By.ID,'dsssd')
input.send_keys('salam')
input_value = input.get_attribute('value')
print(input_value)
assert input_value == 'salam'

