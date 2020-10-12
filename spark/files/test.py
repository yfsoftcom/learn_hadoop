from pyspark.sql import SparkSession

if __name__ == "__main__":

    spark = SparkSession \
        .builder \
        .appName('MyApp') \
        .config('spark.mongodb.input.uri', 'mongodb://172.16.11.63/ev_metro.customer') \
        .getOrCreate()

    df = spark.read.format('mongo').load()

    df.createOrReplaceTempView('user')

    resDf = spark.sql('select companymobile from user')

    resDf.show()

    spark.stop()

    exit(0)