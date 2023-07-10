# 1、树形结构多选搜索的全选问题

## 1、搜索实现

### 1、html

elementUI 的tree选择器在开启多选后，在需要对节点进行过滤时，调用 Tree 实例的`filter`方法，参数为搜索的关键字。需要注意的是，此时需要设置`filter-node-method`，绑定过滤函数。

```html
<div class="picker-tree">
    <el-input
              placeholder="输入关键字进行过滤"
              v-model="filterText">
    </el-input>
    <el-tree
             :data="deptData"
             show-checkbox
             ref="depttree"
             node-key="id"
             empty-text="请选择角色类型"
             :props="defaultProps"
             :filter-node-method="filterNode"
             @check-change="handleCheckChange"
             >
    </el-tree>
</div>
```

### 2、Vue

创建一个监听器，监听搜索的关键字所属变量`filterText`。然后创建一个节点过滤函数`filterNode`通过关键字过滤结果。

```javascript
export default {
    watch: {
      filterText(val) {
        this.$refs.tree.filter(val);
      }
    },
    methods: {
      filterNode(value, data) {
        //value为关键字，data为节点数据
        //value为空代表未开始搜索，所以全部为true，不进行过滤
        if (!value) return true;
        return data.label.indexOf(value) !== -1;
      }
    },
}
```

## 2、问题产生

