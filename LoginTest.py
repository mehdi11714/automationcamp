from Login import Login
from MainPage import MainPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.implicitly_wait(3)
login = Login(driver=driver)
main_page = MainPage(driver=driver)
login.enter_username('Admin')
login.enter_password('admin123')
login.click_on_login_button()
main_page.check_main_page()
sleep(1)

