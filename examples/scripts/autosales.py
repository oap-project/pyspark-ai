from pyspark_ai import SparkAI

spark_ai = SparkAI(verbose=True)
spark_ai.activate()



# Search and ingest web content into a DataFrame
# If you have set up google-api-python-client, you can just run
# auto_df = spark_ai.create_df("2022 USA national auto sales by brand")
auto_df = spark_ai.create_df("https://www.carpro.com/blog/full-year-2022-national-auto-sales-by-brand")
auto_df.show()

