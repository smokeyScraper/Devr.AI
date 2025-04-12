

import asyncio
import uuid
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router  
import uvicorn
from .app.core.events.event_bus import EventBus
from .app.core.events.enums import EventType, PlatformType
from .app.core.events.base import BaseEvent
from .app.core.handler.handler_registry import HandlerRegistry

app = FastAPI()


# CORS Configuration

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],  
)


app.include_router(router, prefix="/api")  

# Initialize Handler Registry and Event Bus
handler_registry = HandlerRegistry()
event_bus = EventBus(handler_registry)



app.include_router(router, prefix="/api")  

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
    asyncio.run(main())


