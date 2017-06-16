neo4j 相关笔记
=============

脚本工具
-------

安装依赖：

	$ pip install requirements.txt

### generate\_cypher\_from\_csv\_file.py

读取从 MySQL 导出的表 csv 文件（需要带header），生成 cypher 语句。

	# -f <filename>，支持相对路径，绝对路径
	$ python generate_cypher_from_csv_file.py -f "/path/to/table_name.csv"

	# -c 自动保存结果到剪切板
	$ python generate_cypher_from_csv_file.py -f "/path/to/table_name.csv" -c


遇到的问题
---------

### 从本地 load csv 文件

**Q:** 尝试 `load csv from file:///Users/username/.../data.csv`，提示 `Couldn't load the external resource at: file:/usr/local/Cellar/neo4j/3.2.0/libexec/import/Users/username/.../data.csv`

版本：`macOS Sierra 10.12.5`, `neo4j 3.2.0` 

**A:** 看起来是从固定目录导入，可以把数据放在 neo4j import 目录中，再load csv。

或者：
![load-local-csv.png](./imgs/load-local-csv.png)

[StackOverflow: Cypher Neo4j Couldn't load the external resource](https://stackoverflow.com/questions/28398778/cypher-neo4j-couldnt-load-the-external-resource)