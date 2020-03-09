from time import sleep

from selenium import webdriver

# 绑定浏览器
# driver = webdriver.Firefox()
driver = webdriver.Chrome()

# 输入 url
url = "file:///d:/python/PythonProject/reg.html"
driver.get(url)

# 找到class元素并填入值
driver.find_element_by_class_name("uname").send_keys("想你了")
driver.find_element_by_name("password").send_keys("有吃的吗")

sleep(5)

driver.quit()

