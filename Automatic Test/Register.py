import time
import pytest
from selenium.webdriver.common.by import By
from BaseTest import BaseTest

test_data = [
    ("小李", "123456", "123456"),
    ("", "123456", "123456"),
    ("张三", "", "123456"),
    ("张三", "123456", "12345"),
    ("张三", "123456", "123456")
]

class TestReg(BaseTest):
    @pytest.mark.parametrize("username, password, confirmedPassword", test_data)
    def test_perform_register(self, username, password, confirmedPassword):
        self.driver.find_element(By.LINK_TEXT, "注册").click()
        self.wait_for_element(By.ID, "username").send_keys(username)
        self.wait_for_element(By.ID, "password").send_keys(password)
        self.wait_for_element(By.ID, "confirmedPassword").send_keys(confirmedPassword)
        self.driver.find_element(By.CSS_SELECTOR, "#app > div > div > div > div > div > form > button").click()
        time.sleep(2)
