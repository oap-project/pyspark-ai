from langchain_community.llms import VLLM
llm = VLLM(
    model="yahma/llama-7b-hf",
    trust_remote_code=True,  # mandatory for hf models
)

from pyspark_ai import SparkAI
spark_ai = SparkAI(llm=llm)
spark_ai.activate()
