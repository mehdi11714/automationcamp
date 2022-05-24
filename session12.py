from selenium import webdriver
from urllib3.util import timeout
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from datetime import datetime

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
actions = ActionChains(driver=driver)
driver.maximize_window()
driver.implicitly_wait(1)


# print(datetime.now())
# try:
#     driver.find_element(By.XPATH, "//*[text() = 'dfdfdddfdfd']")
# except:
# #    print(datetime.now())
# def wait_until_element_has_an_attribute(element_selector, element_locator, attribute, attribute_value, timeout=2,
#                                         exact=True):
#     for i in range(timeout * 5):
#         try:
#             element = driver.find_element(element_selector, element_locator)
#             if exact:
#                 assert element.get_attribute(attribute) == attribute_value
#             else:
#                 assert attribute_value in element.get_attribute(attribute)
#             return
#         except:
#             sleep(0.2)
#     raise Exception("Element attribute is not " + str(attribute))

#


# wait_until_element_has_an_attribute(By.ID, 'enabled_target', 'class', 'success', exact=False)
def wait_until_element_is_enabled(selector, locator,timeout):
    for i in range(timeout * 2):
        try:
            element = driver.find_element(By.ID, "enabled_target")
            assert element.is_enabled() == True
            return
        except:
            sleep(0.5)


driver.get("https://www.play1.automationcamp.ir/expected_conditions.html")
trigger = driver.find_element(By.ID, "enabled_trigger")
trigger.location_once_scrolled_into_view
trigger.click()
wait_until_element_is_enabled(By.ID, 'enabled_target',5)
print('enable')
