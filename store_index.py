from src.helper import load_pdf, text_split, download_embedding
from langchain_community.vectorstores import Pinecone
from dotenv import load_dotenv
from src.logger import logger
import os
import pinecone

load_dotenv()

extract_data = load_pdf('data/')
logger.info('Load data successfully')

text_chunks = text_split(extract_data=extract_data)
logger.info('Split data successfully')

embeddings = download_embedding()
logger.info('Data embedding done')

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")

pinecone.init(
    api_key=PINECONE_API_KEY,
    environment=PINECONE_ENVIRONMENT
)

index_name = "medical-chatbot"

docsearch = Pinecone.from_texts(
    texts=[t.page_content for t in text_chunks],
    embedding=embeddings,
    index_name=index_name
)

logger.info('Vector transfer done')

print(docsearch)