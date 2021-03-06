# Filter

## 1、过滤器可以用在两个地方

  双花括号插值和 v-bind 表达式 (后者从 2.1.0+ 开始支持)。过滤器应该被添加在 JavaScript 表达式的尾部，由“管道”符号指示：

``` html
<!-- 在双花括号中 -->
{{ message | capitalize }}

<!-- 在 `v-bind` 中 -->
<div v-bind:id="rawId | formatId"></div>
```

  rawId的值将传入formatId过滤器.

  使用filtes属性定义过滤器，并返回处理结果

``` js
filters: {
  capitalize: function (value) {
    if (!value) return ''
    value = value.toString()
    return value.charAt(0).toUpperCase() + value.slice(1)
  }
}
```

## 2、使用多个过滤器

当使用多个过滤器的时候

``` html
<div :id="{{ message | filterA | filterB }}"></div>
```

按顺序执行messge, filterA的返回结果会传如filterB

## 3、传入参数

过滤器是 JavaScript 函数，因此可以接收参数：

``` html
{{ message | filterA('arg1', arg2) }}
```

`filter` 中传入三个参数，顺序是 `message、arg1、aarg2`

## Vue文档[Vue-filter](https://cn.vuejs.org/v2/guide/filters.html)


| 类型                             | 正则表达式                                | 部分验证的格式         |
| -----------------------------| -------------------------------------- | --------------------- |
| 整数                                         | ^-?\d+$                            |                       |
| 正浮点数                                   |  ^(([0-9]+\.[0-9]*[1-9][0-9]*)\|([0-9]*[1-9][0-9]*\.[0-9]+)\|([0-9]*[1-9][0-9]*))$/               |                   |
| 浮点数                                      |  /^(-?\d+)(\.\d+)?$/                                     |                         |
| 负浮点数                                   |  /^(-(([0-9]+\.[0-9]*[1-9][0-9]*)\|([0-9]*[1-9][0-9]*\.[0-9]+)\|([0-9]*[1-9][0-9]*)))$/          |           |
| 非正浮点数（负浮点数 + 0）               |  /^((-\d+(\.\d+)?)\|(0+(\.0+)?))$/                                          |                  |
| 非负浮点数（正浮点数 + 0）          | ^\d+(\.\d+)?$                                                                                  |                 |
| 验证Email地址           | /^([a-zA-Z0-9]+[_\|\_\|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_\|\_\|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/ |       |
| 验证InternetURL         | /^http://([\w-]+\.)+[\w-]+(/[\w-./?%&=]*)?$ ；^[a-zA-z]+://(w+(-w+)*)(.(w+(-w+)*))*(?S*)?$/     |  |
| 验证m-n位的数字                          | ^\d{m,n}$                                                                                |       |
| 验证n位的数字                            | ^\d{n}$                                                                                  |                     |
| 验证一个月的31天                        | ^((0?[1-9])\|((1\|2)[0-9])\|30\|31)$     | 正确格式为： 01、09和1、31。                           |
| 验证一年的12个月                        | ^(0?[1-9]\|1[0-2])$       | 正确格式为：“01”-“09”和“1”“12”                                     |
| 验证数字                                   | ^[0-9]*$                                                                               |                       |
| 验证是否含有 ^%&',;=?$\" 等字符       | [^%&',;=?$\x22]+                                                                               |    |
| 验证有1-3位小数的正实数              | ^[0-9]+(.[0-9]{1,3})?$                                                                         |         |
| 验证有两位小数的正实数              | ^[0-9]+(.[0-9]{2})?$                                                                           |     |
| 验证汉字                                   | ^[\u4e00-\u9fa5],{0,}$                                                                         |         |
| 验证用户密码                             | ^[a-zA-Z]\w{5,17}$           | 正确格式为：以字母开头，长度在6-18之间，只能包含字符、数字和下划线。  |
| 验证由26个大写英文字母组成的字符串 | ^[A-Z]+$                                                                                       |        |
| 验证由26个小写英文字母组成的字符串 | ^[a-z]+$                                                                                       |          |
| 验证由26个英文字母组成的字符串   | ^[A-Za-z]+$                                                                                    |       |
| 验证由数字、26个英文字母或者下划线组成的字符串 | ^\w+$                                                                                          |    |
| 验证由数字和26个英文字母组成的字符串 | ^[A-Za-z0-9]+$                                                                                 |           |
| 验证电话号码     | ^(\d3,4\d3,4\|\d{3,4}-)?\d{7,8}$    | 正确格式为： XXXX-XXXXXXX，XXXX-XXXXXXXX，XXX-XXXXXXX，XXX-XXXXXXXX，XXXXXXX，XXXXXXXX。  |
| 验证至少n位数字                         | ^\d{n,}$                                                                                  |         |
| 验证身份证号（15位或18位数字）    | ^\d{15}\|\d{}18$           |         |
| 验证长度为3的字符                      | ^.{3}$                                                                                         |              |
| 验证零和非零开头的数字              | /^(0\|[1-9][0-9]*)$/                                                                          |   |
| 验证非正整数（负整数 + 0）          |  ^((-\d+)\|(0+))$                                                                               |      |
| 验证非负整数（正整数 + 0）          |  ^\d+$                                                                                         |           |
| 验证非零的正整数                       | ^\+?[1-9][0-9]*$                                                                             |              |
| 验证非零的负整数                       | ^\-[1-9][0-9]*$                                                                                |          |