""" Main function
"""

from kaggle_web_traffic_forecasting import spark_start, dataset_train_transpose
from kaggle_web_traffic_forecasting.data_processing.utils import KEY_SHEMA

spark = spark_start(show_output=True)

data_id = spark.read.csv('./mnt/kaggle-data-raw/key_1.csv',
                         header=True,
                         schema=KEY_SHEMA)

data_train_raw = spark.read.csv('./mnt/kaggle-data-raw/train_1.csv',
                                header=True,
                                inferSchema=True)

data_train = dataset_train_transpose(data_train_raw)

print('end')


print('End process')