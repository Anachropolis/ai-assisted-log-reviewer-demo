from argparse import ArgumentParser
from api_client import ApiClient
from pathlib import Path
from document_loader import DocumentLoader
from llm_client import LLMClient
from vector_store import VectorStore
from reviewer import LogReviewer
import glob
import json




def cli():
    parser = ArgumentParser(description="AI Log Reviewer Demo")
    parser.add_argument("--log_id", help="The unique id of the log")
    parser.add_argument("--endpoint", help="The API endpoint used to query logs")
    parser.add_argument("--docs_dir", help="The directory containing compliance documents")
    parser.add_argument("--output", help="Output filepath with filename")

    return parser.parse_args()




def main():
    args = cli()
    log_id = args.log_id
    endpoint = args.endpoint
    docs_dir = args.docs_dir
    output_path = args.output
    api_client = ApiClient()
    log_entry = api_client.fetch_operator_log(endpoint, log_id)
    document_loader = DocumentLoader()
    vector_store = VectorStore()
    llm_client = LLMClient()


    for document in glob.glob(f"{docs_dir.rstrip("/")}/*.md"):
        reference = document_loader.run(Path(document))
        vector_store.vectorize_data(reference)


    relevant_references = vector_store.retrieve_relevant_references(log_entry["log_text"])

    reviewer = LogReviewer(llm_client).review_log_entry(log_entry, relevant_references)

    output_directory = Path(output_path).parent
    Path(output_directory).mkdir(parents=True, exist_ok=True)

    with open(output_path, "w") as file:
        json.dump(reviewer, file)


if __name__ == "__main__":
    main()








