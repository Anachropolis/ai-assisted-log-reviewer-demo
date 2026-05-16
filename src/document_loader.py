from langchain_text_splitters import MarkdownHeaderTextSplitter
from pathlib import Path

HEADERS = [("#", "Header 1"),
           ("##", "Header 2"),
           ("###", "Header 3"), ]


class DocumentLoader:

    def __init__(self):
        self.markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=HEADERS)

    def run(self, document: Path):

        with open(document, encoding="utf-8") as file:
            document = file.read().rstrip()

        md_header_splits = self.markdown_splitter.split_text(document)
        return md_header_splits


doc = DocumentLoader()
print(doc.run(Path("../data/compliance_references/SAMPLE_DATA_NOTES.md")))


