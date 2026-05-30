from argparse import ArgumentParser
from api_module.api_client import ApiClient
from pathlib import Path
from ingest_module.document_loader import DocumentLoader
from review_module.llm_client import LLMClient
from ingest_module.vector_store import VectorStore
from review_module.reviewer import LogReviewer
from reporters import FileWriter





def cli():
    """Command Line Interface for generating AI report"""
    parser = ArgumentParser(description="AI Log Reviewer Demo")
    parser.add_argument("--log_id", default="LOG-1003", help="The unique id of the log")
    parser.add_argument("--endpoint", default="operator-logs", help="The API endpoint used to query logs")
    parser.add_argument("--docs_dir", default=Path("../data/compliance_references").resolve(), help="The directory containing compliance documents")
    parser.add_argument("--output", default=Path("../data/sample_output/log_review_report.json").resolve(), help="Output filepath with filename")

    return parser.parse_args()




def main():
    args = cli()

    docs_dir = args.docs_dir
    output_path = args.output


    api_client = ApiClient()
    document_loader = DocumentLoader()
    vector_store = VectorStore()
    llm_client = LLMClient()
    log_reviewer = LogReviewer(llm_client)
    file_writer = FileWriter()


    print("Fetching operator log...")
    log_entry = api_client.fetch_operator_log(args.endpoint, args.log_id)


    print("Loading and indexing documents...")
    vector_store.reset_collection()
    for document in Path(docs_dir).glob("*.md"):
        reference = document_loader.run(Path(document))
        vector_store.vectorize_data(reference)

    print("Retrieving relevant references...")
    relevant_references = vector_store.retrieve_relevant_references(log_entry["log_text"])

    print("Reviewing log entry...")
    review_result = log_reviewer.review_log_entry(log_entry, relevant_references)


    print("Writing review report...")
    output_message = file_writer.run(output_path, review_result)

    print("\nAI log review complete.")
    print(f"Log reviewed: {args.log_id}")
    print(f"References retrieved: {len(relevant_references)}")
    print(f"Output file: {output_path}")
    print(output_message)



if __name__ == "__main__":
    main()








