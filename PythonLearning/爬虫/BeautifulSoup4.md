<!--
 * @Author: your name
 * @Date: 2020-02-11 11:19:04
 * @LastEditTime : 2020-02-11 23:48:28
 * @LastEditors  : Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \VueLearnc:\Users\11346\OneDrive\笔记\PythonLearning\爬虫\BeautifulSoup4.md
 -->

# BeautifulSoup4 模块


<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [BeautifulSoup4 模块](#beautifulsoup4-%e6%a8%a1%e5%9d%97)
  - [1、安装](#1%e5%ae%89%e8%a3%85)
    - [1、安装 BeautifulSoup4](#1%e5%ae%89%e8%a3%85-beautifulsoup4)
    - [2、安装解析器](#2%e5%ae%89%e8%a3%85%e8%a7%a3%e6%9e%90%e5%99%a8)
  - [2、简单使用](#2%e7%ae%80%e5%8d%95%e4%bd%bf%e7%94%a8)
  - [3、对象种类](#3%e5%af%b9%e8%b1%a1%e7%a7%8d%e7%b1%bb)
    - [1、Tag](#1tag)
    - [2、NavigableString](#2navigablestring)
    - [3、BeautifulSoup](#3beautifulsoup)
    - [4、Comment注释](#4comment%e6%b3%a8%e9%87%8a)
  - [4、](#4)

<!-- /code_chunk_output -->


## 1、安装

### 1、安装 BeautifulSoup4

```
pip install bs4
```

### 2、安装解析器

Beautiful Soup 支持 Python 标准库中的 HTML 解析器,还支持一些第三方的解析器，如下表：

| 解析器           | 使用方法                                                            | 优势                                                            | 劣势                                           |
| ---------------- | ------------------------------------------------------------------- | --------------------------------------------------------------- | ---------------------------------------------- |
| Python 标准库    | BeautifulSoup(markup, "html.parser")                                | Python 的内置标准库<br>执行速度适中<br>文档容错能力强           | Python 2.7.3 or 3.2.2)前的版本中文档容错能力差 |
| lxml HTML 解析器 | BeautifulSoup(markup, "lxml")                                       | 速度快<br>文档容错能力强                                        | 需要安装 C 语言库                              |
| lxml XML 解析器  | BeautifulSoup(markup, ["lxml-xml"])<br>BeautifulSoup(markup, "xml") | 速度快<br>唯一支持 XML 的解析器                                 | 需要安装 C 语言库                              |
| tml5lib          | BeautifulSoup(markup, "html5lib")                                   | 最好的容错性<br>以浏览器的方式解析文档<br>生成 HTML5 格式的文档 | 速度慢不依赖外部扩展                           |

## 2、简单使用

导入 BeautifulSoup 模块，通过使用 python 的标准库中的解析器

```python
import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.baidu.com")
r.encoding = "utf-8"

# 选用python的解析器，这里使用的是python的标准库中的解析器
soup = BeautifulSoup(r.text, "html.parser")
print (soup)
```

## 3、对象种类

Beautiful Soup 将复杂 HTML 文档转换成一个复杂的树形结构,每个节点都是 Python 对象,所有对象可以归纳为 4 种:`Tag` `NavigableString` , `BeautifulSoup` , `Comment` .

### 1、Tag

```python
print(soup.a.attrs)
print("soup.a的类型：")
print(type(soup.a))
```

tag 对象有两个重要属性：`names`,`Attrubtes`

**names**

```python {cmd}
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p id=\"lh\"> <a href=\"http://home.baidu.com\">关于百度</a> </p>","html.parser")
tag = soup.p
# 打印第一个p标签的字典内容
print(tag.attrs)
print("tag的名称：")
print(tag.name)
print("soup.p的类型：")
print(type(tag))
```

**Attrubtes**

tag的属性可以被添加,删除或修改. tag的属性操作方法与字典一样

```python {cmd}
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p id=\"lh\"> <a href=\"http://home.baidu.com\">关于百度</a> </p>","html.parser")
tag = soup.p
print("tag.attrs的类型：")
print(type(tag.attrs))

print("tag对象的属性：")
print(tag.attrs)

print("按照字典的方式获取其中的元素：")
print(tag.attrs['id'])
```

tag的属性可以被添加,删除或修改. tag的属性操作方法与字典一样

```python {cmd}
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p id=\"lh\"> hello </p>","html.parser")
tag = soup.p
# 修改tag的标签名
tag.name = "test"
print(tag.name)
# 删除tag的属性
print(tag.attrs)
del tag["id"]
print(tag.attrs)
```

Tag 有很多方法和属性,在 [遍历文档树](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#id18) 和 [搜索文档树](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#id27) 中有详细解释

### 2、NavigableString

用来表示标签内的内容，可以使用`replace_with()`方法替换内容

```python
print("获取a标签的内容:")
print(tag.string)
tag.string.replace_with("百度一下，你就不知道")
print("替换后的字符串：")
print(tag)
```

### 3、BeautifulSoup

```python

```

### 4、Comment注释

Comment 对象是一个特殊类型的 NavigableString 对象

```python
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup2 = BeautifulSoup(markup, "html.parser")
# b标签中的内容为注释，commment的类型被定为bs4.element.Comment
commment = soup2.b.string
print(type(comment))
```

## 4、

```python

```

```python

```

```python

```
