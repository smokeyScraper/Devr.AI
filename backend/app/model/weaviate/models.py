from pydantic import BaseModel, Field
from typing import List


class WeaviateUserProfile(BaseModel):
    """
    Represents a vectorized user profile for semantic search in Weaviate.
    """
    supabase_user_id: str = Field(..., alias="supabaseUserId")
    profile_summary: str = Field(..., alias="profileSummary")
    primary_languages: List[str] = Field(..., alias="primaryLanguages")
    expertise_areas: List[str] = Field(..., alias="expertiseAreas")
    embedding: List[float] = Field(..., description="384-dimensional vector")


class WeaviateCodeChunk(BaseModel):
    """
    Vectorized representation of code chunks stored in Weaviate.
    """
    supabase_chunk_id: str = Field(..., alias="supabaseChunkId")
    code_content: str = Field(..., alias="codeContent")
    language: str
    function_names: List[str] = Field(..., alias="functionNames")
    embedding: List[float] = Field(..., description="384-dimensional vector")


class WeaviateInteraction(BaseModel):
    """
    Vectorized interaction representation stored in Weaviate.
    """
    supabase_interaction_id: str = Field(..., alias="supabaseInteractionId")
    conversation_summary: str = Field(..., alias="conversationSummary")
    platform: str
    topics: List[str]
    embedding: List[float] = Field(..., description="384-dimensional vector")
