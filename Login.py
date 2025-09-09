import time
import pytest
from selenium.webdriver.common.by import By
from BaseTest import BaseTest

# 修正测试数据，添加预期结果
test_data = [
    ("", "123456", False),
    ("张三", "12345", False),
    ("张三", "123456", False),
    ("小李", "123456", True)
]

class TestLogin(BaseTest):
    @pytest.mark.parametrize("username, password, should_succeed", test_data)
    def test_perform_login(self, username, password, should_succeed):
        self.wait_for_element(By.ID, "username").send_keys(username)
        self.wait_for_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/form/button").click()
        time.sleep(2)

        current_url = self.driver.current_url

        if should_succeed:
            # 添加断言：成功登录应跳转页面
            assert "login" not in current_url
            print(f"✅ 登录成功 - 用户名: {username}, 密码: {password}")
        else:
            # 添加断言：失败登录应仍在登录页面
            assert "login" in current_url
            print(f"❌ 登录失败（预期） - 用户名: {username}, 密码: {password}")
