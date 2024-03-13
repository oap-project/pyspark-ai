from langchain_community.llms import VLLM
llm = VLLM(
    model="yahma/llama-7b-hf",
    trust_remote_code=True,  # mandatory for hf models
)

from pyspark_ai import SparkAI
spark_ai = SparkAI(llm=llm,verbose=True)
spark_ai.activate()

auto_df = spark_ai.create_df("https://www.carpro.com/blog/full-year-2022-national-auto-sales-by-brand")
auto_df.show()
