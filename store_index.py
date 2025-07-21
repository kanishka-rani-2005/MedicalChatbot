from src.helper import load_pdf,text_split,download_embedding
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
import os
from dotenv import load_dotenv

import pinecone

load_dotenv()

extract_data=load_pdf('data/')


text_chunks=text_split(extract_data=extract_data)

embeddings=download_embedding()



PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "medicalchatbot"
index = pc.Index(index_name)

docsearch = PineconeVectorStore.from_texts(
    texts=[t.page_content for t in text_chunks],
    embedding=embeddings,
    index_name=index_name,
    pinecone_api_key=PINECONE_API_KEY
)



