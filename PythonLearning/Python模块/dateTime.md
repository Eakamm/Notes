<!--
 * @Author: your name
 * @Date: 2020-01-16 22:09:17
 * @LastEditTime : 2020-01-16 22:33:03
 * @LastEditors  : Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \VueLearnc:\Users\11346\OneDrive\笔记\PythonLearning\Python模块\dateTime.md
 -->

# datetime 模块

## 1、使用

```python {cmd}
from datetime import datetime


time = datetime.strptime('2017-1-23', '%Y-%M-%d')
print(time)
```

我们首先导入了模块 datetime 中的 datetime 类，然后调用方法 strptime()

- 第一个实参为日期的字符串。
- 第二个实参告诉 Python 如何设置日期的格式。

在这个示例中，'%Y-'让 Python 将字符串中第一个连字符前面的部分视为四位的年份；'%m-'让 Python 将第二个连字符前面的部分视为表示月份的数字；而'%d'让 Python 将字符串的最后一部分视为月份中的一天（1 ～ 31）。

还有其他的参数：

![20200116221049.png](https://cdn.jsdelivr.net/gh/1134642046/ImageBed/PythonLearn/20200116221049.png)
