from .cache_service import cache_service
from .data_version import data_version
from .rag_chain import create_rag_chain
import os


class RAGService:
    def ask(self, user_id: int, question: str) -> str:
        version = data_version.get(user_id)
        cache_key = cache_service.make_key(user_id, question, version)

        cached = cache_service.get(cache_key)
        if cached:
            return cached

        index_path = os.path.join(
            os.path.dirname(__file__),
            "user_indexes",
            f"user_{user_id}"
        )

        if not os.path.exists(index_path):
            return "No documents found for this user."

        rag_chain = create_rag_chain(index_path)
        result = rag_chain.invoke({"query": question})["result"]

        cache_service.set(cache_key, result)
        return result


rag_service = RAGService()
