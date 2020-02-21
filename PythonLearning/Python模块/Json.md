<!--
 * @Author: your name
 * @Date: 2020-02-17 10:33:21
 * @LastEditTime: 2020-02-17 10:33:21
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \VueLearnc:\Users\11346\OneDrive\笔记\PythonLearning\Python模块\Json.md
 -->

# Json 模块


<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Json 模块](#json-%e6%a8%a1%e5%9d%97)
  - [1、什么是 Json](#1%e4%bb%80%e4%b9%88%e6%98%af-json)
  - [2、json 简单使用](#2json-%e7%ae%80%e5%8d%95%e4%bd%bf%e7%94%a8)
    - [1、 使用 json.dump()和 json.load()](#1-%e4%bd%bf%e7%94%a8-jsondump%e5%92%8c-jsonload)
    - [2、 json.dumps()和 json.loads()](#2-jsondumps%e5%92%8c-jsonloads)
  - [3、注意](#3%e6%b3%a8%e6%84%8f)

<!-- /code_chunk_output -->


## 1、什么是 Json

[官方文档](https://docs.python.org/zh-cn/3/library/json.html#module-json)

**定义：** JSON(JavaScript Object Notation, JS 对象简谱) 是一种轻量级的数据交换格式。
**特点：** 简洁和清晰的层次结构使得 JSON 成为理想的数据交换语言。 易于人阅读和编写，同时也易于机器解析和生成，并有效地提升网络传输效率。

在 JS 语言中，一切都是对象。因此，任何支持的类型都可以通过 JSON 来表示，例如字符串、数字、对象、数组等。但是对象和数组是比较特殊且常用的两种类型：

- 对象表示为键值对
- 数据由逗号分隔
- 花括号保存对象
- 方括号保存数组

**序列化简单定义：** 变成 json 格式。定义：变成 json 格式。
**反序列化简单定义：** json 格式变其它

## 2、json 简单使用

### 1、 使用 json.dump()和 json.load()

函数`json.dump()`接受两个实参：

- 要存储的数据
- 可用于存储数据的文件对象

下面演示了如何使用`json.dump()`来存储数字列表：

```python {cmd .line-numbers}
import json

names = ['小王','小李','老王','老李']
file_name = '处理所需文件/names.txt'

with open(file_name,'w') as json_write:
  json.dump(names,json_write)
```

函数`json.load()`接受一个参数：

- 要读取的文件对象

```python {cmd .line-numbers}
import json

file_name = '处理所需文件/names.txt'
with open(file_name) as json_read:
  names2 = json.load(json_read)
  for name in names2:
    print(name)

```

### 2、 json.dumps()和 json.loads()

dumps()将 Python 对象转为 json 字符串，loads()反之。

```python {cmd .line-numbers}
import json

numbers = ['1','2','3']

numbers = json.dumps(numbers)
print(type(numbers))
print(numbers)
numbers = json.loads(numbers)
print(type(numbers))
print(numbers)
```

![20200113114532.png](https://cdn.jsdelivr.net/gh/1134642046/ImageBed/PythonLearn/20200113114532.png)

## 3、注意

- 两种语言之间数据类型的差异，用 json 交换。
- 外层必须是字典或列表这两个容器类数据类型。
- 必须是双引号（因为 java 等其它语言有使用双引号表示字符串，单引号不表示字符串）
- json 是字符串
- json 中不存在元组。序列化元组之后元组变列表；不能是集合，序列化集合报错。默认支持以下对象和类型：

| Python                              | JSON   |
| ----------------------------------- | ------ |
| dict                                | object |
| list, tuple                         | array  |
| str                                 | string |
| int, float, int 和 float 派生的枚举   | number |
| TRUE                                | TRUE   |
| FALSE                               | FALSE  |
| None                                | null   |

```python {cmd .line-numbers}
import json

numbers = （'1','2','3'）

numbers = json.dumps(numbers)
print(type(numbers))
print(numbers)
```

- 以后传值就是传一个也要用字典或列表
- 中文写入注意编码格式

```python {cmd .line-numbers}
with open('PythonModule/file/test.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)
```

因为`json.dump/dumps`序列化时对中文默认使用的`ascii`编码.想输出真正的中文需要指定`ensure_ascii=False`,例：

```python {cmd .line-numbers}
import json
data = {
  '国家':'中国'
}
print(json.dumps(data))

print(json.dumps(data, ensure_ascii=False))
```
