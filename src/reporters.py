from pathlib import Path
import json

class FileWriter:

    def run(self, output_path: str | Path, data: dict) -> str:
        """Write data to JSON file"""
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with output_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent = 2)

        return "Output file written"
