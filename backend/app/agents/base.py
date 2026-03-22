from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

from ..ai.llm import OllamaUnavailableError, generate_text

from .types import AgentInput, AgentOutput, StructuredPayload


class PromptLoader:
    """Loads prompt templates from backend/app/ai/prompts."""

    def __init__(self, prompts_root: Path | None = None) -> None:
        if prompts_root is None:
            prompts_root = Path(__file__).resolve().parent.parent / "ai" / "prompts"
        self.prompts_root = prompts_root

    def load(self, language: str, prompt_name: str) -> str:
        prompt_path = self.prompts_root / language / f"{prompt_name}.txt"
        if not prompt_path.exists():
            fallback_path = self.prompts_root / "he" / f"{prompt_name}.txt"
            if fallback_path.exists():
                return fallback_path.read_text(encoding="utf-8").strip()
            raise FileNotFoundError(f"Prompt template not found: {prompt_path}")

        return prompt_path.read_text(encoding="utf-8").strip()


class BaseAgent(ABC):
    """Base class for modular agents in the content pipeline."""

    prompt_name: str

    def __init__(self, prompt_loader: PromptLoader | None = None) -> None:
        self.prompt_loader = prompt_loader or PromptLoader()

    @property
    @abstractmethod
    def agent_name(self) -> str:
        """A stable name for the current agent."""

    def generate(self, payload: StructuredPayload, language: str = "he") -> StructuredPayload:
        """User-facing API: structured input -> structured output."""
        output = self.run(AgentInput(data=payload, language=language))
        return {
            "agent": output.agent,
            "language": output.language,
            "prompt_template": output.prompt_template,
            "input": output.input_data,
            "result": output.result,
            "metadata": output.metadata,
        }

    def run_llm(self, prompt: str) -> str:
        """Run a prompt against Ollama and return generated text."""
        return generate_text(prompt)

    def run(self, request: AgentInput) -> AgentOutput:
        prompt_template = self.prompt_loader.load(request.language, self.prompt_name)
        result = self._build_placeholder_result(request.data)
        return AgentOutput(
            agent=self.agent_name,
            language=request.language,
            prompt_template=prompt_template,
            input_data=request.data,
            result=result,
            metadata={"status": "placeholder", "hebrew_first": True},
        )

    def _build_placeholder_result(self, payload: StructuredPayload) -> StructuredPayload:
        return {
            "summary": f"Placeholder output for {self.agent_name}",
            "next_step": "Replace placeholder logic with LLM execution in a future iteration.",
            "received_keys": sorted(payload.keys()),
        }


__all__ = ["BaseAgent", "PromptLoader", "OllamaUnavailableError"]
