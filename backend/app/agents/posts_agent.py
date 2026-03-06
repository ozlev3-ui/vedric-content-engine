from .base import BaseAgent


class PostsAgent(BaseAgent):
    prompt_name = "posts_agent"

    @property
    def agent_name(self) -> str:
        return "PostsAgent"
