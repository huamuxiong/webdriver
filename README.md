# webdriver
selenium_python 下存放的webdriver小知识

使用webdriver需要知道：  
&emsp;&emsp;Firefox浏览器50版本以上需要安装geckodriver  
&emsp;&emsp;Chrome版本要安装chromedriver
    
安装selenium： 默认安装最新版本   
`pip install selenium`  
如果需要安装指定版本，后边加==版本号  
`pip install selenium==2.22.22`  

使用webdriver，首先要导包：  
`from selenium import webdriver`  
**初始化浏览器:以Chrome为例**  
`driver = webdriver.Chrome()`  

## 获取元素或属性
  
**四个基本方法：id,class,name,tag**  
 
现有html代码如下：  
`<input type="text" id="uname" name="uname" class="uname"/>`  
  
获取到input，并填入值：send_keys()  
`driver.find_element_by_id("uname").send_keys("zhangsan")`  
`driver.find_element_by_class_name("uname").send_keys("zhangsan")`  
`driver.find_element_by_name("uname").send_keys("zhangsan")`
`driver.find_element_by_tag_name("input").send_keys("zhangsan")`

