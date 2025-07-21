# ! pip install langchain ctransformers langchain-community pinecone pypdf sentence-transformers
from src.helper import load_pdf,text_split,download_embedding
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
import os
from dotenv import load_dotenv
from src.logger import logger
import pinecone

load_dotenv()


extract_data=load_pdf('data/')
logger.info('Load data succesfully')

text_chunks=text_split(extract_data=extract_data)
logger.info('split data successfully')
embeddings=download_embedding()

logger.info('Data embedding done')

PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')

pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "medicalchatbot"
index = pc.Index(index_name)

docsearch = PineconeVectorStore.from_texts(
    texts=[t.page_content for t in text_chunks],
    embedding=embeddings,
    index_name=index_name,
    pinecone_api_key=PINECONE_API_KEY
)

logger.info('Vector transfer done')



print(docsearch)