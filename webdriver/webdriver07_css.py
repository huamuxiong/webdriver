from time import sleep

from selenium import webdriver

# 初始化浏览器
driver = webdriver.Chrome()

# 打开url
url = "file:///D:/python/PythonProject/reg.html"
driver.get(url)

driver.find_element_by_css_selector("#uname").send_keys("嘿嘿哈嘿")
driver.find_element_by_css_selector(".password").send_keys("反反复复方法")

sleep(3)

driver.quit()
