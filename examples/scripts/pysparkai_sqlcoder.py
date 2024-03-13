from langchain_community.llms import VLLM
llm = VLLM(
    model="defog/sqlcoder"
)

from pyspark_ai import SparkAI
spark_ai = SparkAI(llm=llm)
spark_ai.activate()
