<!--
 * @Author: your name
 * @Date: 2020-02-27 18:02:25
 * @LastEditTime: 2020-03-03 09:27:04
 * 1:21
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \VueLearnc:\Users\11346\OneDrive\笔记\PythonLearning\Python模块\Scrapy.md
 -->

# Scrapy爬虫框架

## 1、安装

## 2、使用

### 1、创建scrapy项目

创建命令：

```cmd
scrapy startproject [ProjectName]
```

该命令会在当前目录下创建一个scrapy项目，创建一个JingDong项目，目录结构为：
![20200228164020.png](https://cdn.jsdelivr.net/gh/1134642046/ImageBed/PythonLearn/20200228164020.png)

根目录下的文件是一些配置文件，spiders目录下存放的是你的爬虫代码

### 2、scrapy的代码框架

```python {cmd .line-numbers}
import scrapy

# 创建一个爬虫,继承与Spider类
class Demo(scrapy.Spider):
    # 爬虫名称，启动时候使用
    name = "demo"

    # 向网站发起请求
    def start_requests(self):
        # 需要爬取的页面
        urls = [
            'http://74.push2.eastmoney.com/api/qt/clist/get?pn=1&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=b:MK0201&fields=f2,f12,f14,f15,f16,f17,f18,f20',
            'https://www.laohu8.com/proxy/stock/stock_info/detail/'
        ]
        # 遍历请求网站
        for url in urls:
            if 'laohu' in url:
                    yield scrapy.Request(url=url+'HUYA', callback=self.parse)
            else:
                yield scrapy.Request(url=url, callback=self.parse)
    # 处理返回数据
    def parse(self, response):
        print(response.text)
```

使用命令行启动爬虫

```cmd
scrapy crawl demo
```

### 3、scrapy调试工具

有时候我们需要验证

```cmd
scrapy shell [url]
```

一执行这么一段代码scrapy就立马把我们相应链接的相应页面给拿到了，可以进行其他的操作了

### 4、css选择器

当进行分析页面的时候，需要对html的标签进行选择和处理，例如：`<title>爬虫实验室 - SCRAPY中文网提供</title>`

```python {cmd .line-numbers}
str = '<title>爬虫实验室 - SCRAPY中文网提供</title>'
    
```

### 4、

```python {cmd .line-numbers}

```

## 3、其他

## 4、坑

### 1、Robots协议

scrapy是默认遵守Robots协议的所以在爬取页面的时候会先查询该网站的根目录下的robots协议内容

```text
2020-02-28 13:31:22 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://74.push2.eastmoney.com/robots.txt> (referer: None)
2020-02-28 13:31:22 [scrapy.downloadermiddlewares.robotstxt] DEBUG: Forbidden by robots.txt: <GET http://74.push2.eastmoney.com/api/qt/clist/get?pn
=1&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=b:MK0201&fields=f2,f12,f14,f15,f16,f17,f18,f20>

```

所以提示`Forbidden by robots.txt`被Robots协议禁止

在settings.py中将`ROBOTSTXT_OBEY = True`改为False

### 2、
