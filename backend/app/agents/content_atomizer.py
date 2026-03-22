from .base import BaseAgent


class ContentAtomizer(BaseAgent):
    prompt_name = "content_atomizer"

    @property
    def agent_name(self) -> str:
        return "ContentAtomizer"
