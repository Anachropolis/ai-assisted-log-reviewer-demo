from langchain_text_splitters import MarkdownHeaderTextSplitter
import uuid_utils as uuid
from pathlib import Path


HEADERS = [("#", "Header 1"),
           ("##", "Header 2"),
           ("###", "Header 3"), ]


class DocumentLoader:

    def __init__(self) -> None:
        self.markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=HEADERS)

    def run(self, document: Path) -> dict:

        with open(document, encoding="utf-8") as file:
            document = file.read().rstrip()

        content = []
        metadata = []
        ids = []
        md_header_splits = self.markdown_splitter.split_text(document)
        for entry in md_header_splits:
            entry.id = str(uuid.uuid4())
            content.append(entry.page_content)
            metadata.append(entry.metadata)
            ids.append(entry.id)

        entries = {"content": content,
                   "metadata": metadata,
                   "ids": ids}



        return entries


# doc = DocumentLoader()
# chunked_doc = doc.run(Path("../data/compliance_references/SAMPLE_DATA_NOTES.md"))
#
# print(chunked_doc)



