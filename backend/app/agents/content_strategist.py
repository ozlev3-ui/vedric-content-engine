from .base import BaseAgent


class ContentStrategist(BaseAgent):
    prompt_name = "content_strategist"

    @property
    def agent_name(self) -> str:
        return "ContentStrategist"
