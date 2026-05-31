import json
from pathlib import Path
from reporters import FileWriter


def test_file_writer_creates_json_file(tmp_path: Path) -> None:
    output_path = tmp_path / "report.json"

    data = {
        "log_id": "LOG-1001",
        "summary": "Test summary",
        "possible_missing_information": ["Restoration time"],
    }

    writer = FileWriter()
    writer.run(output_path, data)

    assert output_path.exists()

    written_data = json.loads(output_path.read_text(encoding="utf-8"))

    assert written_data["log_id"] == "LOG-1001"
    assert written_data["summary"] == "Test summary"
    assert "Restoration time" in written_data["possible_missing_information"]
