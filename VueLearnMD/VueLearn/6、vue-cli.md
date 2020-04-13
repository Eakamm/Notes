<!--
 * @Author: your name
 * @Date: 2020-04-11 12:15:52
 * @LastEditTime: 2020-04-13 22:38:36
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

**tag：** 有时候想要 `<router-link>` 渲染成某种标签，例如 `<button>`。 于是我们使用 tag prop类指定何种标签，同样它还是会监听点击，触发导航。

```html
<router-link to="/about" tag="button">About</router-link>|
```

渲染结果



```js
```

```js
```

## 2、
