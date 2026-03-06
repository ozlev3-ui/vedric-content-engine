from .base import BaseAgent


class HookGenerator(BaseAgent):
    prompt_name = "hook_generator"

    @property
    def agent_name(self) -> str:
        return "HookGenerator"
