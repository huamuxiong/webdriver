from time import sleep

from selenium import webdriver

# 绑定浏览器
driver = webdriver.Chrome()

# 设置浏览器最大化
driver.maximize_window()

# 设置超时等待
driver.implicitly_wait(30)

# url
driver.get("d://python/PythonProject/reg.html")
# 获取当前窗口的句柄
current_window_handle = driver.current_window_handle

# 定位a链接并点击
driver.find_element_by_partial_link_text("百度").click()
# 点击后获取浏览器的所有窗口的句柄
window_handles = driver.window_handles

# 遍历所有的句柄，如果不和当前的句柄相同，就切换
for handle in window_handles:
    if handle != current_window_handle:
        # 切换窗口
        driver.switch_to.window(handle)
        driver.find_element_by_xpath('//*[@id="kw"]').send_keys("我是切换的窗口啊")
sleep(3)

driver.quit()

