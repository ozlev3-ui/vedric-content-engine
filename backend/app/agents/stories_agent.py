from .base import BaseAgent


class StoriesAgent(BaseAgent):
    prompt_name = "stories_agent"

    @property
    def agent_name(self) -> str:
        return "StoriesAgent"
