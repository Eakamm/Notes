# Sql Mode

## 1、


```mysql
MariaDB [train]> select STU_ID,COURSE_ID ,count(*) from T_SCORE_SMALL group by course_id;
+--------+-----------+----------+
| STU_ID | COURSE_ID | count(*) |
+--------+-----------+----------+
|...|      1 |         8 |     1000 |
|      1 |         9 |     1000 |
+--------+-----------+----------+
9 rows in set (0.007 sec)

MariaDB [train]> select @@sql_mode;
+-------------------------------------------------------------------------------------------+
| @@sql_mode                                                                                |
+-------------------------------------------------------------------------------------------+
| STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION |
+-------------------------------------------------------------------------------------------+
1 row in set (0.000 sec)

MariaDB [train]> set @@sql_mode='STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION,ONLY_FULL_GROUP_BY';
Query OK, 0 rows affected (0.000 sec)

MariaDB [train]> select STU_ID,COURSE_ID ,count(*) from T_SCORE_SMALL group by course_id;
ERROR 1055 (42000): 'train.T_SCORE_SMALL.STU_ID' isn't in GROUP BY
```