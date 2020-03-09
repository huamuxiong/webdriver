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

# 设置滚动条到最底下
js1 = "window.scrollTo(0, 10000)"
sleep(2)
driver.execute_script(js1)

# 设置滚动条到最上边
js2 = "window.scrollTo(0, 0)"
sleep(2)
driver.execute_script(js2)

sleep(2)

driver.quit()

