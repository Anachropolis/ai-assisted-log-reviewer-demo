from fastapi import FastAPI
from pathlib import Path
import json

LOGS = DATA = Path(__file__).resolve().parents[1] / "data" / "sample_input" / "operator_logs.json"


app = FastAPI(title="Operator Log API",
              description="Returns sample log entries from operators",
              version="1.0")

@app.get("/operator-logs/{log_id}")
async def get_logs(log_id) -> object:

    with open(LOGS, encoding="utf-8") as file:
            log_list = json.load(file)

    for log in log_list:
        if log_id.upper() == log["log_id"]:
            return log

    return {"no log found"}
