# 1、双向数据绑定
## 1、介绍

## 2、实现
利用v-model将数据与标签的值绑定
```html
<!-- 实现双向数据绑定 -->
<input v-model="name">{{name}}</input>
```
## 3、原理
之前有一个v-bind可以将变量绑定到标签，但是标签数据改变无法改变变量。
但是我们可以利用v-on监听标签，当事件发生时在方法中改变变量值。
```html

<!-- 双向数据绑定原理 -->
<input type="text" :value = "test" @input="setName"/>
-------------------------------------------------
 methods:{
  setName(event){
    this.test = event.target.value;
  }
}
<!-- 或者 -->
<input type="text" :value = "test" @input="test = $event.target.value"/>
```

## 4、使用
### 1、配合`<input>`的radio属性
* 当两个`<input>`绑定相同的变量时会出现互斥,例如：
```html

```





