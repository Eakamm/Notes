## 1、for循环
```js
  totalPrice(){
        let total = 0;
        //1、普通for循环
        for (let index = 0; index < this.list.length; index++) {
          total += this.list[index].price*this.list[index].count;
        }
        //2、in
        for (const key in this.list) {
          total += this.list[key].price*this.list[key].count;
        }
        // //3、of
        for (const iterator of this.list) {
          total += iterator.price*iterator.count;
        }
        return total;
  }
```

---

## 2、数组函数

### 1、filter过滤元素
* 传入参数为n，即数组中的每个元素，相当于遍历数组，当返回值为true，代表留下元素，false反之
* 返回值：过滤后的新数组
```js
let newNums = this.nums.filter(function(n){
    return n<100;
})
```

### 2、map遍历替换
* 传入参数n，即数组中的每个元素，相当于自动遍历数组，将该返回值替换原来的元素
* 返回值：替换后的数组
```js
let newNums2 = newNums.map(function(n){
    return n*2;
})
```

### 3、reduce数据汇总
* 传入参数（previousValue，n），previousVlaue为上一个元素，n为当前元素，函数计算结果作为下一次函数的previousValue值。（初始previousValue值可以在reduce中设置）
* 返回值：汇总结果
```js
let newNums3 = newNums2.reduce(function(proviousValue, n){
  return proviousValue+n;
  //初始previousValue
},0)
```
---

## 3、箭头函数

```js
let newNums3 = this.nums.filter(n => n < 100).map(n => n*2).reduce((proviousValue, n) => proviousValue+n,0);
```




