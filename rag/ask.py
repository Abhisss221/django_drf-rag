from rag_chain import rag_chain

while True:
    q = input("\nAsk: ")
    if q.lower() in ["exit", "quit"]:
        break

    result = rag_chain.invoke({"query": q})
    print("\nAnswer:", result["result"])
