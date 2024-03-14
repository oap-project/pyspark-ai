from langchain_community.llms import VLLM
llm = VLLM(
    model="yahma/llama-7b-hf",
    trust_remote_code=True,  # mandatory for hf models
)

from pyspark_ai import SparkAI
spark_ai = SparkAI(llm=llm,verbose=True)
spark_ai.activate()
print("spark_ai.activate() succeed ")

#auto_df = spark_ai.create_df("https://www.carpro.com/blog/full-year-2022-national-auto-sales-by-brand")
#auto_df.show()

#df=spark_ai.create_df("https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States", ["president", "vice_president"])
#df.show()
df = spark_ai._spark.createDataFrame(
    [
        ("Normal", "Cellphone", 6000),
        ("Normal", "Tablet", 1500),
        ("Mini", "Tablet", 5500),
        ("Mini", "Cellphone", 5000),
        ("Foldable", "Cellphone", 6500),
        ("Foldable", "Tablet", 2500),
        ("Pro", "Cellphone", 3000),
        ("Pro", "Tablet", 4000),
        ("Pro Max", "Cellphone", 4500)
    ],
    ["product", "category", "revenue"]
)

df.ai.transform("What are the best-selling and the second best-selling products in every category?").show()

