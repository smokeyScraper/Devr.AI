import logging
from typing import Dict, Any
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from ..shared.base_agent import BaseAgent, AgentState
from ..shared.classification_router import MessageCategory, ClassificationRouter
from .tools.search_tool import TavilySearchTool
from .tools.faq_tool import FAQTool
from app.core.config import settings

logger = logging.getLogger(__name__)

class DevRelAgent(BaseAgent):
    """DevRel LangGraph Agent for community support and engagement"""

    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.llm = ChatGoogleGenerativeAI(
            model=settings.devrel_agent_model,
            temperature=0.3,
            google_api_key=settings.gemini_api_key
        )
        self.search_tool = TavilySearchTool()
        self.faq_tool = FAQTool()
        super().__init__("DevRelAgent", self.config)

    def _build_graph(self):
        """Build the DevRel agent workflow graph"""
        workflow = StateGraph(AgentState)

        # Add nodes
        workflow.add_node("classify_intent", self._classify_intent)
        workflow.add_node("gather_context", self._gather_context)
        workflow.add_node("handle_faq", self._handle_faq)
        workflow.add_node("handle_web_search", self._handle_web_search)
        workflow.add_node("handle_technical_support", self._handle_technical_support)
        workflow.add_node("handle_onboarding", self._handle_onboarding)
        workflow.add_node("generate_response", self._generate_response)

        # Add edges
        workflow.add_edge("classify_intent", "gather_context")
        workflow.add_conditional_edges(
            "gather_context",
            self._route_to_handler,
            {
                "faq": "handle_faq",
                "web_search": "handle_web_search",
                "technical_support": "handle_technical_support",
                "onboarding": "handle_onboarding",
                "default": "handle_technical_support"
            }
        )

        # All handlers lead to response generation
        for node in ["handle_faq", "handle_web_search", "handle_technical_support", "handle_onboarding"]:
            workflow.add_edge(node, "generate_response")

        workflow.add_edge("generate_response", END)

        # Set entry point
        workflow.set_entry_point("classify_intent")

        self.graph = workflow.compile()

    async def _classify_intent(self, state: AgentState) -> AgentState:
        """Classify the user's intent and needs"""
        logger.info(f"Classifying intent for session {state.session_id}")

        # Get the latest message
        latest_message = ""
        if state.messages:
            latest_message = state.messages[-1].get("content", "")
        elif state.context.get("original_message"):
            latest_message = state.context["original_message"]

        # Use classification router
        router = ClassificationRouter(self.llm)

        classification = await router.classify_message(latest_message, state.context)

        # Update state with classification
        state.context.update({
            "classification": classification,
            "intent": classification["category"],
            "priority": classification["priority"]
        })

        state.current_task = "intent_classified"
        return state

    async def _gather_context(self, state: AgentState) -> AgentState:
        """Gather additional context for the user and their request"""
        logger.info(f"Gathering context for session {state.session_id}")

        # TODO: Add context gathering from databases
        # Currently, context is simple
        # In production, query databases for user history, etc.
        context_data = {
            "user_profile": {"user_id": state.user_id, "platform": state.platform},
            "conversation_context": len(state.messages),
            "session_info": {"session_id": state.session_id}
        }

        state.context.update(context_data)
        state.current_task = "context_gathered"
        return state

    async def _handle_faq(self, state: AgentState) -> AgentState:
        """Handle FAQ requests"""
        logger.info(f"Handling FAQ for session {state.session_id}")

        latest_message = ""
        if state.messages:
            latest_message = state.messages[-1].get("content", "")
        elif state.context.get("original_message"):
            latest_message = state.context["original_message"]

        faq_response = await self.faq_tool.get_response(latest_message)

        state.task_result = {
            "type": "faq",
            "response": faq_response,
            "source": "faq_database"
        }

        state.current_task = "faq_handled"
        return state

    async def _handle_web_search(self, state: AgentState) -> AgentState:
        """Handle web search requests"""
        logger.info(f"Handling web search for session {state.session_id}")

        latest_message = ""
        if state.messages:
            latest_message = state.messages[-1].get("content", "")
        elif state.context.get("original_message"):
            latest_message = state.context["original_message"]

        # Extract search query from message
        search_query = await self._extract_search_query(latest_message)

        # Perform search
        search_results = await self.search_tool.search(search_query)

        state.task_result = {
            "type": "web_search",
            "query": search_query,
            "results": search_results,
            "source": "tavily_search"
        }

        state.tools_used.append("tavily_search")
        state.current_task = "web_search_handled"
        return state

    async def _handle_technical_support(self, state: AgentState) -> AgentState:
        """Handle technical support requests"""
        logger.info(f"Handling technical support for session {state.session_id}")

        state.task_result = {
            "type": "technical_support",
            "action": "provide_guidance",
            "requires_human_review": False
        }

        state.current_task = "technical_support_handled"
        return state

    async def _handle_onboarding(self, state: AgentState) -> AgentState:
        """Handle onboarding requests"""
        logger.info(f"Handling onboarding for session {state.session_id}")

        state.task_result = {
            "type": "onboarding",
            "action": "welcome_and_guide",
            "next_steps": ["setup_environment", "first_contribution", "join_community"]
        }

        state.current_task = "onboarding_handled"
        return state

    async def _generate_response(self, state: AgentState) -> AgentState:
        """Generate final response to user"""
        logger.info(f"Generating response for session {state.session_id}")

        task_result = state.task_result or {}

        if task_result.get("type") == "faq":
            state.final_response = task_result.get("response", "I don't have a specific answer for that question.")

        elif task_result.get("type") == "web_search":
            response = await self._create_search_response(task_result)
            state.final_response = response

        else:
            # Use LLM to generate contextual response
            response = await self._create_llm_response(state, task_result)
            state.final_response = response

        state.current_task = "response_generated"
        return state

    def _route_to_handler(self, state: AgentState) -> str:
        """Route to appropriate handler based on classification"""
        intent = state.context.get("classification", {}).get("category", "")

        routing_map = {
            MessageCategory.FAQ: "faq",
            MessageCategory.WEB_SEARCH: "web_search",
            MessageCategory.ONBOARDING: "onboarding",
            MessageCategory.TECHNICAL_SUPPORT: "technical_support",
            MessageCategory.COMMUNITY_ENGAGEMENT: "technical_support",
            MessageCategory.DOCUMENTATION: "technical_support",
            MessageCategory.BUG_REPORT: "technical_support",
            MessageCategory.FEATURE_REQUEST: "technical_support"
        }

        return routing_map.get(intent, "default")

    async def _extract_search_query(self, message: str) -> str:
        """Extract search query from user message"""
        # Simple extraction - in production, use LLM for better extraction
        search_indicators = ["search for", "look up", "find information about", "research"]

        message_lower = message.lower()
        for indicator in search_indicators:
            if indicator in message_lower:
                # Extract text after the indicator
                start_idx = message_lower.find(indicator) + len(indicator)
                query = message[start_idx:].strip()
                return query

        # Fallback: use the entire message as query
        return message

    async def _create_search_response(self, task_result: Dict[str, Any]) -> str:
        """Create response from search results"""
        query = task_result.get("query", "")
        results = task_result.get("results", [])

        if not results:
            return f"I searched for '{query}' but couldn't find any relevant information. Could you try rephrasing your question?"

        response = f"I found some information about '{query}':\n\n"

        for i, result in enumerate(results[:3], 1):  # Show top 3 results
            title = result.get("title", "")
            content = result.get("content", "")
            url = result.get("url", "")

            response += f"**{i}. {title}**\n"
            if content:
                # Truncate content to keep response manageable
                content_preview = content[:300] + "..." if len(content) > 300 else content
                response += f"{content_preview}\n"
            if url:
                response += f"🔗 [Read more]({url})\n\n"

        response += "Is there anything specific from these results you'd like me to explain further?"

        return response

    async def _create_llm_response(self, state: AgentState, task_result: Dict[str, Any]) -> str:
        """Create response using LLM"""
        try:
            latest_message = ""
            if state.messages:
                latest_message = state.messages[-1].get("content", "")
            elif state.context.get("original_message"):
                latest_message = state.context["original_message"]

            system_prompt = """You are a helpful DevRel (Developer Relations) assistant for Devr.AI, an AI-powered developer relations platform. 
            
            Your role is to:
            - Help developers with technical questions
            - Guide new users through onboarding
            - Provide information about the platform
            - Be friendly, helpful, and knowledgeable
            
            Keep responses concise but informative. If you don't know something specific, it's okay to say so and offer to help find the information."""

            prompt = f"""System: {system_prompt}

User Query: {latest_message}

Context: {task_result.get('type', 'general')} request

Please provide a helpful response:"""

            response = await self.llm.ainvoke([HumanMessage(content=prompt)])
            return response.content

        except Exception as e:
            logger.error(f"Error generating LLM response: {str(e)}")
            return "I'm having trouble processing your request right now. Please try again or rephrase your question."
