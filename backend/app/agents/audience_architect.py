from .base import BaseAgent


class AudienceArchitect(BaseAgent):
    prompt_name = "audience_architect"

    @property
    def agent_name(self) -> str:
        return "AudienceArchitect"
