import os
from pyspark.sql import SparkSession
from pyspark.dbutils import DBUtils

spark = SparkSession\
.builder\
.getOrCreate()

print("Testing simple count")

print(spark.range(100).count())


dbutils = DBUtils(spark.sparkContext)
print(dbutils.fs.ls("dbfs:/"))