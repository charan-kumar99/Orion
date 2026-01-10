"""Gemini (Google Generative AI) client placeholder for Orion.

This module provides a simple wrapper `get_ai_response` that will
use the configured `GOOGLE_API_KEY`. Full Gemini integration can be
implemented here (for example using `google-generativeai`), but for
now this placeholder checks for the API key and returns `None` when
no key is present so the code falls back to other behaviors.
"""
import config

def get_ai_response(user_query, conversation_history=None):
    """Return an AI response using Google Gemini if configured.

    Currently a placeholder: returns None if no `GOOGLE_API_KEY` is set.
    Implement actual Gemini calls here when ready.
    """
    if not config.GOOGLE_API_KEY:
        return None

    # TODO: Implement real Gemini client using `google-generativeai`.
    # For now, return None so the assistant falls back to Wikipedia.
    return None


if __name__ == "__main__":
    if config.USE_GEMINI:
        print("Gemini is configured. Use `get_ai_response()` to query the model.")
    else:
        print("Gemini API key not configured. Add your API key to .env file.")