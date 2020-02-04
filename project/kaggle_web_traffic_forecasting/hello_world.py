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
token_48h = 'dkea854ad26b80bd5286d77364ab509fc377'
dbutils.secrets.setToken(token_48h)
storage_name = dbutils.secrets.get(scope='kaggle-storage', key='storage-name')
storage_key = dbutils.secrets.get(scope='kaggle-storage', key='storage-key')
storage_container_name = 'dataraw'
mount_point = "/mnt/kaggle-data-raw/"

key = spark.read.csv(f'{mount_point}key_1.csv',
                     sep=',',
                     header=True,
                     inferSchema=True)

train = spark.read.csv(f'{mount_point}train_1.csv',
                     sep=',',
                     header=True,
                     inferSchema=True)


print('end ml process')