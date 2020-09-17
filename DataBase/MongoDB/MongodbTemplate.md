# MongodbTemplated的使用

创建一个MongoTemplate对象

```java
@Autowried
MongoTemplate mongoTemplate;
```

更多内容见[Api文档](https://docs.spring.io/spring-data/mongodb/docs/3.0.2.RELEASE/api/)

## 1、查询

查询有多种方式这里介绍`find`方法，还有`FindAll、FindById、FindOne`等见API

```java
// 创建查询规则相当于 where _id = "1"
Query query = new Query(Criteria.where("_id").is("1"));
// 执行查询操作 select * from Form where _id = 1
// Form.class为返回类型，操作做的mongo集合如果实体类没有指定默认为Form表单
List <Form> form = mongoTemplate.findOne(query, Form.class);
// 可以通过collectionName指定集合名称
public <T> List<T> find(Query query,
                        Class<T> entityClass,
                        String collectionName)
// 例如
Form form = mongoTemplate.findOne(query, Form.class, "form");
```

## 2、添加

添加有两种方式`insert、save`

### 1. insert

插入用于最初将对象存储到数据库中。如果该对象在集合中已存在,要更新现有对象，请使用save方法。insert无法更新数据

如果你的对象中包含Id,那么该Id将会有MongoDB自动生成填充，类型为ObjectId。如果你的Id类型为String，将会自动转换格式

```java
Form form = mongoTemplate.insert(form);
```

### 2. save

save可以更新数据,如果数据不存在这执行插入操作，即“ upsert”。

save会将传入的实体类存入mongodb，也可以使用`save(T objectToSave,String collectionName)`的collectionName指定集合。

如果你的对象中包含Id,那么该Id将会有MongoDB自动生成填充，类型为ObjectId。如果你的Id类型为String，将会自动转换格式。

```java
// 返回存入的数据
Form form = mongoTemplate.save(form);
```

## 3、删除

删除分为删除指定集合全部、根据集合中的文档Id删除，例如：`remove(Object object)、remove(Query query, Class<?> entityClass)`更多详见API

```java
// 查询所有在delete_ids数组中的的Id
// where _id in(...)
Query query = new Query(Criteria.where("_id").in(delete_ids));
// 删除所有查找的数据，getDeletedCount()获取删除的数量并返回
Long count = mongoTemplate.remove(query, Form.class).getDeletedCount();
```

通过该实体类对象中的Id查找并删除一条数据,返回删除的数据

```java
Form form2 = mongoTemplate.remove(form).
```

## 4、修改

```java

```

## 5、聚合

```java

```

```java

```