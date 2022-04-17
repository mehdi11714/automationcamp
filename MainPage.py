class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard_lable_id = 'menu_dashboard_index'

    def check_main_page(self):
        self.driver.find_element('id', self.dashboard_lable_id)

