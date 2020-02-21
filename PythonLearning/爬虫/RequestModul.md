<!--
 * @Author: your name
 * @Date: 2020-01-31 09:49:27
 * @LastEditTime : 2020-02-11 10:54:54
 * @LastEditors  : Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \VueLearnc:\Users\11346\OneDrive\笔记\PythonLearning\爬虫\RequestModul.md
 -->

# Request 模块

- [Request 模块](#request-%e6%a8%a1%e5%9d%97)
  - [1、安装](#1%e5%ae%89%e8%a3%85)
  - [2、简单使用](#2%e7%ae%80%e5%8d%95%e4%bd%bf%e7%94%a8)
    - [1、导入模块](#1%e5%af%bc%e5%85%a5%e6%a8%a1%e5%9d%97)
    - [2、编码问题](#2%e7%bc%96%e7%a0%81%e9%97%ae%e9%a2%98)
    - [3、开发接口](#3%e5%bc%80%e5%8f%91%e6%8e%a5%e5%8f%a3)
      - [1、request 方法](#1request-%e6%96%b9%e6%b3%95)
    - [4、异常](#4%e5%bc%82%e5%b8%b8)
    - [5、主要方法](#5%e4%b8%bb%e8%a6%81%e6%96%b9%e6%b3%95)

## 1、安装

使用 pip 安装

```cmd
pip install requests
```

[request 官方文档](https://requests.readthedocs.io/zh_CN/latest/)

## 2、简单使用

### 1、导入模块

`import`导入 request 模块，使用`get()`方法获取百度的网页

```python {cmd}
import requests

# get方法向百度发起get请求，返回response对象
r = requests.get("http://www.baidu.com")
# 设置编码格式为utf-8,格式是从HTTP的headers中判断而来，
# 没有设置编码格式，默认为ISO-8859-1
r.encoding = "utf-8"
print(r.text)
```

### 2、编码问题

requests 会根据请求头中的 charset 来猜测网页解码方式，默认的格式为 ISO-8859-1，如上面的例子，如果不通过`r.encoding`设置会出现中文乱码。

**response 的 headers**
![20200131113238.png](https://cdn.jsdelivr.net/gh/1134642046/ImageBed/PythonLearn/20200131113238.png)

因为百度的 response 中没有在 charset 中定义编码格式，所以
![20200131113454.png](https://cdn.jsdelivr.net/gh/1134642046/ImageBed/PythonLearn/20200131113454.png)

而在访问 xiaomi 的官网的时候明确定义了编码格式

```python
import requests

r = requests.get(" https://www.mi.com")
print(r.encoding)
print(r.headers['Content-Type'])
```

![20200131114609.png](https://cdn.jsdelivr.net/gh/1134642046/ImageBed/PythonLearn/20200131114609.png)

### 3、开发接口

[官方文档](https://requests.readthedocs.io/zh_CN/latest/api.html)

#### 1、request 方法

```python {cmd}

```

```python {cmd}

```

### 4、异常

```python {cmd}
import requests

try:
    r = requests.get(" https://www.mi.com")
except requests.ConnectionError:
    print("连接错误")
else:
    print(r.text)
```

### 5、主要方法

```python {cmd}

```

```python {cmd}

```

```python {cmd}

```

```python {cmd}

```

```python {cmd}

```
