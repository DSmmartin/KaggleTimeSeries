from pyspark.sql import SparkSession
spark = SparkSession\
.builder\
.getOrCreate()

print("Testing simple count")

print(spark.range(100).count())