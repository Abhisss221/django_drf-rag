import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def ingest_for_user(user_id: int):
    data_path = os.path.join(
        BASE_DIR, "user_data", f"user_{user_id}", "docs.txt"
    )

    index_path = os.path.join(
        BASE_DIR, "user_indexes", f"user_{user_id}"
    )

    if not os.path.exists(data_path):
        print(f"No data found for user {user_id}")
        return

    os.makedirs(index_path, exist_ok=True)

    loader = TextLoader(data_path, encoding="utf-8")
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(index_path)

    print(f"✅ Indexed data for user {user_id}")
