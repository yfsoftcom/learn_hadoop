# learn hadoop in hard way

write mapperReducer with golang in hadoop

https://github.com/vistarmedia/gossamr

mooc -> https://www.imooc.com/video/20757


### hadoop docker-compose

https://github.com/big-data-europe/docker-hadoop



### hdfs commands

`$ hdfs dfs -ls /`

### submit mapperReducer

`$ `

### First Demo

https://songlee24.github.io/2015/07/29/mapreduce-word-count/

hadoop jar second-0.0.1-SNAPSHOT.jar io.yunplus.second.WordCount /data/foo/hello.txt /data/foo/out1.txt


### Python MapReduce

#### install python for each container
`$ apt update && apt install -y python`

#### test local
`$ cat hello.txt | python mp1/mapper.py | sort -k1,1 | python mp1/reducer.py`

#### run the script

- upload file `make put file=test.txt`
- run mapreduce `make run mp=mp1 input=test.txt output=test_out`
- checkout `make check file=test_out`

### About hadoop

大数据，通常是指海量的非规则数据，基于 HDFS 进行文件的分布式存储，普通的程序开发都是将数据加载到程序所在的内存中进行处理，大数据则包含了太多数据，传输过程会消耗很多资源，于是，大数据开发就将代码传送到数据平台上进行执行。

最基础的数据开发则是 MapReduce 的批处理编程模型，通过规则筛选出数据源进行 Map，拆分成多个 Split，然后经过处理和排序，shuffle，整合到 Reduce 函数中进行数据的汇总和排序，并将数据写入到 Hadoop。

其它的如 Spark Hive 等等都是为了方便开发者自动构建 Map 和 Reduce 任务而创建的框架。

https://www.infoq.cn/article/hadoop-storm-samza-spark-flink

https://zhuanlan.zhihu.com/p/94302767

数据收集工具 
- Sqoop 可以将传统的关系型数据库数据导入/导出到 HDFS
- Flume 可以将日志文件转换成流数据推送到目标服务器
- Filebeat 可以搜集日志文件到目标服务器

数据处理工具
- MapReduce
- Hive
- Storm
- Flink
