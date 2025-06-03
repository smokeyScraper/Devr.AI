from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)

class AgentState(BaseModel):
    """Base state for all LangGraph agents"""
    # Core identification
    session_id: str
    user_id: str
    platform: str  # discord, slack, github

    # Conversation context
    messages: List[Dict[str, Any]] = Field(default_factory=list)
    conversation_history: List[Dict[str, Any]] = Field(default_factory=list)
    context: Dict[str, Any] = Field(default_factory=dict)

    # Processing state
    current_task: Optional[str] = None
    task_result: Optional[Dict[str, Any]] = None
    next_action: Optional[str] = None

    # Tools and capabilities
    tools_used: List[str] = Field(default_factory=list)
    available_tools: List[str] = Field(default_factory=list)

    # Human-in-the-loop
    requires_human_review: bool = False
    human_feedback: Optional[str] = None

    # Platform-specific
    thread_id: Optional[str] = None
    channel_id: Optional[str] = None

    # Error handling
    errors: List[str] = Field(default_factory=list)
    retry_count: int = 0
    max_retries: int = 3

    # Response
    final_response: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True

class BaseAgent:
    """Base class for all LangGraph agents"""

    def __init__(self, agent_name: str, config: Dict[str, Any]):
        self.agent_name = agent_name
        self.config = config
        self.graph = None
        self._build_graph()

    def _build_graph(self):
        """Build the LangGraph workflow - to be implemented by subclasses"""
        raise NotImplementedError("Subclasses must implement _build_graph")

    async def run(self, initial_state: AgentState) -> AgentState:
        """Execute the agent workflow"""
        try:
            logger.info(f"Starting {self.agent_name} for session {initial_state.session_id}")
            result = await self.graph.ainvoke(initial_state.model_dump())
            return AgentState(**result)
        except Exception as e:
            logger.error(f"Error in {self.agent_name}: {str(e)}")
            initial_state.errors.append(str(e))
            return initial_state

    async def stream_run(self, initial_state: AgentState):
        """Stream the agent execution for real-time updates"""
        async for step in self.graph.astream(initial_state.model_dump()):
            yield step
