from __future__ import annotations

import json

from .base import BaseAgent, OllamaUnavailableError
from .types import AgentInput, AgentOutput


class HookGenerator(BaseAgent):
    prompt_name = "hook_generator"

    @property
    def agent_name(self) -> str:
        return "HookGenerator"

    def run(self, request: AgentInput) -> AgentOutput:
        prompt_template = self.prompt_loader.load(request.language, self.prompt_name)
        composed_prompt = (
            f"{prompt_template}\n\n"
            f"שפת פלט: {request.language}\n"
            "החזר תשובה קצרה וברורה בפורמט טקסט.\n"
            f"קלט JSON:\n{json.dumps(request.data, ensure_ascii=False, indent=2)}"
        )

        try:
            llm_text = self.run_llm(composed_prompt)
            result = {
                "hook_text": llm_text,
                "source": "ollama",
                "received_keys": sorted(request.data.keys()),
            }
            metadata = {"status": "generated", "hebrew_first": True}
        except OllamaUnavailableError as exc:
            result = {
                "hook_text": "[Placeholder] לא ניתן להתחבר ל-Ollama כרגע.",
                "source": "fallback",
                "received_keys": sorted(request.data.keys()),
                "error": str(exc),
            }
            metadata = {"status": "fallback", "hebrew_first": True}

        return AgentOutput(
            agent=self.agent_name,
            language=request.language,
            prompt_template=prompt_template,
            input_data=request.data,
            result=result,
            metadata=metadata,
        )
