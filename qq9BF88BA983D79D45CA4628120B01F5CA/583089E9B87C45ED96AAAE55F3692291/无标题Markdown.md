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


