from __future__ import annotations

from .base import BaseAgent
from .content_scheduler import ContentScheduler
from .content_strategist import ContentStrategist
from .content_atomizer import ContentAtomizer
from .hook_generator import HookGenerator
from .anchor_writer import AnchorWriter
from .lead_magnet_builder import LeadMagnetBuilder
from .audience_architect import AudienceArchitect
from .posts_agent import PostsAgent
from .reels_agent import ReelsAgent
from .scenario_refiner import ScenarioRefiner
from .stories_agent import StoriesAgent


class AgentPipeline:
    """Simple orchestrator for the 11-agent Hebrew-first content pipeline."""

    def __init__(self) -> None:
        self.agents: list[BaseAgent] = [
            AudienceArchitect(),
            ContentStrategist(),
            ScenarioRefiner(),
            HookGenerator(),
            AnchorWriter(),
            LeadMagnetBuilder(),
            ContentAtomizer(),
            ReelsAgent(),
            StoriesAgent(),
            PostsAgent(),
            ContentScheduler(),
        ]

    def run(self, payload: dict, language: str = "he") -> list[dict]:
        results: list[dict] = []
        current_payload = payload
        for agent in self.agents:
            agent_output = agent.generate(current_payload, language=language)
            results.append(agent_output)
            current_payload = {
                "previous_result": agent_output["result"],
                "agent": agent_output["agent"],
            }
        return results
