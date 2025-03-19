from typing import List, Dict, Optional, Any
from pydantic import Field
from .base import BaseEvent
from .enums import PlatformType

class DiscordEvent(BaseEvent):
    """Discord specific event model"""
    platform: PlatformType = PlatformType.DISCORD
    guild_id: str
    channel_id: str
    message_id: Optional[str] = None
    content: Optional[str] = None
    attachments: List[Dict[str, Any]] = Field(default_factory=list)
    mentions: List[str] = Field(default_factory=list)

    def __init__(self, **data):
        """Ensure event data is properly initialized from raw_data"""
        super().__init__(**data)
        
        raw_data = data.get("raw_data", {})

        self.content = raw_data.get("content") or self.content
        self.message_id = raw_data.get("id") or self.message_id
        self.attachments = raw_data.get("attachments", []) or self.attachments
        self.mentions = raw_data.get("mentions", []) or self.mentions
