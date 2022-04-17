from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os
from pathlib import Path
from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_argument("--incognito")


# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get('https://yahoo.com')
sleep(2)
# driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
# sleep(2)
# current_path = Path(__file__).parent
# file_name = os.path.join(str(current_path) , 'session.png')

# driver.save_screenshot(file_name)


