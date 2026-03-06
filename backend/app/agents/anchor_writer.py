from .base import BaseAgent


class AnchorWriter(BaseAgent):
    prompt_name = "anchor_writer"

    @property
    def agent_name(self) -> str:
        return "AnchorWriter"
