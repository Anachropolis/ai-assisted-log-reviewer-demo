from fastapi import FastAPI
from pathlib import Path
import json

LOGS = Path(__file__).resolve().parents[1] / "data" / "sample_input" / "operator_logs.json"


app = FastAPI(title="Operator Log API",
              description="Returns sample log entries from operators",
              version="1.0")

@app.get("/operator-logs")
def get_operator_logs() -> list[dict]:
    with open(LOGS) as file:
        log_list = json.load(file)

    return log_list

@app.get("/operator-logs/{log_id}")
async def get_logs(log_id) -> object:

    log_list = get_operator_logs()

    for log in log_list:
        if log_id.upper() == log["log_id"]:
            return log

    return {"no log found"}
