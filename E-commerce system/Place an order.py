from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time
import os
from test.login import fun_login3, fun_login4
from user_manager import user_manager

# 加载用户信息
user_info = user_manager.load_user_info()
if not user_info:
    # 如果没有找到注册用户，使用默认账号
    phone_number = "13445835176"
    password = "123456"
    goods_name = "kd2_7414"  # 默认商品名称
    print("未找到用户信息文件，使用默认设置")
else:
    phone_number = user_info.get('phone', "13445835176")
    password = user_info.get('password', "123456")
    goods_name = user_info.get('goods_name', "kd2_7414")  # 从用户信息中获取商品名称
    print(f"加载用户信息成功")

print(f"将要搜索的商品名称: {goods_name}")

# 设置截图保存路径为image文件夹
screenshot_dir = "image"

# 生成带时间戳的截图文件名，使用英文和数字避免编码问题
screenshot_filename = f"order_result_{int(time.time())}.png"
image_path = os.path.join(screenshot_dir, screenshot_filename)

driver = fun_login3("http://hmshop-test.itheima.net/")

try:
    # 等待并点击登录链接
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "登录"))
    ).click()

    # 填写登录信息
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    ).send_keys(phone_number)

    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "verify_code").send_keys("8888")
    driver.find_element(By.NAME, "sbtbutton").click()

    # 等待登录完成，确保搜索框出现
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "q"))
    )

    # 使用添加的商品名称进行搜索
    search_box = driver.find_element(By.ID, "q")
    search_box.clear()
    search_box.send_keys(goods_name)

    # 等待并点击搜索按钮
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "搜索"))
    ).click()

    # 等待搜索结果加载，然后点击"加入购物车"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "加入购物车"))
    ).click()

    # 等待并关闭提示框
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#layui-layer1 > span > a"))
    ).click()

    # 等待并点击购物车图标
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#hd-my-cart > a > div"))
    ).click()

    # 等待并点击"去结算"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "去结算"))
    ).click()

    # 等待并点击提交订单按钮
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "submit_order"))
        ).click()
    except ElementClickInterceptedException:

        submit_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "submit_order"))
        )
        driver.execute_script("arguments[0].click();", submit_button)

    # 等待并点击确认支付方式
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "确认支付方式"))
    ).click()

    # 打印当前页面信息
    print(f"支付完成页面标题: {driver.title}")
    print(f"支付完成页面URL: {driver.current_url}")

    # 等待并点击"我的订单"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "我的订单"))
    ).click()

    # 切换窗口信息
    # 等待新窗口出现
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    handles = driver.window_handles
    driver.switch_to.window(handles[1])

    # 等待新窗口页面加载完成
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    print(f"订单页面标题: {driver.title}")
    print(f"订单页面URL: {driver.current_url}")

    # 使用截图保存下单结果界面，保存到指定路径
    driver.get_screenshot_as_file(image_path)
    print(f"下单成功，商品名称: {goods_name}")
    print(f"截图已保存为: {image_path}")

except Exception as e:
    print(f"发生其他错误: {e}")
    # 即使发生错误也尝试保存截图以便调试
    error_screenshot = os.path.join(screenshot_dir, f"error_{int(time.time())}.png")
    try:
        driver.get_screenshot_as_file(error_screenshot)
        print(f"错误截图已保存为: {error_screenshot}")
    except:
        pass
    raise

finally:
    fun_login4(driver)
