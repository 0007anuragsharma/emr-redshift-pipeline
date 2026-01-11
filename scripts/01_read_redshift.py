from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Read_Redshift_Table") \
    .getOrCreate()

jdbc_url = "jdbc:redshift://<REDSHIFT-ENDPOINT>:5439/dev"

df = spark.read \
    .format("jdbc") \
    .option("url", jdbc_url) \
    .option("dbtable", "orders") \
    .option("user", "<REDSHIFT_USER>") \
    .option("password", "<REDSHIFT_PASSWORD>") \
    .option("driver", "com.amazon.redshift.jdbc.Driver") \
    .load()

df.show(5)
df.printSchema()

spark.stop()
