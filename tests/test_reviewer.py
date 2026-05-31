from review_module.reviewer import build_review_prompt, format_retrieved_context


def test_format_retrieved_context_includes_reference_content() -> None:
    references = [
        {
            "title": "Communication Failure Response",
            "source_file": "communication_failure_response.md",
            "section": "Required Information",
            "content": "The log should capture notification time and restoration status.",
        }
    ]

    formatted = format_retrieved_context(references)

    assert "Communication Failure Response" in formatted
    assert "communication_failure_response.md" in formatted
    assert "notification time" in formatted


def test_build_review_prompt_includes_log_and_context() -> None:
    log_entry = {
        "log_id": "LOG-1001",
        "event_type": "Communication Failure",
        "log_text": "Lost primary voice communication with Remote Station North.",
    }

    references = [
        {
            "title": "Communication Failure Response",
            "source_file": "communication_failure_response.md",
            "section": "Required Information",
            "content": "Capture affected facility and restoration status.",
        }
    ]

    prompt = build_review_prompt(log_entry, references)

    assert "LOG-1001" in prompt
    assert "Lost primary voice communication" in prompt
    assert "Communication Failure Response" in prompt
    assert "restoration status" in prompt