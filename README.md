
# AI-Assisted Operator Log Review Demo

A Python AI workflow demo that retrieves relevant compliance-style reference material for operator log entries and suggests missing information, follow-up questions, and review notes for human review.

This project demonstrates a retrieval-augmented generation (RAG) workflow for operational documentation review. It uses a mock operator log API, local reference documents, vector search, and an LLM to produce structured review guidance.

The tool does **not** determine compliance. It is designed as a human-in-the-loop assistant that helps reviewers identify relevant references and possible documentation gaps.

---

## Overview

Operations teams often create logs during abnormal conditions, communications issues, equipment status changes, procedure activations, and post-event reviews.

Those logs may need to be reviewed against internal procedures, compliance-style references, or documentation standards. Manually searching through reference material is time-consuming and can lead to missed follow-up items.

This project automates part of that review process by:

1. Pulling a fake operator log from a mock API.
2. Loading local compliance-style reference documents.
3. Indexing the reference documents in a vector database.
4. Retrieving reference sections relevant to the log entry.
5. Sending the log and retrieved context to an LLM.
6. Generating a structured review report.

The result is a decision-support report that helps a human reviewer focus on relevant references, possible missing information, and follow-up questions.

---

## Business Problem

Operational logs often contain important details about events, actions, notifications, equipment status, and follow-up work.

However, reviewing logs manually can be difficult when:

- Reference documentation is spread across multiple documents.
- The reviewer must search for relevant procedures or documentation expectations.
- Logs may omit key information such as notification times, restoration status, owners, or closeout details.
- The review process needs to be consistent and repeatable.
- The user needs guidance, not a raw document search result.

This project demonstrates how AI and retrieval can support that workflow without replacing human judgment.

---

## Solution

The tool uses a retrieval-augmented generation workflow.

Instead of asking the LLM to answer from memory, the project first retrieves relevant reference material from local documents. The retrieved context is then passed to the LLM along with the operator log.

The LLM is instructed to return structured JSON containing:

- A summary of the log entry
- Relevant reference documents
- Why each reference may apply
- Possible missing information
- Suggested follow-up questions
- A human-review note

This keeps the workflow focused, explainable, and grounded in retrieved reference material.

---

## Features

- Mock FastAPI endpoint for fake operator logs
- API client for pulling a specific log entry
- Markdown document loading and chunking
- Local vector database using ChromaDB
- Retrieval of relevant compliance-style reference sections
- OpenAI API integration
- Structured JSON review output
- Output report written to local file
- Environment variable support using `.env`
- Human-in-the-loop positioning to avoid overclaiming compliance decisions

---

## Tech Stack

- Python
- FastAPI / Uvicorn
- Requests
- ChromaDB
- OpenAI API
- LangChain document utilities
- python-dotenv

---

## Project Structure

```text
ai-assisted-log-review-demo/
│
├── src/
│   ├── app.py
│   ├── mock_log_api.py
│   ├── api_client.py
│   ├── document_loader.py
│   ├── vector_store.py
│   ├── llm_client.py
│   ├── reviewer.py
│   └── reporters.py
│
├── data/
│   ├── sample_input/
│   │   └── operator_logs.json
│   │
│   ├── compliance_references/
│   │   ├── communication_failure_response.md
│   │   ├── emergency_procedure_activation.md
│   │   ├── event_notification_requirements.md
│   │   ├── switching_and_work_control.md
│   │   ├── logkeeping_requirements.md
│   │   └── alarm_review_and_closeout.md
│   │
│   └── sample_output/
│       └── sample_log_review_report.json
│
├── docs/
│   ├── PROJECT_BRIEF.md
│   ├── WORKFLOW.md
│   ├── SAMPLE_OUTPUT.md
│   └── screenshots/
│
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
````

---

## How It Works

### 1. Mock Operator Log API

The project includes a mock FastAPI application that simulates an external system containing operator logs.

Example endpoint:

```text
GET /operator-logs/{log_id}
```

Example log entry:

```json
{
  "log_id": "LOG-1001",
  "timestamp": "2026-03-15T14:22:00",
  "operator": "Operator A",
  "facility": "Control Center Alpha",
  "event_type": "Communication Failure",
  "severity": "High",
  "log_text": "Lost primary voice communication with Remote Station North..."
}
```

In a real environment, this API could be replaced by an internal logging system, ticketing platform, operations database, or compliance review tool.

---

### 2. Compliance Reference Documents

The project includes fictional compliance-style markdown documents.

Example reference categories:

* Communication failure response
* Emergency procedure activation
* Event notification requirements
* Switching and work control documentation
* Operator logkeeping requirements
* Alarm review and closeout

These are demo documents only. They are not real regulatory guidance.

---

### 3. Document Loading and Vector Search

The reference documents are loaded from Markdown files and split into smaller chunks using LangChain document utilities. Those chunks are stored in a local ChromaDB collection.

When a log is reviewed, the log text is used as a search query against the vector database. The most relevant reference chunks are retrieved and passed into the LLM prompt.

---

### 4. LLM Review

The LLM receives:

* The operator log entry
* Retrieved reference material
* A structured review prompt
* Instructions not to determine compliance or invent facts

The expected output is structured JSON.

---

### 5. Report Generation

The final review result is written to a JSON file.

Example output path:

```text
data/sample_output/log_review_report.json
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-assisted-log-review-demo.git
cd ai-assisted-log-review-demo
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a local `.env` file

Copy the example file:

```bash
cp .env.example .env
```

On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Then open `.env` and add your OpenAI API key.

---

## Environment Variables

The project uses environment variables for API keys and configuration.

Example `.env.example`:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4.1-mini
EMBEDDING_MODEL=text-embedding-3-small
CHROMA_COLLECTION_NAME=operator-log-references
CHROMA_PERSIST_DIR=chroma_db
MOCK_API_BASE_URL=http://127.0.0.1:8000
```

Do not commit your real `.env` file to GitHub.

---

## Usage

This project runs in two terminals.

### Terminal 1: Start the mock log API

```bash
uvicorn src.mock_log_api:app --reload
```

The mock API will be available at:

```text
http://127.0.0.1:8000
```

FastAPI docs are available at:

```text
http://127.0.0.1:8000/docs
```

---

### Terminal 2: Run the log review workflow

Example:

```bash
python src/app.py \
  --log-id LOG-1001 \
  --endpoint operator-logs \
  --docs-dir data/compliance_references \
  --output data/sample_output/log_review_report.json
```

This command:

1. Fetches log `LOG-1001` from the mock API.
2. Loads local compliance reference documents.
3. Indexes the documents in ChromaDB.
4. Retrieves relevant reference sections.
5. Sends the log and retrieved context to the LLM.
6. Writes a structured review report to JSON.

---

## Example Terminal Output

```text
Fetching operator log...
Loading and indexing reference documents...
Retrieving relevant references...
Reviewing log entry...
Writing review report...

AI log review complete.
Log reviewed: LOG-1001
References retrieved: 3
Output file: data/sample_output/log_review_report.json
```

---

## Example Output

Example review output:

```json
{
  "log_id": "LOG-1001",
  "summary": "The operator documented loss of primary voice communication with Remote Station North and initiated alternate communication checks.",
  "relevant_references": [
    {
      "title": "Communication Failure Response",
      "source_file": "communication_failure_response.md",
      "why_relevant": "The log mentions loss of primary voice communication and alternate communication checks."
    },
    {
      "title": "Operator Logkeeping Requirements",
      "source_file": "logkeeping_requirements.md",
      "why_relevant": "The log describes an abnormal operational condition requiring clear status and follow-up documentation."
    }
  ],
  "possible_missing_information": [
    "Whether alternate communication was successfully established",
    "Time communication was restored, if applicable",
    "Field technician name or group responsible for confirmation",
    "Corrective action or ticket number, if one was created"
  ],
  "suggested_follow_up_questions": [
    "Was alternate communication with Remote Station North successfully established?",
    "At what time was communication restored?",
    "Who confirmed the remote station communication status?",
    "Was a corrective action or tracking record created?"
  ],
  "review_note": "This log appears related to communication failure response and general logkeeping requirements. Human review should confirm alternate communication status, restoration time, and follow-up ownership."
}
```


## Business Use Cases

This pattern could be adapted for:

* Operator log review
* Compliance documentation support
* Incident report review
* Maintenance log review
* Alarm review documentation
* Internal procedure reference search
* Shift turnover review
* Corrective action intake
* Audit preparation support
* SOP/documentation gap analysis

---

## What This Project Demonstrates

This project demonstrates my ability to:

* Build and consume a mock API
* Load and process operational log data
* Structure a retrieval-augmented generation workflow
* Use a vector database for reference retrieval
* Integrate an LLM into a practical business workflow
* Build human-in-the-loop AI tools
* Produce structured JSON outputs
* Keep AI responses grounded in retrieved reference material
* Design AI tools that support review rather than replace human judgment

---

## Portfolio Case Study

### Situation

Operational logs may need to be reviewed against internal procedures, compliance references, or documentation expectations. Manually searching reference material and identifying missing information can be slow and inconsistent.

### Task

The goal was to build a prototype AI workflow that retrieves relevant reference material for a selected operator log and produces structured review guidance for a human reviewer.

### Action

I built a Python application that pulls a log entry from a mock API, loads markdown reference documents, stores searchable document chunks in ChromaDB, retrieves relevant context, sends the log and context to an LLM, and writes a structured JSON review report.

### Result

The project demonstrates how retrieval-augmented generation can support operational documentation review by surfacing relevant references, possible missing information, and follow-up questions.

---

## Important Disclaimer

This project uses fictional sample data and fictional compliance-style reference documents.

It does not determine compliance, provide legal or regulatory advice, or replace qualified human review.

The purpose of the project is to demonstrate a human-in-the-loop AI workflow for operational documentation support.

---

## Future Improvements

Potential enhancements include:

* Add batch review for multiple logs
* Add a Streamlit or FastAPI frontend
* Add confidence scoring for retrieved references
* Add source chunk citations in the output
* Add improved document chunking and metadata extraction
* Add automated tests for document loading and retrieval
* Add retry/error handling for LLM responses
* Add JSON schema validation for model output
* Add support for PDF reference documents
* Add a separate indexing command for reference documents
* Add review history storage
* Add export to Markdown or Excel

````