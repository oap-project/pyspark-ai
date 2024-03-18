import os
import time
from langchain_community.llms import VLLM
from pyspark_ai import SparkAI

# Set the environment variable
#os.environ['OMP_NUM_THREADS'] = '32'
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

# Start timer
start_time = time.time()

# Initialize the VLLM
llm = VLLM(
    #optional model: "bigcode/starcoder", "defog/sqlcoder-7b-2", "defog/sqlcoder"
    model="defog/sqlcoder",
    trust_remote_code=True,
)

# Initialize and activate SparkAI
spark_ai = SparkAI(llm=llm,verbose=True)
spark_ai.activate()

# DataFrame operation
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
df.ai.transform("What are the best-selling Cellphone?").show()
#df.ai.plot()

# End timer
end_time = time.time()
print(f"Total execution time: {end_time - start_time} seconds")


