# 1、`<label>`标签
* 参数：`for="..."`指定一个标签名称

鼠标点击`<label>`标签包裹的内容时，将跳转到标签内指定的名称的标签，例

```html
<label for="sex">
    <input type="radio" id="sex" v-model = "sex" value="男"/>男
</label>
<label for="sex2">
    <input type="radio" id="sex2" v-model = "sex" value="女"/>女
</label>
```
当点击男或女就会跳到相应的input标签

# 2、