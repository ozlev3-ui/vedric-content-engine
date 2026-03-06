from .base import BaseAgent


class ScenarioRefiner(BaseAgent):
    prompt_name = "scenario_refiner"

    @property
    def agent_name(self) -> str:
        return "ScenarioRefiner"
