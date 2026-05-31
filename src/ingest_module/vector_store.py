import chromadb
import os
from dotenv import load_dotenv



load_dotenv()


class VectorStore:

    def __init__(self) -> None:
        self.persist_dir = os.getenv("CHROMA_PERSIST_DIR", "../data/chroma_db")
        self.collection_name = os.getenv("CHROMA_COLLECTION_NAME", "compliance_references")

        self.client = chromadb.PersistentClient(path=self.persist_dir)
        self.collection = self.client.get_or_create_collection(self.collection_name)



    def vectorize_data(self, documents: dict) -> None:
        """Converts data into vector format and store in DB"""
        self.collection.add(documents=documents["content"],
                            metadatas=documents["metadata"],
                            ids=documents["ids"])



    def retrieve_relevant_references(self, query: str, top_k: int = 3) -> list[dict]:
        """Retrieves relevant references from a query"""
        results = self.collection.query(query_texts = query,
                                        n_results = top_k)
        references = []
        documents = results["documents"][0]
        metadatas = results["metadatas"][0]

        for document, metadata in zip(documents, metadatas):
            references.append({
                "title" : metadata.get("Header 1", "Unknown Reference"),
                "section": metadata.get("Header 2", ""),
                "source_file": metadata.get("source_file", "Unknown"),
                "content": document,
            })

        return references



    def reset_collection(self) -> None:
        """Resets collection"""
        collection_name = os.getenv("CHROMA_COLLECTION_NAME", "compliance_references")
        try:
            self.client.delete_collection(collection_name)
        except Exception:
            pass

        self.collection = self.client.get_or_create_collection(self.collection_name)




