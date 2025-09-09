import datetime
import time
from selenium.webdriver.common.by import By
from BaseTest import BaseTest


class TestBot(BaseTest):
    def test_bot_operations(self):
        # 登录
        self.driver.find_element(By.ID, "username").send_keys("小李")
        self.driver.find_element(By.ID, "password").send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR, "#app > div > div > div > div > div > form > button").click()
        time.sleep(2)

        # 导航到Bot管理页面
        self.wait_for_element_clickable(By.ID, "navbarDropdown").click()
        self.wait_for_element_clickable(By.LINK_TEXT, "我的Bot").click()
        time.sleep(2)

        # 创建Bot
        self.wait_for_element_clickable(
            By.CSS_SELECTOR,
            "button.btn.btn-primary.float-end"
        ).click()
        time.sleep(2)

        timestamp = datetime.datetime.now().strftime("%H%M%S")
        self.wait_for_element(By.CSS_SELECTOR, "#add-bot-title").send_keys("A" + timestamp)
        ace_input = self.wait_for_element(By.CLASS_NAME, "ace_text-input")
        ace_input.send_keys("123")
        self.wait_for_element(By.XPATH, "//button[text()='创建']").click()
        time.sleep(5)

        # 删除Bot
        self.wait_for_element(By.XPATH, "(//button[text()='删除'])[1]").click()
        time.sleep(2)
