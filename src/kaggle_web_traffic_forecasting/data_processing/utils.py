""" Data configuration shared between modules
"""

from pyspark.sql.types import IntegerType, StringType, StructField, StructType, DateType

DATASET_KEY_RAW = 'key_raw'
DATASET_TRAIN_PROCESSED = 'train_processed'
DATASET_RAW = 'dataset_raw'

METADATA_COLUMNS_NAMES = 'columns_names'
METADATA_COLUMNS_TYPES = 'columns_types'

COLUMN_PAGE = 'Page'
COLUMN_ID = 'Id'
COLUMN_DATE = 'Date'
COLUMN_TRAFFIC = 'Traffic'

TYPE_COLUMN_PAGE = 'string'
TYPE_COLUMN_ID = 'string'
TYPE_COLUMN_DATE = 'string'
TYPE_COLUMN_TRAFFIC = 'integer'


KEY_SHEMA = StructType([
    StructField(COLUMN_PAGE, StringType()),
    StructField(COLUMN_ID, StringType())
])

TRAINING_SHEMA = StructType([
    StructField(COLUMN_PAGE, StringType()),
    StructField(COLUMN_TRAFFIC, IntegerType()),
    StructField(COLUMN_DATE, DateType())
])
