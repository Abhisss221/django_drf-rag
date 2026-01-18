from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(BASE_DIR, "data", "docs.txt")
INDEX_PATH = os.path.join(BASE_DIR, "faiss_index")

# Load document
loader = TextLoader(DATA_PATH, encoding="utf-8")
documents = loader.load()

# Split text
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)
chunks = splitter.split_documents(documents)

# Embeddings (open-source)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create vector store
vectorstore = FAISS.from_documents(chunks, embeddings)

# Save index
vectorstore.save_local(INDEX_PATH)

print("✅ FAISS index created at:", INDEX_PATH)
