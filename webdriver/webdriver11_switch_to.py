from time import sleep

from selenium import webdriver

# 初始化浏览器
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

# 设置浏览器窗口最大化
driver.maximize_window()

# 设置超时检测 30 秒
driver.implicitly_wait(30)

# 设置url
driver.get("d://python/PythonProject/reg.html")

# 点击按钮：点我有惊喜哦，并处理警示框
driver.find_element_by_id("button").click()
alert = driver.switch_to.alert
text = alert.text
print("警示框的内容是%s" % text)
# 关闭警示框
sleep(2)
# alert.accept()
alert.dismiss()
sleep(2)
# 输入用户名和密码
driver.find_element_by_id("uname").send_keys("admin")
driver.find_element_by_css_selector(".password").send_keys("123456")
sleep(2)

# 下拉框选择广州
select = Select(driver.find_element_by_tag_name("select"))
select.select_by_value("gz")

sleep(3)

driver.quit()

