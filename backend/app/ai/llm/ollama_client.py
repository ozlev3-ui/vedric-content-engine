from __future__ import annotations

import os

import requests

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
DEFAULT_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:7b")


class OllamaUnavailableError(RuntimeError):
    """Raised when Ollama cannot be reached or returns an invalid response."""


class OllamaClient:
    def __init__(self, base_url: str = OLLAMA_URL, model: str = DEFAULT_MODEL, timeout: int = 60) -> None:
        self.base_url = base_url
        self.model = model
        self.timeout = timeout

    def generate_text(self, prompt: str) -> str:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
        }

        try:
            response = requests.post(self.base_url, json=payload, timeout=self.timeout)
            response.raise_for_status()
        except requests.RequestException as exc:
            raise OllamaUnavailableError(
                "Ollama API is unavailable. Ensure Ollama is running on localhost:11434."
            ) from exc

        try:
            data = response.json()
        except ValueError as exc:
            raise OllamaUnavailableError("Ollama returned a non-JSON response.") from exc

        generated = data.get("response")
        if not isinstance(generated, str) or not generated.strip():
            raise OllamaUnavailableError("Ollama response did not include generated text.")

        return generated.strip()


def generate_text(prompt: str) -> str:
    """Convenience function for simple generate calls."""
    return OllamaClient().generate_text(prompt)
