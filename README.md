# AI-Assisted Operator Log Review Demo

A Python RAG application that helps human reviewers evaluate operational log entries against compliance-style reference documentation.

The project uses a mock FastAPI log source, a document ingestion pipeline, ChromaDB vector search, an OpenAI-powered review workflow, and a Streamlit dashboard for viewing and exporting structured review reports.

This tool does **not** determine compliance. It is designed as a human-in-the-loop assistant that retrieves potentially relevant reference material and suggests follow-up items for qualified review.

---

## Project Overview

Operations teams often create logs during abnormal conditions, communication issues, equipment status changes, procedure activations, alarm reviews, and post-event follow-up.

Those logs may need to be reviewed against internal procedures, documentation standards, or compliance-style references. Manually searching reference material can be slow and inconsistent, especially when logs omit details such as notification time, final status, owner, approval, restoration time, or corrective action tracking.

This project demonstrates how retrieval-augmented generation can support that workflow by:

1. Pulling a selected operator log from a mock API.
2. Retrieving relevant reference documentation from a local vector store.
3. Sending the log and retrieved context to an LLM.
4. Producing a structured review report.
5. Displaying the result in a Streamlit dashboard.

---

## Project Components

This project includes four related components.

### 1. Mock Operator Log API

Located in `src/api_module/`, this FastAPI service simulates an external operator log system.

Example endpoint:

```text
GET /operator-logs/{log_id}
```

### 2. Reference Document Ingestion

Located in `src/ingest_module/`, this workflow loads compliance-style markdown documents, splits them into chunks, and stores them in ChromaDB.

### 3. AI Review Workflow

Located in `src/review_module/`, this workflow combines an operator log with retrieved reference context and sends it to an LLM for structured review output.

### 4. Streamlit Dashboard

Located in `src/streamlit_app_homepage.py` and `src/pages/`, this interface lets reviewers select logs, run reviews, view generated reports, and export results.

---

## Features

- Mock FastAPI endpoint for fictional operator logs
- API client for pulling a selected log entry
- Markdown document loading and chunking
- ChromaDB vector store for reference retrieval
- OpenAI API integration for structured review generation
- Streamlit dashboard for user-facing review
- JSON review report output
- Environment variable support using `.env`
- Human-in-the-loop design that avoids compliance overclaiming

---

## Tech Stack

- Python
- FastAPI / Uvicorn
- Streamlit
- ChromaDB
- OpenAI API
- LangChain document utilities
- Requests
- python-dotenv
- Pydantic

---

## Project Structure

```text
ai-assisted-log-reviewer-demo/
│
├── README.md
├── pyproject.toml
├── .env.example
├── .gitignore
│
├── data/
│   ├── sample_input/
│   │   └── operator_logs.json
│   │
│   ├── compliance_references/
│   │   ├── alarm_review_and_closeout.md
│   │   ├── communication_failure_response.md
│   │   ├── emergency_procedure_activation.md
│   │   ├── event_notification_requirements.md
│   │   ├── logkeeping_requirements.md
│   │   └── switching_and_work_control.md
│   │
│   └── sample_output/
│       └──  sample_log_review_report.json
│  
│
├── docs/
│   ├── PROJECT_BRIEF.md
│   ├── WORKFLOW.md
│   ├── SAMPLE_OUTPUT.md
│   ├── CHANGELOG.md
│   │
│   ├── architecture/
│   │   └── project_architecture.png
│   │
│   └── screenshots/
│       ├── streamlit_homepage.png
│       ├── streamlit_report_page.png
│       ├── mock_api_docs.png
│       └── sample_output_report.png
│
├── src/
│   ├── app.py
│   ├── streamlit_app_homepage.py
│   ├── reporters.py
│   │
│   ├── api_module/
│   │   ├── __init__.py
│   │   ├── api_client.py
│   │   └── mock_log_api.py
│   │
│   ├── ingest_module/
│   │   ├── __init__.py
│   │   ├── document_loader.py
│   │   ├── ingest_documents.py
│   │   └── vector_store.py
│   │
│   ├── review_module/
│   │   ├── __init__.py
│   │   ├── llm_client.py
│   │   └── reviewer.py
│   │
│   ├── ui_features/
│   │   ├── __init__.py
│   │   └── ui_features.py
│   │
│   └── pages/
│       └── streamlit_report.py
│
└── tests/
    ├── test_document_loader.py
    ├── test_reviewer.py
    └── test_reporters.py

```

---

## How It Works

### 1. Mock Log API

The mock API returns fictional operator logs.

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

In a real environment, this API could be replaced with an internal logging system, ticketing platform, operations database, or compliance review tool.

### 2. Reference Document Ingestion

The project includes fictional compliance-style markdown documents. These documents are loaded, split into chunks using LangChain document utilities, and stored in ChromaDB.

Example reference categories:

- Communication failure response
- Emergency procedure activation
- Event notification requirements
- Switching and work control documentation
- Operator logkeeping requirements
- Alarm review and closeout

### 3. Vector Retrieval

When a log is reviewed, the log text is used as a query against the vector database. The most relevant reference chunks are retrieved and passed into the LLM prompt.

### 4. LLM Review

The LLM receives:

- the selected operator log entry
- retrieved reference material
- a structured review prompt
- instructions not to determine compliance or invent facts

The expected output is structured JSON.

### 5. Dashboard and Report Output

The Streamlit dashboard displays:

- the selected log
- the generated review
- relevant references
- possible missing information
- suggested follow-up questions
- review notes

The review can also be written to JSON.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-assisted-log-reviewer-demo.git
cd ai-assisted-log-reviewer-demo
```

### 2. Create and activate a virtual environment

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

This project uses `pyproject.toml` for dependency management.

```bash
pip install -e .
```

If you maintain a separate `requirements.txt`, you can instead run:

```bash
pip install -r requirements.txt
```

Use one dependency source consistently to avoid drift.

---

## Environment Setup

Copy the example environment file:

```bash
cp .env.example .env
```

On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Then open `.env` and add your OpenAI API key.

Example `.env.example`:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4.1-mini
EMBEDDING_MODEL=text-embedding-3-small
CHROMA_COLLECTION_NAME=operator-log-references
CHROMA_PERSIST_DIR=data/chroma_db
MOCK_API_BASE_URL=http://127.0.0.1:8000
```

Do not commit your real `.env` file to GitHub.

---

## Usage

This project has three main steps.

### Step 1: Start the mock log API

From the project root:

```bash
uvicorn src.api_module.mock_log_api:app --reload
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

### Step 2: Ingest reference documents

Before running reviews, load the reference documents into ChromaDB:

```bash
python src/ingest_module/ingest_documents.py \
  --docs-dir data/compliance_references \
  --reset
```

This command loads the markdown reference documents, chunks them, and stores them in the local vector database.

---

### Step 3A: Run the Streamlit dashboard

```bash
streamlit run src/streamlit_app_homepage.py
```

The dashboard lets a user:

- view available operator logs
- select a log for review
- run the AI-assisted review workflow
- view the generated report
- inspect suggested missing information and follow-up questions

---

### Step 3B: Run the CLI workflow

The project can also be run from the command line:

```bash
python src/app.py \
  --log-id LOG-1001 \
  --endpoint operator-logs \
  --output data/sample_output/log_review_report.json
```

The CLI workflow fetches the selected log, retrieves relevant reference material, calls the LLM review workflow, and writes the output to JSON.

---

## Example Terminal Output

```text
Fetching operator log...
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

---
## Running Tests

Install development dependencies:

```bash
pip install -e ".[dev]"
```

Perform test:
```bash
pytest
```
___

## Business Use Cases

This pattern could be adapted for:

- Operator log review
- Compliance documentation support
- Incident report review
- Maintenance log review
- Alarm review documentation
- Internal procedure reference search
- Shift turnover review
- Corrective action intake
- Audit preparation support
- SOP/documentation gap analysis

---

## What This Project Demonstrates

This project demonstrates my ability to:

- Build and consume a mock API
- Create a document ingestion workflow
- Use vector search for reference retrieval
- Build a retrieval-augmented generation workflow
- Integrate an LLM into a practical business process
- Package an AI workflow into a Streamlit dashboard
- Produce structured JSON review output
- Design human-in-the-loop AI tools
- Keep AI responses grounded in retrieved reference material

---

## Portfolio Case Study

### Situation

Operational logs may need to be reviewed against internal procedures, compliance references, or documentation expectations. Manually searching reference material and identifying missing information can be slow and inconsistent.

### Task

The goal was to build a prototype AI workflow that retrieves relevant reference material for a selected operator log and produces structured review guidance for a human reviewer.

### Action

I built a Python application that pulls log entries from a mock API, loads markdown reference documents, stores searchable document chunks in ChromaDB, retrieves relevant context, sends the log and context to an LLM, and displays the structured review result in a Streamlit dashboard.

### Result

The project demonstrates how retrieval-augmented generation can support operational documentation review by surfacing relevant references, possible missing information, suggested follow-up questions, and review notes.

---

## Important Disclaimer

This project uses fictional sample data and fictional compliance-style reference documents.

It does not determine compliance, provide legal or regulatory advice, or replace qualified human review.

The purpose of the project is to demonstrate a human-in-the-loop AI workflow for operational documentation support.

---

## Future Improvements

Potential enhancements include:

- Add batch review for multiple logs
- Add source chunk citations in the output
- Add improved document chunking and metadata extraction
- Add automated tests for document loading and retrieval
- Add retry/error handling for LLM responses
- Add JSON schema validation for model output
- Add support for PDF reference documents
- Add review history storage
- Add export to Markdown or Excel
- Add Docker support for local multi-service execution
- Add webhook-triggered review workflow




