import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseTest:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_class(self):
        self.driver.quit()

    def setup_method(self):
        self.driver.get("https://app2703.acapp.acwing.com.cn/user/account/login/")

    def wait_for_element(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def wait_for_element_clickable(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
