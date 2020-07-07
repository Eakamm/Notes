<!--
 * @Author: your name
 * @Date: 2020-04-11 12:15:52
 * @LastEditTime: 2020-04-14 15:09:10
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \VueLearn\6、vue-cli.md
 -->

# Vue-Cli

## 1、起步

### 1、安装

全局安装

```js
npm install -g @vue/cli
```

### 2、创建项目

```cmd
npm create [ProjectName]
```

![20200411125231](https://cdn.jsdelivr.net/gh/1134642046/ImageBed/PythonLearn/20200411125231.png)

### 3、runtimeOnly 与 runtimeCompiler

```js
```

## 2、router 路由

### 1、路由简单使用

配置路由的映射表,目录位置：
![20200413162000](https://cdn.jsdelivr.net/gh/1134642046/ImageBed/VueLearn/20200413162000.png)

```js
const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    // 页面的路由地址
    path: "/about",
    // 名称
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    // 使用的组件
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
  {
    path: "/me",
    name: "Me",
    component: Me,
  },
];
```

创建一个vue对象，放入一个路由的映射表，通过import导入之前的路由映射表

```js
import Vue from 'vue'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false

new Vue({
	// 路由
  router,
	// 渲染网站的第一个页面
  render: h => h(App)
}).$mount('#app')
```

编写页面

```html
<div id="app">
  <div id="nav">
    <!-- 路由标签，在生成页面的时候渲染为<a>标签，点击跳转相应的页面 -->
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>|
    <router-link to="/me">Me</router-link>
  </div>
  <!-- 将路由跳转后的页面渲染到这个位置 -->
  <router-view/>
</div>
```

### 2、`<router-link>` 的一些属性

#### tag

有时候想要 `<router-link>` 渲染成某种标签，例如 `<button>`。 于是我们使用 tag prop类指定何种标签，同样它还是会监听点击，触发导航。

```html
<router-link to="/about" tag="button">About</router-link>|
```

渲染结果

![20200413224331](https://cdn.jsdelivr.net/gh/1134642046/ImageBed/VueLearn/20200413224331.png)

#### replace

- type: `boolean`
- default: `false`

  设置 replace 属性的话，当点击时，会调用 router.replace() 而不是 router.push()，于是导航后不会留下 history 记录。

```html
<router-link to="/about" replace>About</router-link>|
```

更多的api参考[API 参考](https://router.vuejs.org/zh/api/)

### 3、动态路由

当我们有时候需要根据后端不同数据跳转到相同的页面时我们就需要使用动态路由。例如，我们有一个`User` 组件，对于所有`Name`各不相同的用户，都要使用这个组件来渲染。那么，我们可以在`vue-router`的路由路径中使用“动态路径参数”(dynamic segment) 来达到这个效果：

在路由的配置中添加User组件

```js
{
  // ：userName表示该路径下的所有用户名称都匹配该组件
  path: "/user/:userName",
  name: "User",
  component: User
}
```

在需要跳转`<router-link>`标签中使用`v-bind`绑定`to`属性

```html
<!-- 拼接用户名称 -->
<router-link :to="'/user/'+userName">用户</router-link>

<script>
export default{
  name: 'App',
  data() {
    return {
      userName: 123
    }
  }
}
</script>
```

跳转后的页面使用`this.$route.params`获取用户名称

```js
export default{
  name: "User",
  data() {
    return {
      // 根据之前的传入参数取值
      userName: this.$route.params.userName
    }
  }
}
```

### 4、路由嵌套

实际生活中的应用界面，通常由多层嵌套的组件组合而成。同样地，URL 中各段动态路径也按某种结构对应嵌套的各层组件，例如：用户界面还包含两个组件

```js
/user/lisi/account
/user/lisi/profile 
```

这时候需要使用路由嵌套的方法配置路径

```js
{
  path: "/user/:userName",
  name: "User",
  component: User,
  // 使用children属性表示在该组件内
  children: [
    {
      path: "account",
      name: "Account",
      component: Account
    },
    {
      path: "profile",
      name: "Profile",
      component: Profile
    }
  ]
}
```

在User组件中添加两个新的组件

```html
<div id="user">
  <h2>欢迎{{userName}}来到用户界面！</h2>
  <div id="bar">
    <router-link :to="'/user/'+userName+'/account'">账号</router-link>
    <router-link :to="'/user/'+userName+'/profile'">个人档案</router-link>
    <router-view></router-view>
  </div>
</div>
```

### 5、路由参数传递

有时候我们需要在两个页面之间传递一些数据，例如：从当前组件向下一个组件跳转的时候，传递一些用户的信息。

vue使用`query`这个属性来传递数据，从而在浏览器地址栏中生成如图所示url：

![20200414153043](https://cdn.jsdelivr.net/gh/1134642046/ImageBed/VueLearn/20200414153043.png)

在User组件中`query`设置传递的参数

```html
<router-link :to="{path: '/user/'+userName+'/profile', query: {name: '李四', age: 15, sex: '男'}}">个人档案</router-link>
```

在跳转的目标组件使用`this.$route.query`取出参数

```js
export default{
  name: 'Profile',
  data() {
    return {
      name: this.$route.query.name,
      age: this.$route.query.age,
      sex: this.$route.query.sex,
    }
  }
}
```

### 6、



```js

```

```js

```

```js

```

## 2、
