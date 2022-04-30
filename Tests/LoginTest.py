from Pages.Login import Login
from Pages.MainPage import MainPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import unittest


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    def test_valid_login(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        login = Login(driver=self.driver)
        main_page = MainPage(driver=self.driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.click_on_login_button()
        main_page.check_main_page()
        sleep(1)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
