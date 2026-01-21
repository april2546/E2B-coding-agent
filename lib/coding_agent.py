def clean_messages_for_llm(messages: list[dict]) -> list[dict]:
    return [{k: v for k, v in msg.items() if not k.startswith("_")} for msg in messages]
