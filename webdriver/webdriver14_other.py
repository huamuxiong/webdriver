from time import sleep

from selenium import webdriver

# 绑定浏览器
# driver = webdriver.Firefox()
driver = webdriver.Chrome()

# 输入 url
url = "file:///d:/python/PythonProject/test_other.html"
driver.get(url)

size = driver.find_element_by_css_selector("#uname").size
print(size)

text = driver.find_element_by_css_selector("a").text
print(text)

title = driver.title
print(title)

current_url = driver.current_url
print(current_url)

get_attribute = driver.find_element_by_css_selector("a").get_attribute("href")
print(get_attribute)

is_display = driver.find_element_by_css_selector("span").is_displayed()
print(is_display)

is_enabled = driver.find_element_by_css_selector("button").is_enabled()
print(is_enabled)

sleep(5)

driver.quit()