""" Spark manager instance
"""

import os
import sys
import pyspark # pylint:  disable=E0401


def spark_start(show_output=False):
    """ Spark initialization instance

    Keyword Arguments:
        show_output {bool} -- show environment configuration (default: {False})

    Returns:
        SparkSession -- spark application
    """

    print("Starting Spark")
    spark = pyspark.sql.SparkSession.builder.getOrCreate()

    if show_output:
        print("Spark configuration")
        print(spark.sparkContext.uiWebUrl)
        print(spark.sparkContext.getConf().getAll())
        print_environment(spark)

    return spark

def print_environment(spark):
    """ show environment configuration

    Arguments:
        spark {SparkSession} -- spark application
    """

    print("Work directory:", os.getcwd())
    print('****************')
    print('Python version: {}'.format(sys.version))
    print('Spark version: {}'.format(spark.version))
    print('****************')
