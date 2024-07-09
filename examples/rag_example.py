
from pyspark_ai import SparkAI
from pyspark.sql import DataFrame, SparkSession

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import VLLM

model_name = "sentence-transformers/all-mpnet-base-v2"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}
hf_embedding = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

index_name = 'tpch_index'

def load_tpch_schema():
    with open("tpch.sql","r") as f:
        all_lines = f.readlines()
    tpch_texts = "".join(all_lines).replace("\n",' ')
    tables = tpch_texts.split(";")
    return tables


def store_in_faiss(texts):
    db = FAISS.from_texts(texts, hf_embedding)
    db.save_local(index_name)


if __name__ == '__main__':
    # split TPCH schema and store it in faiss vector store
    tpch_texts = load_tpch_schema()
    store_in_faiss(tpch_texts)

    db = FAISS.load_local(index_name, hf_embedding)
    # Initialize the VLLM
    # Arguments for vLLM engine: https://github.com/bigPYJ1151/vllm/blob/e394e2b72c0e0d6e57dc818613d1ea3fc8109ace/vllm/engine/arg_utils.py#L12
    llm = VLLM(
        # model="defog/sqlcoder-7b-2",
        # model="deepseek-ai/deepseek-coder-7b-instruct-v1.5",
        model="microsoft/Phi-3-mini-4k-instruct",
        trust_remote_code=True,
        download_dir="/mnt/DP_disk2/models/Huggingface/"
    )

    # show reference tables
    docs = db.similarity_search("What is the customer's name who has placed the most orders in year of 1995? ")
    for doc in docs:
        print(doc.page_content)

    spark_session = SparkSession.builder.appName("text2sql").master("local[*]").enableHiveSupport(). getOrCreate()
    spark_session.sql("show databases").show()
    spark_session.sql("use tpch;").show()
    # # Initialize and activate SparkAI
    spark_ai = SparkAI(llm=llm,verbose=True,spark_session=spark_session, vector_db=db)
    spark_ai.activate()
    spark_ai.transform_rag("What is the customer's name who has placed the most orders in year of 1995? ").show()
