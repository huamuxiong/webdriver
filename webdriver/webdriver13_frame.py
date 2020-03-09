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

driver.find_element_by_css_selector("#uname").send_keys("admin")
driver.find_element_by_css_selector("#password").send_keys("admin")

driver.switch_to.frame("myframeA")
driver.find_element_by_css_selector("#unameA").send_keys("aaa")
driver.find_element_by_css_selector("#passwordA").send_keys("bbb")

driver.switch_to.default_content()

driver.switch_to.frame("myframeB")
driver.find_element_by_css_selector("#unameB").send_keys("ccc")
driver.find_element_by_css_selector("#passwordB").send_keys("ddd")

driver.switch_to.default_content()
sleep(2)

driver.quit()

