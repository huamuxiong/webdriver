# 导包
from time import sleep

from selenium import webdriver

# 初始化浏览器
driver = webdriver.Chrome()

# 设置浏览器窗口做大化
driver.maximize_window()

# 设置url
url = "file:///d:/python/PythonProject/reg.html"
driver.get(url)

# 找到节点
driver.find_element_by_css_selector("#uname").send_keys("嘿嘿哈嘿")
driver.find_element_by_css_selector(".password").send_keys("嘿嘿哈嘿")

sleep(3)

driver.quit()
