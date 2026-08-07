from pyspark.sql import functions as F

df=spark.table("silver.customers")
gold=df.groupBy("Country").agg(F.count("*").alias("customers"))
gold.write.format("delta").mode("overwrite").saveAsTable("gold.customer_summary")
gold.show()
