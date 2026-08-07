from pyspark.sql import functions as F

df=spark.table("bronze.customers")
df=df.dropDuplicates().fillna("Unknown")
df.write.format("delta").mode("overwrite").saveAsTable("silver.customers")
print("Silver load complete")
