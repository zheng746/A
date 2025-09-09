import time
from selenium.webdriver.common.by import By
from BaseTest import BaseTest


class TestBattleTable(BaseTest):
    def test_battle_table_navigation(self):
        # 登录
        self.driver.find_element(By.ID, "username").send_keys("小李")
        self.driver.find_element(By.ID, "password").send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR, "#app > div > div > div > div > div > form > button").click()
        time.sleep(2)

        # 导航到对局列表
        self.driver.find_element(By.LINK_TEXT, "对局列表").click()
        time.sleep(2)

        # 测试分页功能
        self.wait_for_element_clickable(By.LINK_TEXT, "后一页").click()
        time.sleep(2)
        self.wait_for_element_clickable(By.LINK_TEXT, "前一页").click()
        time.sleep(2)

        # 查看录像
        self.wait_for_element_clickable(
            By.XPATH, "(//button[text()='查看录像'])[3]"
        ).click()
        time.sleep(5)
