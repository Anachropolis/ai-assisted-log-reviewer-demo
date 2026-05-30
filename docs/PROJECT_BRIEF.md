
# Project Brief

## Project Name

AI-Assisted Operator Log Review Demo


## Project Type

Python AI workflow / RAG demo / operational documentation support

## Current Version

The current version includes both a command-line workflow and a Streamlit dashboard.

The dashboard allows a reviewer to select an operator log, view retrieved reference material, run the AI-assisted review, and download the generated report.

## Target User

Operations teams, compliance reviewers, procedure owners, shift supervisors, documentation reviewers, and analysts who review operational log entries against internal references or documentation expectations.

## Problem

Operator logs often describe abnormal conditions, procedure use, communication issues, alarms, equipment status changes, and follow-up actions.

Reviewers may need to determine which reference documents are relevant and whether the log contains enough information for follow-up review.

Manual review can be repetitive, inconsistent, and time-consuming.

## Goal

Build a human-in-the-loop AI workflow that retrieves relevant reference material for a selected operator log and suggests possible missing information or follow-up questions.

## Inputs

- Operator log entry from mock API
- Local compliance-style markdown reference documents
- Environment variables for OpenAI and vector store configuration

## Outputs

- Structured JSON review report containing:
  - log summary
  - relevant references
  - why each reference may apply
  - possible missing information
  - suggested follow-up questions
  - human-review note

## Success Criteria

The tool should:

- Fetch a selected log entry from a mock API.
- Load and chunk local reference documents.
- Store reference chunks in a vector database.
- Retrieve relevant references based on log text.
- Send log and context to an LLM.
- Return structured JSON.
- Write the output to a report file.
- Avoid claiming to determine compliance.

## Business Value

This workflow reduces manual reference searching and helps reviewers focus on the parts of a log that may require clarification, documentation cleanup, or follow-up.

## Assumptions

- Sample logs are fictional.
- Reference documents are fictional and for demonstration only.
- The LLM output is advisory and requires human review.
- The system is not intended to replace compliance professionals or procedure owners.