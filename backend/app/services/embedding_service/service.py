import logging
import os
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
from dotenv import load_dotenv
load_dotenv()

logger = logging.getLogger(__name__)


class EmbeddingItem(BaseModel):
    id: str
    collection: str
    content: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
    embedding: Optional[List[float]] = None