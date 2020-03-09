from time import sleep

from selenium import webdriver

# driver = webdriver.Firefox()
driver = webdriver.Chrome()

url = "file:///d:/python/PythonProject/reg.html"
driver.get(url)
driver.find_element_by_name("uname").send_keys("想你了")
driver.find_element_by_name("password").send_keys("有吃的吗")

sleep(3)

driver.quit()
