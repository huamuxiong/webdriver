from time import sleep

from selenium import webdriver

# 绑定浏览器
# driver = webdriver.Firefox()
driver = webdriver.Chrome()

# 输入 url
url = "file:///d:/python/PythonProject/reg.html"
driver.get(url)

sleep(5)

'''
找到class元素并填入值
find_element_by_link_text的值是链接的全部内容，否则会报错
如果想要模糊查找，用另一个find_element_by_partial_link_text
'''

driver.find_element_by_link_text("访问 百度 链接").click()
# driver.find_element_by_partial_link_text("百度").click()
sleep(5)

driver.quit()
