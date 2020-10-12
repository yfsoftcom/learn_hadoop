## Spark

https://hub.docker.com/r/bitnami/spark

`$ curl -LO https://raw.githubusercontent.com/bitnami/bitnami-docker-spark/master/docker-compose.yml`
`$ docker-compose up`

### Spark SQL

https://github.com/tirthajyoti/Spark-with-Python/blob/master/Dataframe_SQL_query.ipynb


### TODO List

- [x] Spark Connected MongoDB
- [x] Run Sql to read data from it
- [ ] Run advanced sql to read parent-children documents
- [ ] Save the data into mongo or csv
- [ ] Connect postgresql at the same time
- [ ] Join the 2 dataset.

### Spark And Mongo

1. Spark 和 mongo 交互需要使用connector对应的jar包，该jar包可以从下面的项目中下载 `https://github.com/mongodb/mongo-spark`。

2. 除了该jar包之外，还需要使用到 mongo 对应的 driver，不然会导致下面的问题
https://stackoverflow.com/questions/52385123/pyspark-mongodb-java-lang-noclassdeffounderror-com-mongodb-client-model-coll

3. 需要下载到对应的jar文件，然后copy到Spark_Home的jars目录下，执行下面的命令可以打开对应的交互终端。

```bash
pyspark --jars mongo-spark-connector_2.12-3.0.0.jar \
 --driver-class-path mongo-spark-connector_2.12-3.0.0.jar \
 --conf spark.mongodb.input.uri=mongodb://172.16.11.63/ev_metro.customer?readPreference=primaryPreferred \
 --conf spark.mongodb.output.uri=mongodb://172.16.11.63/ev_metro.customer
```

4. 使用下面的命令提交脚本

```bash
spark-submit --master "local[4]"  \
    --jars /opt/bitnami/spark/ivy/jars/mongo-spark-connector_2.12-3.0.0.jar \
    --driver-class-path /opt/bitnami/spark/ivy/jars/mongo-spark-connector_2.12-3.0.0.jar \
    --conf spark.mongodb.input.uri=mongodb://172.16.11.63/ev_metro.customer?readPreference=primaryPreferred \
    --conf spark.mongodb.output.uri=mongodb://172.16.11.63/ev_metro.customer \
    test.py
```

5. 使用如下命令复制jar文件
```bash
cp /opt/bitnami/spark/ivy/jars/*.jar /opt/bitnami/spark/jars/
```