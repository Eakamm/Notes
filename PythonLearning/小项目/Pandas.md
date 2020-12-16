# Pandas

## 1、Servies

pandas创建一个一维数组

```python{cmd}
import pandas as pd
import numpy as np

s = pd.Series(['a', 'b', 'c'], index=[1, 2, 3])

# 获取索引序列
print(s.index)

# 根据索引查找数据
print(s[1])
s[1] = "e"
print(s[1])

print('----------------------------------')
# 多个索引或值查找
s2 = pd.Series([1, 2, 6], index=['a', 'b', 'c'])
# 自定义的索引('a', 'b', 'c')
print(s2[['a', 'b']])
# 第n行(0,1,2)
print(s2[[1, 2]])
# 值小于等于n
print(s2[s2 <= 3])

print('----------------------------------')
# in判断索引是否存在
print(1 in s)

```

通过`.index`改变索引

```python
# Series的索引可以通过按位置赋值的方式进行改变
s.index = ['a','b','c']
```

Python切片中是不包含尾部的，Series的自定义字符串索引的切片与之不同.

```python {cmd}
import pandas as pd
import numpy as np

# 字符串索引
s = pd.Series([1,2,3], index=['a', 'b', 'c'])
# 数字索引
s1 = pd.Series([1,2,3], index=[1, 2, 3])
s2 = [1,2,3]
print(s2[0:1])
# 根据行数做切片与普通数组的切片相同
print(s1[1:2])
# 自定义字符串索引包含尾部
print(s['a':'b'])

# 可以使用切片更改数据
s['a':'b'] = 4
print(s)
```

## 2、DataFrame

### 2.1、创建

最常用的方式是利用包含等长度列表或NumPy数组的字典来形成DataFrame(某一列没有赋值，会出现缺省值NaN)

```python {cmd}
import pandas as pd

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)

print(frame)
```

设置列名与行名，`debt`列为空，为NaN

```python
>>> frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
...                       index=['one', 'two', 'three', 'four',
...                              'five', 'six'])
>>> frame2
one    2000    Ohio  1.5  NaN
two    2001    Ohio  1.7  NaN
three  2002    Ohio  3.6  NaN
four   2001  Nevada  2.4  NaN
five   2002  Nevada  2.9  NaN
six    2003  Nevada  3.2  NaN
```

### 2.2、查找

`loc[]`获取某一行的数据

```python {cmd}
import pandas as pd

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)

# 查找某一行
print(frame)
print(frame.loc[1])

# 多个索引查找


# 创建新的一列
frame['test'] = frame.state == 'Ohio'
print(frame)
# 删除一列
del frame['test']
print(frame.columns)
```

### 2.3、根据布尔值切片

可以根据一个布尔值数组选择数据，也可以比较所有的元素，对符合要求的元素执行操作。

```python{cmd}
import pandas as pd
import numpy as np
frame = pd.DataFrame(np.arange(20).reshape(4, 5),
                      index=list('abcd'),
                      columns=list('abcde'))
# frame < 5
print(frame < 5)
# 将小于5的元素改为0
frame[frame < 5] = 0
print(frame)
# 根据列的比较结果显示数据
print(frame[frame['b'] > 10])

print(frame)
```

### 2.4、loc与iloc索引

标签选出单行多列的数据可以使用`loc`（也就是自定义的索引）

```python {cmd}
import numpy as np
import pandas as pd

frame = pd.DataFrame(np.arange(20).reshape(4, 5),
                      index=list('abcd'),
                      columns=list('abcde'))
# 获取某一行
print(frame.loc['a'])
# 获取某一行的n列数据
print(frame.loc['a',['a', 'b']])
# 
print(frame.loc[['a','b'],['a', 'b']])
```

整数标签`iloc`进行类似的数据选择

```python {cmd}
import numpy as np
import pandas as pd

frame = pd.DataFrame(np.arange(20).reshape(4, 5),
                      index=list('abcd'),
                      columns=list('abcde'))
print(frame.iloc[1])

print(frame.iloc[1,[1,2]])

print(frame.iloc[[1,2],[1,2]])
```

### 2.5、整数索引问题

```python
import numpy as np
import pandas as pd


```
当使用字符串的索引就不会对s[-1]产生歧义

所以你有一个包含整数的轴索引，数据选择时请始终使用标签索引。

### 2.6、广播机制

### 2.7、函数

使用`apply`可以取出每一行或每一列的元素。`axis = 'columns'`取出每一行，以行为索引。默认为列。
可以使用函数对数据进行更复杂的操作

```python {cmd}
import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(20).reshape(4, 5),
                  columns=list('abcde'))

# 求每组数据的最大最小值的差


def f(x): return x.max()-x.min()


# 默认为取出每列
series = df.apply(f)
print(series)

# 取出每行
series = df.apply(f, axis="columns")
print(series)
```

使用`applymap`取出每个元素

```python {cmd}
import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(20).reshape(4, 5),
                  columns=list('abcde'))
# 处理所有的元素
# 求平方
def f2(x): return x**2


data_frame = df.applymap(f2)
print(data_frame)

# 处理某一行
data_frame = df.loc[1].map(f2)
print(data_frame)
```