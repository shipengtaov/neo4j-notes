neo4j 相关笔记
=============

### 从本地 load csv 文件

**Q:** 尝试 `load csv from file:///Users/username/.../data.csv`，提示 `Couldn't load the external resource at: file:/usr/local/Cellar/neo4j/3.2.0/libexec/import/Users/username/.../data.csv`

版本：`macOS Sierra 10.12.5`, `neo4j 3.2.0` 

**A:** 看起来是从固定目录导入，可以把数据放在 neo4j import 目录中，再load csv。

或者：
![load-local-csv.png](./imgs/load-local-csv.png)

[StackOverflow: Cypher Neo4j Couldn't load the external resource](https://stackoverflow.com/questions/28398778/cypher-neo4j-couldnt-load-the-external-resource)