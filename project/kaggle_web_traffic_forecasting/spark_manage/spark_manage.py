import pyspark
import os
import sys

def spark_start(show_output=False):
    print("Starting Spark")
    spark = pyspark.sql.SparkSession.builder.getOrCreate()

    if show_output:
        print("Spark configuration")
        print(spark.sparkContext.uiWebUrl)
        print(spark.sparkContext.getConf().getAll())
        print_environment(spark)

    return spark

def print_environment(spark):
    print("Work directory:", os.getcwd())
    print ('****************')
    print ('Python version: {}'.format(sys.version))
    print ('Spark version: {}'.format(spark.version))
    print ('****************')
