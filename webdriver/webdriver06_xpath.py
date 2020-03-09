from time import sleep

from selenium import webdriver

# 绑定浏览器
# driver = webdriver.Firefox()
driver = webdriver.Chrome()

# 输入 url
url = "file:///d:/python/PythonProject/reg.html"
driver.get(url)

# 相对路径
# driver.find_element_by_xpath('//*[@id="uname"]').send_keys("嘿嘿哈嘿")
# 绝对路径
driver.find_element_by_xpath('/html/body/div[1]/div[1]/input').send_keys("嘿嘿哈嘿")


sleep(5)

driver.quit()
