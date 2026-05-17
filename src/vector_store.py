import chromadb
from pathlib import Path


client = chromadb.PersistentClient(path="../data/compliance_references/compliance_db")
collection = client.get_or_create_collection("compliance_references")

class VectorStore:

    def __init__(self, file_path: Path, entry: str) -> None:
        self.client = chromadb.PersistentClient(file_path)
        self.collection = client.get_or_create_collection(entry)

    def vectorize_data(self, documents: dict) -> None:

        self.collection.add(documents=documents["content"], metadatas=documents["metadata"],ids=documents["ids"])

    def retrieve_relevant_references(self, query: str, top_k: int = 3) -> object:
        references = self.collection.query(query_texts = query, n_results = top_k)
        return references



# doc = DocumentLoader()
# doc_chunks = doc.run(Path("../data/compliance_references/logkeeping_requirements.md"))
# vector_store = VectorStore(Path("../data/compliance_db"), "compliance_references")
# vector_store.vectorize_data(doc_chunks)
# results = vector_store.collection.query(query_texts="Tell me what log entries should include", n_results=1)
# print(results["documents"])
