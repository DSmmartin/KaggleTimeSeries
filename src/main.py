""" Main function
"""

from delta.tables import *
from pyspark.sql.functions import *
from kaggle_web_traffic_forecasting import spark_start

spark = spark_start(show_output=True)


data = spark.range(0, 5)
data.write.format("delta").mode("overwrite").save("/tmp/delta-table")
deltaTable = DeltaTable.forPath(spark, "/tmp/delta-table")
deltaTable.toDF().show()


print('End process')