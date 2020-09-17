# Vuex

Vuex 是一个专为 Vue.js 应用程序开发的状态管理模式。它采用集中式存储管理应用的所有组件的状态，并以相应的规则保证状态以一种可预测的方式发生变化。Vuex 也集成到 Vue 的官方调试工具 devtools extension，提供了诸如零配置的 time-travel 调试、状态快照导入导出等高级调试功能

## 1、单个逐渐数据流动  

![20200824154459](https://cdn.jsdelivr.net/gh/1134642046/ImageBed/JavaLearn/20200824154459.png)

## 2、多个组件共享状态

![20200824160158](https://cdn.jsdelivr.net/gh/1134642046/ImageBed/JavaLearn/20200824160158.png)

## 3、基本使用

Vuex 使用单一状态树——是的，用一个对象就包含了全部的应用层级状态。至此它便作为一个“唯一数据源 (SSOT)”而存在。这也意味着，每个应用仅包含一个 store 实例

### 1、State

存储共享的数据,创建一个Vuex的文件夹，创建index.js文件，如下获得一个Store对象

```js
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state:{
    num: 1
  }
})

export default store

```

在main.js中Vue实例中注册Store

```js
import store from './views/store/index'

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')

```

```html
<div>{{this.$store.state.num}}</div>
```

### 2、Getter

有时我们可能想要在多个组件中对同一个数据做一些过滤或者做一些计算，然后使用处理过的值，这时候我们可以在 store 中定义“getter”（可以认为是 store 的计算属性），当数据发生改变时进行一次计算.

首先在store的getters中创建一个getter

```js
const store = new Vuex.Store({
  state:{
    num: 1，
    profiles:[
        {
            name: "zhangsan",
            age: 12
        },
        {
            name: "lisi",
            age: 22
        },
        {
            name: "wangwu",
            age: 8
        }
    ]
  },
  getters: {
    //   过滤年龄在10岁及以上的用户
    filterProfile: state => state.profiles.filter(profile => profile.age >= 10)
  }
})
```

在组件的计算属性中使用`store.getters`对象调用该getter

```js
export default {
    data() {
        return {

        };
    },
    computed: {
      profiles(){
        return this.$store.getters.filterProfile
      }
    }
}
```

直接使用该计算属性

```html
<el-divider>Getters</el-divider>
<li v-for="value in profiles" :key="value.name">
    {{value.name}}
</li>
```

### 3、Mutation

对state中的数据想要进行一些改变，并让vuex记录该改变，可以使用Mutation

```js
 mutations:{
    increment(state){
        state.num++
    },
    // 传入一个对象，payload(载荷)
    reduce(state, payload){
        state.num -= payload.num
    }
}
```

在组件中使用`commit`来调用该函数

```js
methods: {
    increment(){
        this.$store.commit('increment')
    },
    reduce(){
        //无参
        // this.$store.commit('reduce')
        // 传入单个参数
        // this.$store.commit('reduce', 2)
        // 传入对象
        // this.$store.commit('reduce', {
        //   num: 2
        // })
        // 对象风格提交
        this.$store.commit({
          type:"reduce",
          num: 2
        })
    }
}
```

### 4、Action