import os
from pyspark.sql import SparkSession
from pyspark.dbutils import DBUtils

spark = SparkSession\
.builder\
.getOrCreate()

print("Testing simple count")

dbutils = DBUtils(spark.sparkContext)
print(dbutils.fs.ls("dbfs:/"))

print('--------')
print(dbutils.secrets.listScopes())