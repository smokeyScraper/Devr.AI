from typing import Dict, Any, AsyncGenerator
from abc import ABC, abstractmethod
import logging
from .state import AgentState

logger = logging.getLogger(__name__)

class BaseAgent(ABC):
    """Base class for all LangGraph agents"""

    def __init__(self, agent_name: str, config: Dict[str, Any]):
        self.agent_name = agent_name
        self.config = config
        self.graph = None
        self._build_graph()

    @abstractmethod
    def _build_graph(self):
        """Build the LangGraph workflow - to be implemented by subclasses"""
        pass

    async def run(self, initial_state: AgentState) -> AgentState:
        """Execute the agent workflow"""
        try:
            logger.info("Starting %s for session %s", self.agent_name, initial_state.session_id)
            result = await self.graph.ainvoke(initial_state.model_dump())
            return AgentState(**result)
        except AttributeError as e:
            logger.error("Graph not properly initialized for %s: %s", self.agent_name, str(e))
            state_dict = initial_state.model_dump()
            state_dict['errors'].append(f"Agent initialization error: {str(e)}")
            return AgentState(**state_dict)
        except Exception as e:
            logger.error("Error in %s: %s", self.agent_name, str(e))
            state_dict = initial_state.model_dump()
            state_dict['errors'].append(str(e))
            return AgentState(**state_dict)

    async def stream_run(self, initial_state: AgentState) -> AsyncGenerator[Dict[str, Any], None]:
        """Stream the agent execution for real-time updates"""
        try:
            if not self.graph:
                raise AttributeError("Graph not properly initialized")
            async for step in self.graph.astream(initial_state.model_dump()):
                yield step
        except Exception as e:
            logger.error("Error in %s stream: %s", self.agent_name, str(e))
            yield {"error": str(e)}
