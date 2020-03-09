from selenium import webdriver
from time import sleep
# 实例化浏览器
# driver = webdriver.Firefox()
driver = webdriver.Chrome()
# 打开url
url = "file:///D:/python/PythonProject/reg.html"
# url = r"D:/python/PythonProject/reg.html"
driver.get(url)
# 找到元素
uname = driver.find_element_by_id("uname")
# 填入值
uname.send_keys("想你了")

pwd = driver.find_element_by_id("password")
pwd.send_keys("是真的")

sleep(3)

# 退出
driver.quit()

