# from .agent import Agent
from agentverse.registry import Registry

agent_registry = Registry(name="AgentRegistry")

from .base import BaseAgent
from .conversation_agent import ConversationAgent
from .tool_agent import ToolAgent
from .prisoner_dilema_agent import PoliceAgent, PrisonerAgent
from .agent_opr import AgentOPR
from .traffic_agent import TrafficAgent