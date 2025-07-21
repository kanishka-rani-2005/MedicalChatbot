from flask import Flask, render_template, request
from src.helper import download_embedding
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from src.prompt import *
import os

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')


embeddings = download_embedding()


pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "medical-chatbot"
index = pc.Index(index_name)

#Loading the index
docsearch=PineconeVectorStore.from_existing_index(index_name,embeddings)


prompt=PromptTemplate(
    input_variables=['context','question'],
    template=prompt_template
)

chain_type_kwargs={'prompt':prompt}


llm=CTransformers(
    model=r'model\llama-2-7b-chat.ggmlv3.q4_0.bin',
    model_type='llama',
    config={
        'max_new_tokens':512,
        'temperature':0.8
    }
)

qa=RetrievalQA.from_chain_type(
    llm=llm,
    chain_type='stuff',
    retriever=docsearch.as_retriever(search_kwargs={'k':2}),
    return_source_documents=True,
    chain_type_kwargs=chain_type_kwargs
)


@app.route("/")
def index():
    return render_template('index.html')



@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result=qa({"query": input})
    print("Query :",input)
    print("Response : ", result["result"])
    return str(result["result"])



if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)

