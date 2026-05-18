from api_client import ApiClient
from pathlib import Path
from document_loader import DocumentLoader
from src.llm_client import LLMClient
from vector_store import VectorStore
from reviewer import LogReviewer
import glob



api_client = ApiClient()
log_entry = api_client.fetch_operator_log("operator-logs", "LOG-1007")
# log_entry = json.dumps(log_entry)
# print(log_entry)
document_loader = DocumentLoader()
vector_store = VectorStore()
llm_client = LLMClient()

# for document in glob.glob("../data/compliance_references/*.md"):
#     reference = document_loader.run(Path(document))
#     vector_store.vectorize_data(reference)


relevant_references = vector_store.retrieve_relevant_references(log_entry["log_text"])



reviewer = LogReviewer(llm_client).review_log_entry(log_entry, relevant_references)

print(reviewer)





