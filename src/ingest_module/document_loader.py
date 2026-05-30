from langchain_text_splitters import MarkdownHeaderTextSplitter
import uuid
from pathlib import Path


HEADERS = [("#", "Header 1"),
           ("##", "Header 2"),
           ("###", "Header 3"), ]


class DocumentLoader:

    def __init__(self) -> None:
        self.markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=HEADERS)

    def run(self, document_path: Path) -> dict:

        with open(document_path, encoding="utf-8") as file:
            document_text = file.read().rstrip()

        content = []
        metadata = []
        ids = []
        md_header_splits = self.markdown_splitter.split_text(document_text)

        for entry in md_header_splits:
            chunk_id = str(uuid.uuid4())
            chunk_metadata = entry.metadata.copy()
            chunk_metadata["source_file"] = document_path.name

            content.append(entry.page_content)
            metadata.append(chunk_metadata)
            ids.append(chunk_id)

        return {"content": content,
                   "metadata": metadata,
                   "ids": ids}





