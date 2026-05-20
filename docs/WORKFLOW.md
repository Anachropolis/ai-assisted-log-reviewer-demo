# Workflow

## High-Level Workflow

```text
Mock Operator Log API
        ↓
Fetch Selected Log Entry
        ↓
Load Compliance Reference Documents
        ↓
Chunk Documents
        ↓
Store Chunks in Vector Database
        ↓
Retrieve Relevant Reference Sections
        ↓
Build Review Prompt
        ↓
Call LLM
        ↓
Generate Structured JSON Review Report
        ↓
Save Output File
```

## Step-by-Step Logic
### 1. Fetch log entry

The application requests a specific operator log from the mock API using the selected log_id.

Example:
```code
GET /operator-logs/LOG-1001
```
The response includes log metadata and log text.

### 2. Load reference documents

Markdown files are loaded from the compliance reference directory.

Each file represents a fictional reference document, such as:

- Communication Failure Response
- Emergency Procedure Activation
- Event Notification Requirements
- Switching and Work Control Documentation
- Operator Logkeeping Requirements
- Alarm Review and Closeout
### 3. Split documents into chunks

The documents are split into smaller sections for retrieval.

Each chunk should include useful metadata, such as:

- source file
- document title
- section heading
### 4. Store document chunks

The chunks are stored in a local ChromaDB collection.

For demo simplicity, the collection may be rebuilt during each run.

### 5. Retrieve relevant references

The selected log text is used as a query against the vector database.

The vector store returns the top relevant document chunks.

### 6. Build review prompt

The reviewer module combines:

- the operator log entry
- retrieved reference chunks
- output instructions
- safety instructions

The prompt tells the model not to determine compliance or invent facts.

### 7. Call LLM

The LLM client sends the system prompt and user prompt to the model.

The expected response is valid JSON.

### 8. Write review report

The output is written to a local JSON file.

Example:
```code
data/sample_output/log_review_report.json
```
## Human-in-the-Loop Design

This project is designed to assist a human reviewer.


The tool should not say:
```text
This log is compliant.
```
Instead, it should say:
```text
This log may relate to the following references.
The reviewer may want to confirm the following missing details.
```
That distinction is important for responsible use of AI in operational and compliance-adjacent workflows.

