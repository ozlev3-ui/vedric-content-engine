from .base import BaseAgent


class ContentScheduler(BaseAgent):
    prompt_name = "content_scheduler"

    @property
    def agent_name(self) -> str:
        return "ContentScheduler"
