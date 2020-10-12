from pyspark.sql import SparkSession
from pyspark.sql.functions import explode

if __name__ == "__main__":

    spark = SparkSession \
        .builder \
        .appName('MyApp') \
        .config('spark.mongodb.input.uri', 'mongodb://172.16.11.63/ev_metro.customer') \
        .getOrCreate()

    df = spark.read.format('mongo').load()

    df.createOrReplaceTempView('user')
    df.printSchema()
    df2 = df.select(df.companymobile, df.custkey, df.storekey, explode(df.cardholders))
    df2.printSchema()
    df2 = df2.select(df2.companymobile, df2.custkey, df2.storekey, explode(df2.col))
    # , explode(df.cardholders.shortname)

    

    jdbcDF = spark.read \
        .format("jdbc") \
        .option("url", "jdbc:postgresql://172.16.11.63/fim?user=fpm&password=Fim741235896") \
        .option("dbtable", "rtc_activity_join") \
        .load()
    jdbcDF.createOrReplaceTempView('aj')
    jdbcDF.printSchema()

    resDf = spark.sql('select companymobile, custkey, storekey, cardholders.shortname, cardholders.cardholderkey from user, aj where user.companymobile = aj.mobile')

    # Saving data to a JDBC source
    # resDf.write \
    #     .format("mongo") \
    #     .mode("append").option("collection", "result").save()
    resDf.withColumn('shortname_as_str', array_to_string_udf(resDf["shortname"])) \
        .withColumn('cardholderkey_as_str', array_to_string_udf(resDf["cardholderkey"])) \
        .drop("shortname") \
        .drop("cardholderkey") \
        .write.csv('result.csv')
    resDf.show()

    spark.stop()

    exit(0)