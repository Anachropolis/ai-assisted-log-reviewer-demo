import chromadb
import os
from dotenv import load_dotenv
import json

load_dotenv()


client = chromadb.PersistentClient(path="../data/compliance_references/compliance_db")
collection = client.get_or_create_collection("compliance_references")

class VectorStore:

    def __init__(self) -> None:
        self.client = chromadb.PersistentClient(os.getenv("CHROMA_PERSIST_DIR"))
        self.collection = client.get_or_create_collection("CHROMA_COLLECTION_NAME")

    def vectorize_data(self, documents: dict) -> None:

        self.collection.add(documents=documents["content"], metadatas=documents["metadata"],ids=documents["ids"])

    def retrieve_relevant_references(self, query: str, top_k: int = 3) -> list[dict]:
        references = self.collection.query(query_texts = query, n_results = top_k)
        titles = [title["Header 1"] for title in references["metadatas"][0]]
        content = references["documents"][0]
        response = [{"title": title, "content": content, "source_file":f"{title}.md"} for title, content in zip(titles, content)]


        return response



# doc = DocumentLoader()
# doc_chunks = doc.run(Path("../data/compliance_references/logkeeping_requirements.md"))
# vector_store = VectorStore(Path("../data/compliance_db"), "compliance_references")
# vector_store.vectorize_data(doc_chunks)
# results = vector_store.collection.query(query_texts="Tell me what log entries should include", n_results=1)
# print(results["documents"])
