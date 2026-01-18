from .rag_chain import rag_chain


class RAGService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def ask(self, question: str) -> str:
        result = rag_chain.invoke({"query": question})
        return result["result"]


# Singleton instance (loaded once)
rag_service = RAGService()
