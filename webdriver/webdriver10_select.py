# 导包
from time import sleep

from selenium import webdriver

from selenium.webdriver.support.select import Select

# 初始化浏览器
driver = webdriver.Chrome()

# 设置超时等待30秒
driver.implicitly_wait(30)

# 设置浏览器窗口做大化
driver.maximize_window()

# 设置url
url = "file:///d:/python/PythonProject/reg.html"
driver.get(url)

# 找到节点
webelement = driver.find_element_by_tag_name("select")
select = Select(webelement)   # webelement:tag_name
select.select_by_value("sh")
sleep(2)
select.select_by_visible_text("福建")
sleep(2)
select.select_by_value("gz")


sleep(3)

driver.quit()
