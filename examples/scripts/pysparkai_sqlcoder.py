from langchain_community.llms import VLLM
llm = VLLM(
    model="defog/sqlcoder"
)

from pyspark_ai import SparkAI
spark_ai = SparkAI(llm=llm,verbose=True)
spark_ai.activate()

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

