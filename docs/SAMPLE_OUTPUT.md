
# Sample Output

The main output is a structured JSON review report.

## Output Fields

| Field | Description |
|---|---|
| `log_id` | Unique identifier of the reviewed log |
| `summary` | Plain-English summary of the log entry |
| `relevant_references` | Retrieved references that may apply to the log |
| `possible_missing_information` | Details that may need clarification |
| `suggested_follow_up_questions` | Questions a reviewer may ask |
| `review_note` | Human-readable review guidance |

## Example

```json
{
  "log_id": "LOG-1001",
  "summary": "The operator documented loss of primary voice communication with Remote Station North and initiated alternate communication checks.",
  "relevant_references": [
    {
      "title": "Communication Failure Response",
      "source_file": "communication_failure_response.md",
      "why_relevant": "The log mentions loss of primary voice communication and alternate communication checks."
    }
  ],
  "possible_missing_information": [
    "Whether alternate communication was successfully established",
    "Time communication was restored, if applicable",
    "Corrective action or ticket number, if one was created"
  ],
  "suggested_follow_up_questions": [
    "Was alternate communication with Remote Station North successfully established?",
    "At what time was communication restored?",
    "Was a corrective action or tracking record created?"
  ],
  "review_note": "This log appears related to communication failure response. Human review should confirm alternate communication status, restoration time, and follow-up ownership."
}