from pathlib import Path
from ingest_module.document_loader import DocumentLoader


def test_document_loader_creates_chunks(tmp_path: Path) -> None:
    sample_doc = tmp_path / "sample_reference.md"

    sample_doc.write_text("""#Communication Failure Response
    
    This reference describes communication failure documentation expectations.

    ## Required Information

    The log should capture notification time, affected facility, and restoration status.   
    """, encoding="utf-8")

    loader = DocumentLoader()
    result = loader.run(sample_doc)

    assert "content" in result
    assert "metadata" in result
    assert "ids" in result

    assert len(result["content"]) > 0
    assert len(result["content"]) == len(result["metadata"])
    assert len(result["content"]) == len(result["ids"])

    assert result["metadata"][0]["source_file"] == "sample_reference.md"