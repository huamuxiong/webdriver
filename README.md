# webdriver
selenium_python 下存放的webdriver小知识

使用webdriver需要知道：  
&emsp;&emsp;Firefox浏览器50版本以上需要安装geckodriver  
&emsp;&emsp;Chrome版本要安装chromedriver
    
安装selenium： 默认安装最新版本   

```python
pip install selenium
```

如果需要安装指定版本，后边加==版本号  

```
pip install selenium==2.22.22
```

使用webdriver，首先要导包：  

```python
from selenium import webdriver
```

**初始化浏览器:以Chrome为例**  

```python
driver = webdriver.Chrome()
```

打开要访问的地址

```python
url = "http://www.baidu.com"
driver.get(url)
或
driver.get("http://www.baidu.com")
'''
如果是本地文件
Chrome: url="d://pythonproject/reg.html"
Firefox: url="file:///d:/pythonproject/reg.html"
'''
```

## 定位元素或属性的位置

### **四个基本方法：id,class,name,tag**  

现有html代码如下：  

```html
<input type="text" id="uname" name="uname" class="uname"/>
```

获取到input，并填入值：send_keys()  

```python
driver.find_element_by_id("uname").send_keys("zhangsan")
driver.find_element_by_class_name("uname").send_keys("zhangsan")  
driver.find_element_by_name("uname").send_keys("zhangsan")
driver.find_element_by_tag_name("input").send_keys("zhangsan")
```

###### 获取超链接：a

现有html如下：

```html
<a href="https://www.baidu.com"> 点我 百度 链接</a>
```

获取链接有单独的方法：

link_text：链接的内容（全部，就算是空格也不能省略）

partial_link_text：链接的内容（可全部，可部分）

```python
driver.find_element_by_link_text(" 访问 百度 链接").click()
driver.find_element_by_partial_link_text("百度").click()
```

### 通过xpath或css来定位

##### 通过xpath定位

如果是Chrome浏览器，在开发者模式下，选中要定位的代码，右键选择复制xpath即可

如百度的搜索栏代码如下：

```html
<input type="text" class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off">
```

选择复制有两种，一种是简介版的，一种是完整版的，分别如下：

```python
//*[@id="kw"]
/html/body/div[1]/div[1]/div[5]/div[2]/div/form/span[1]/input

driver.find_element_by_xpath('//*[@id="kw"]')
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[5]/div[2]/div/form/span[1]/input')
```

注意：

1、绝对路径以单斜杠开头

2、相对路径以双斜杠抬头，并后边跟标签名或*

3、属性前边一定有@

更多的使用方法可以百度或参考下边的链接

https://blog.csdn.net/geek_xiong/article/details/104759062

##### 通过css来定位

方法同xpath

不过有时也不是很准啊

html代码如下：

```html
<input type="text" id="uname" name="uname" class="uname"/>
```

通过css来定位input

```python
driver.find_element_by_css_selector("#uname")  # id
driver.find_element_by_css_selector(".uname")  # class
driver.find_element_by_css_selector("input")   # tag
```

其他可参考以下的链接：

https://blog.csdn.net/weixin_30607029/article/details/98355380

### 浏览器的一些常用操作

浏览器最大化

```python
driver.maximize_window()
```

自定义浏览器的大小

```python
driver.set_window_size(width, height)  # 像素
```

设置浏览器的位置

```python
driver.set_window_postion(x, y)
```

后退

```python
driver.back()
```

前进

```python
driver.forward()
```

刷新

```python
driver.refresh()
```

关闭当前浏览器窗口

```python
driver.close()
```

关闭浏览器

```python
driver.quit()
```

### webdriver的其他方法

获取元素的大小  ： size

获取元素的文本内容  ：text

获取页面的标题  ：title

获取当前页面的地址url  ：current_url

获取某个属性的值  :  get_attribute("属性")

判断元素是否可用 ： is_enabled()

判断元素是否可见：is_display()

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>这里测试webdriver其他常用方法</title>
</head>
<body>
<input type="text" id="uname">
<a href="https://www.baidu.com">百度链接</a>
<button disabled>我是按钮</button>  <!-- disabled:不可用，默认可用 -->
<span hidden>我是隐藏的内容</span>   <!-- hidden:隐藏，默认显示 -->
</body>
</html>
```

```python
size = driver.find_element_by_css_selector("#uname").size
# {'height': 21, 'width': 173}

text = driver.find_element_by_css_selector("a").text
# 百度链接

title = driver.title
# 这里测试webdriver其他常用方法

current_url = driver.current_url
# file:///D:/python/PythonProject/test_other.html

get_attribute = driver.find_element_by_css_selector("a").get_attribute("href")
# https://www.baidu.com/

is_display = driver.find_element_by_css_selector("span").is_displayed()
# False

is_enabled = driver.find_element_by_css_selector("button").is_enabled()
# False
```

### 隐式超时等待

如果定位某一元素失败，就会触发隐式等待的有效时长，如果指定时间内加载完毕，则继续执行，否则抛出NoSuchElementException异常，如果在第一时间内就定位到元素，则不触发隐式等待时长

```python
driver.implicitly_wait(30)  # 秒
```











