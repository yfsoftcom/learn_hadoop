from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

def array_to_string(my_list):
    return '[' + ','.join([str(elem) for elem in my_list]) + ']'

array_to_string_udf = udf(array_to_string, StringType())

if __name__ == "__main__":

    spark = SparkSession \
        .builder \
        .appName('MyApp') \
        .config('spark.mongodb.input.uri', 'mongodb://172.16.11.63/ev_metro.customer') \
        .getOrCreate()

    df = spark.read.format('mongo').load()

    df.createOrReplaceTempView('user')
    df.printSchema()

    

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