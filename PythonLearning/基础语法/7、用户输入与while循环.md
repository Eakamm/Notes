# 用户输入与while循环


<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [用户输入与while循环](#用户输入与while循环)
  - [1、简单用户输入](#1-简单用户输入)
    - [1、input进行输入](#1-input进行输入)
    - [2、数字输入](#2-数字输入)
  - [2、while循环](#2-while循环)
    - [1、简单循环](#1-简单循环)
    - [3、break，continue跳出循环](#3-breakcontinue跳出循环)
  - [3、使用while循环来处理列表和字典](#3-使用while循环来处理列表和字典)
    - [1、删除包含特定值的所有列表元素](#1-删除包含特定值的所有列表元素)
    - [2、](#2)

<!-- /code_chunk_output -->

---

## 1、简单用户输入

函数input()让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python将其存储在一个变量中，以方便你使用。使用函数input()时，Python将用户输入解读为字符串。

### 1、input进行输入

```python {cmd}
message = input("hello:")

print(message)
```

### 2、数字输入

```python {cmd}
message = input("hello:")
message = (int)message
print(message)
```

## 2、while循环

### 1、简单循环

```python {cmd}
numbers = 10

while numbers >= 0:
  print(numbers)
  numbers-=1

```

### 3、break，continue跳出循环

```python {cmd}
numbers = 10

while 1:
  if numbers < 0:
    break
  if numbers % 2 == 0:
    numbers-=1
    continue
  else:
    print(numbers)
    numbers-=1
```

**注意：**
在任何Python循环中都可使用break语句。例如，可使用break语句来退出遍历列表或字典的for循环。

## 3、使用while循环来处理列表和字典

使用for循环列表的时候，不建议修改列表，因为修改会导致python无法跟踪元素，while是一个可以选择的方式

### 1、删除包含特定值的所有列表元素

首先创建了一个列表，其中包含多个值为`cat`的元素。打印这个列表后，Python进入while循环，因为它发现`cat`在列表中至少出现了一次。进入这个循环后，Python删除第一个`cat`并返回到while代码行，然后发现`cat`还包含在列表中，因此再次进入循环。它不断删除`cat`，直到这个值不再包含在列表中

```python {cmd}
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')  
print(pets)
```

### 2、

```python {cmd}

```

```python {cmd}

```

```python {cmd}

```

