import os
from .rag_chain import create_rag_chain

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class RAGService:
    def ask(self, user_id: int, question: str) -> str:
        user_index_path = os.path.join(
            BASE_DIR, "user_indexes", f"user_{user_id}"
        )

        if not os.path.exists(user_index_path):
            return "No documents found for this user."

        rag_chain = create_rag_chain(user_index_path)

        result = rag_chain.invoke({"query": question})
        return result["result"]


rag_service = RAGService()
