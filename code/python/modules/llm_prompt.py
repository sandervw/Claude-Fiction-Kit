from pathlib import Path
import anthropic
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env", override=True)


def llm_prompt(message: str) -> str:
    """Send a prompt to Claude and return the response text."""

    client = anthropic.Anthropic()

    # Use 'claude-sonnet-4-6' for speed/cost balance
    # Use 'claude-opus-4-6' for highest quality
    MODEL = "claude-opus-4-6"

    response = client.messages.create(
        model=MODEL,
        max_tokens=20000,
        messages=[
            {
                "role": "user",
                "content": message,
            },
        ],
    )

    return response.content[0].text.strip()
