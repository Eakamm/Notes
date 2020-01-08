## 1、过滤器可以用在两个地方
  双花括号插值和 v-bind 表达式 (后者从 2.1.0+ 开始支持)。过滤器应该被添加在 JavaScript 表达式的尾部，由“管道”符号指示：

```html
<!-- 在双花括号中 -->
{{ message | capitalize }}

<!-- 在 `v-bind` 中 -->
<div v-bind:id="rawId | formatId"></div>
```
  rawId的值将传入formatId过滤器.

  使用filtes属性定义过滤器，并返回处理结果

```html
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
```html
<div :id="{{ message | filterA | filterB }}"></div>

```
按顺序执行messge,filterA的返回结果会传如filterB

## 3、传入参数
过滤器是 JavaScript 函数，因此可以接收参数：
```html
{{ message | filterA('arg1', arg2) }}
```
`filter`中传入三个参数，顺序是`message、arg1、aarg2`

## Vue文档[Vue-filter](https://cn.vuejs.org/v2/guide/filters.html)






