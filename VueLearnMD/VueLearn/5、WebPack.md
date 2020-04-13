<!--
 * @Author: your name
 * @Date: 2020-01-06 16:06:18
 * @LastEditTime: 2020-04-11 12:15:23
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \VueLearn\5、WebPack.md
 -->

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [WebPack](#webpack)
  - [1、安装与配置](#1%e5%ae%89%e8%a3%85%e4%b8%8e%e9%85%8d%e7%bd%ae)
  - [2、基础使用](#2%e5%9f%ba%e7%a1%80%e4%bd%bf%e7%94%a8)
    - [1、起步](#1%e8%b5%b7%e6%ad%a5)
    - [2、配置 package.json](#2%e9%85%8d%e7%bd%ae-packagejson)
    - [3、webpack.config.js 配置](#3webpackconfigjs-%e9%85%8d%e7%bd%ae)
    - [4、加载器](#4%e5%8a%a0%e8%bd%bd%e5%99%a8)
      - [1、样式加载器](#1%e6%a0%b7%e5%bc%8f%e5%8a%a0%e8%bd%bd%e5%99%a8)
      - [2、图片文件处理](#2%e5%9b%be%e7%89%87%e6%96%87%e4%bb%b6%e5%a4%84%e7%90%86)
    - [5、webpack_dev_server](#5webpackdevserver)
  - [3、抽离配置文件](#3%e6%8a%bd%e7%a6%bb%e9%85%8d%e7%bd%ae%e6%96%87%e4%bb%b6)

<!-- /code_chunk_output -->

# WebPack

## 1、安装与配置

webPack 依赖 Node 环境。先要安装 node.js

安装 WebPack

```cmd {cmd}
npm install webpack webpack-cli --save-dev
```

## 2、基础使用

### 1、起步

构建一个项目目录

```js
+ |- /dist
+ |- /src
+   |- main.js
  |- index.html
```

npm 初始化生成一个 package.json 文件，进行配置

```cmd
npm init -y
```

创建一个 webpack.config.js 文件，设置打包的入口

```js
+ |- /dist
+ |- /src
+   |- main.js
  |- index.html
  |- package.json
  |- webpack.config.js
```

### 2、配置 package.json

当我们在运行 webpack 时可以通过配置 package.json 文件简化运行代码：
在 scripts 中添加一个`build`，内容为`webpack`

```json
{
  "name": "webpack",
  "version": "1.0.0",
  "description": "",
  "main": "main.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "build": "webpack"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

配置完后`npm run build`就会执行 webpack

### 3、webpack.config.js 配置

当打包的时候为了简化打包的指令可以使用以下的配置

```js
const path = require("path");

module.exports = {
  // 入口文件
  entry: "./src/main.js",
  // 出口：输出打包后的文件
  output: {
    // 路径为绝对路径，获取当前目录的绝对路径
    path: path.resolve(__dirname, "dist"),
    // 输出的文件名
    filename: "bundle.js",
  },
};
```

### 4、加载器

#### 1、样式加载器

有时候我们需要加载css、less等文件，这时候就需要使用样式加载器

安装

```cmd
npm install --save-dev css-loader
```

配置规则

```js
module.exports = {
// 样式加载器模块
  module: {
    rules: [
      {
        // 正则匹配css文件
        test: /\.css$/,
        // 执行顺序从右到左
        use: ["style-loader", "css-loader"],
      },
    ],
  },
};
```

还有许多其他的加载器具体访问[loaders](https://www.webpackjs.com/loaders/)

#### 2、图片文件处理

图片的添加需要使用`url-loader`,安装后的配置

```js
{
  test: /\.(png|jpg|gif)$/,
  use: [
    {
      loader: 'url-loader',
      options: {
        limit: 8192
      }
    }
  ]
}
```

在使用过程中和`file-loader`不可以同时使用会出现问题，具体原因还未找到，但是发现使用``可以实现文件加载的功能，配置一下name属性即可，

```js
{
  test: /\.(png|jpg|gif)$/,
    use: [
      {
        loader: 'url-loader',
        options: {
          limit: 8192,
          // name表示你的文件名，hash:8表示使用8位哈希值，ext表示扩展名
          name: "img/[name].[hash:8].[ext]",
          // 因为大于8192的文件直接加载到了dist目录，所以需要配置一下公共路径
          publicPath: "dist/"
        }
      }
    ]
}
```

### 5、webpack_dev_server

安装

```cmd
npm install webpack-dev-server --save-dev
```

配置

```js
devServer: {
  // 自动打开浏览器
  open: true,
  // 端口号
  port: 8081,
  // 使用的目录
  contentBase: "./list",
  // 是否启动热加载
  hot: true
}
```

**热加载模块:**它允许在运行时更新各种模块，而无需进行完全刷新

```js
const webpack = require("webpack")

plugins: [
  new webpack.HotModuleReplacementPlugin({
    // Options...
  })
]
```

## 3、抽离配置文件

```js

```


```js

```


```js

```