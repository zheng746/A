from pygame.display import get_driver
import time
import random
from selenium.webdriver.common.by import By
from test.login import fun_login3, fun_login4
from user_manager import user_manager

# 生成随机手机号
random_phone = user_manager.generate_random_phone()

driver = fun_login3("http://hmshop-test.itheima.net/Home/user/reg.html")

# 使用生成的手机号注册
driver.find_element(By.CSS_SELECTOR, "#username").send_keys(random_phone)

driver.find_element(By.CSS_SELECTOR,"#reg_form2 > div > div > div > div:nth-child(2) > div.liner > input").send_keys("8888")

driver.find_element(By.CSS_SELECTOR,"#password").send_keys("123456")

driver.find_element(By.CSS_SELECTOR,"#password2").send_keys("123456")

driver.find_element(By.CSS_SELECTOR,"#reg_form2 > div > div > div > div:nth-child(5) > div > input").send_keys("")

time.sleep(3)

driver.find_element(By.CSS_SELECTOR,"#reg_form2 > div > div > div > div.line.liney.clearfix > div > a").click()

# 保存用户信息
user_manager.save_user_info()

fun_login4(driver)
