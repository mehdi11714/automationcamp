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
driver.get("https://www.play2.automationcamp.ir")
sleep(0.5)
# el = driver.find_element('xpath', "//button[text()='Double-click me']")
# sleep(2)
# actions.double_click(el)
# actions.perform()
# sleep(2)
# driver.find_element('xpath', "//*[text()='Your Sample Double Click worked!']")
# Right click///////////////////////////////////////////////////
# el1 = driver.find_element('id', 'fname')
# actions.context_click(el1)
# actions.perform()
# sleep(2)
# ///////////////////////////////////move to element
# el2 = driver.find_element('xpath', "//*[@class='tooltip']")
# actions.move_to_element(el2).perform()
# sleep(2)
# ///////////////////////////////////////////////////////////
# Click and Hold the mouse
# offset -move to element offset
offset = driver.find_element("xpath", "//*[text() ='Lets you select only one option']").location
###///// get cordinnate
driver.find_element('id', "option").click()
sleep(3)
actions.move_by_offset(offset["x"], offset["y"]).click().perform()
sleep(3)
