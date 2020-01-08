# if语句

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [if语句](#if%e8%af%ad%e5%8f%a5)
  - [1、基础写法](#1%e5%9f%ba%e7%a1%80%e5%86%99%e6%b3%95)
    - [1.1 if~else](#11-ifelse)
    - [1.2 elif](#12-elif)
    - [1.3 等值判断](#13-%e7%ad%89%e5%80%bc%e5%88%a4%e6%96%ad)
    - [1.4 检查特定的值](#14-%e6%a3%80%e6%9f%a5%e7%89%b9%e5%ae%9a%e7%9a%84%e5%80%bc)

<!-- /code_chunk_output -->


---

## 1、基础写法

### 1.1 if~else

注意`if,else`结尾的`：`

```python {cmd}
s = 'hell'
if s == 'hell':
  print('true')
else:
  print('false')
```

### 1.2 elif

```python {cmd}
age = 10
if age > 20:
  print(">20")
elif age > 10:
  print(">10")
else:
  print("10<=")
```

### 1.3 等值判断

等值判断区分大小写

```python {cmd}
s = 'hell'
print(s == 'Hell')
print(s != 'Hell')
```

可以使用`lower()`转换为小写再比较，使之不区分大小写,使用该函数后不会改变变量的值。

```python {cmd}
s = 'Hell'
print(s.lower() == 'hell')
print(s)
```

### 1.4 检查特定的值

```python {cmd}
list = list(range(1, 10))

if 1 in list:
# if 1 not in list:
  print("1 in list")
else:
  print("1 not in list")

```


