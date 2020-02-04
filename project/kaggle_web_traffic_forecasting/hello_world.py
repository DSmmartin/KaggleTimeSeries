import os
from pyspark.sql import SparkSession
from pyspark.dbutils import DBUtils

spark = SparkSession\
.builder\
.getOrCreate()

print("Testing dbutils")

dbutils = DBUtils(spark.sparkContext)
print(dbutils.fs.ls("dbfs:/"))

print('--------')
print(dbutils.secrets.listScopes())

print('--------')
token_48h = 'TOKE_48h'
dbutils.secrets.setToken(token_48h)
print(dbutils.secrets.get(scope='kaggle-storage', key='storage-name'))
print(dbutils.secrets.get(scope='kaggle-storage', key='storage-key'))

