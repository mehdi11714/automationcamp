from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
actions = ActionChains(driver=driver)
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("https://www.imdb.com/chart/top/")
sleep(2)
# element = driver.find_element('link text', 'The Wizard of Oz')
# driver.execute_script("arguments[0].scrollIntoView();", element)
# sleep(2)

driver.execute_script('window.scrollBy(0 , document.body.scrollHeight)')
sleep(2)