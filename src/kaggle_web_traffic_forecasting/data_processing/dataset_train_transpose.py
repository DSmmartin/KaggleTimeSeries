from pyspark.sql.functions import array, col, explode, struct, lit
from pyspark.sql.types import DateType
from .utils import COLUMN_DATE, COLUMN_TRAFFIC


def dataset_train_transpose(dataset_train_raw):
    by = ['Page']
    cols, dtypes = zip(*((c, t) for (c, t) in dataset_train_raw.dtypes if c not in by))
    assert len(set(dtypes)) == 1, "All columns have to be of the same type"

    kvs = explode(array([
      struct(lit(c).alias(COLUMN_DATE), col(c).alias(COLUMN_TRAFFIC)) for c in cols
    ])).alias("kvs")

    dataset_train = dataset_train_raw.select(by + [kvs]).select(by + [f"kvs.{COLUMN_TRAFFIC}", f"kvs.{COLUMN_DATE}"])

    dataset_train = dataset_train.withColumn("Date", dataset_train["Date"].cast(DateType()))

    return dataset_train
