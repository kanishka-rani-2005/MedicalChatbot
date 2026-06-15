from flask import Flask, render_template, request
from src.helper import download_embedding

from langchain_community.vectorstores import Pinecone
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_community.llms import CTransformers

from dotenv import load_dotenv
from src.prompt import *

import pinecone
import os

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")

embeddings = download_embedding()

# Initialize Pinecone
pinecone.init(
    api_key=PINECONE_API_KEY,
    environment=PINECONE_ENVIRONMENT
)

index_name = "medical-chatbot"

# Load existing Pinecone index
docsearch = Pinecone.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=prompt_template
)

chain_type_kwargs = {"prompt": prompt}

llm = CTransformers(
    model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
    model_type="llama",
    config={
        "max_new_tokens": 512,
        "temperature": 0.8
    }
)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=docsearch.as_retriever(search_kwargs={"k": 2}),
    return_source_documents=True,
    chain_type_kwargs=chain_type_kwargs
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]

    result = qa({"query": msg})

    return str(result["result"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)