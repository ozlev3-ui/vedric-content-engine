from .base import BaseAgent


class ReelsAgent(BaseAgent):
    prompt_name = "reels_agent"

    @property
    def agent_name(self) -> str:
        return "ReelsAgent"
