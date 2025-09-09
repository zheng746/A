from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import random
from test.login import fun_login4, fun_login3
from user_manager import user_manager

# 生成随机商品名称
goods_name = f"kd2_{random.randint(0, 9999)}"
print(f"生成的商品名称: {goods_name}")

# 登录后台管理系统
driver = fun_login3("http://hmshop-test.itheima.net/index.php/Admin/Admin/login")

try:
    # 登录
    driver.find_element(By.NAME, "username").send_keys("test1")
    driver.find_element(By.NAME, "password").send_keys("123456")
    driver.find_element(By.ID, "vertify").send_keys("8888")

    # 等待并点击登录按钮
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "submit"))
    ).click()

    # 等待并点击商城链接
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "商城"))
    ).click()

    # 切换iframe窗口
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "workspace"))
    )
    driver.switch_to.frame(iframe)

    # 点击添加按钮
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "add"))
    ).click()

    # 填写商品信息
    driver.find_element(By.NAME, "goods_name").send_keys(goods_name)

    select = Select(driver.find_element(By.ID, "cat_id"))
    select.select_by_index(2)

    driver.find_element(By.NAME, "shop_price").send_keys("24")
    driver.find_element(By.NAME, "market_price").send_keys("44")

    # 选择是否包邮
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#is_free_shipping_label_1"))
    ).click()

    # 提交表单
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit"))
    ).click()

    print(f"商品添加成功，商品名称: {goods_name}")

    # 将商品名称保存到用户信息中
    user_info = user_manager.load_user_info()
    if user_info is None:
        user_info = {}
    user_info['goods_name'] = goods_name
    user_manager.current_user = user_info
    user_manager.save_user_info()
    print("商品名称已保存到用户信息文件")

finally:
    # 返回默认窗口
    try:
        driver.switch_to.default_content()
    except:
        pass
    fun_login4(driver)
