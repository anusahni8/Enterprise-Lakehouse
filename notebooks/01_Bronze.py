from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

customers = spark.read.option("header",True).csv("data/customers.csv")
customers.write.format("delta").mode("overwrite").saveAsTable("bronze.customers")
print("Bronze load complete")
