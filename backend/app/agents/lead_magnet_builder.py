from .base import BaseAgent


class LeadMagnetBuilder(BaseAgent):
    prompt_name = "lead_magnet_builder"

    @property
    def agent_name(self) -> str:
        return "LeadMagnetBuilder"
