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

extra_configs = {
    "fs.azure.account.key.{storage_container_name}.blob.core.windows.net": storage_key
}

dbutils.fs.mount(
    source = f'wasbs://{storage_container_name}@{storage_name}.blob.core.windows.net/',
    mount_point = "/mnt/kaggle-data-raw/",
    extra_configs = extra_configs)

