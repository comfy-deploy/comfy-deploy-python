"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .eventupdate import EventUpdate, EventUpdateTypedDict
from comfydeploy.types import BaseModel
from enum import Enum
import pydantic
from typing import Final, Optional, TypedDict
from typing_extensions import Annotated


class EventUpdateEventEvent(str, Enum):
    EVENT_UPDATE = "event_update"

class EventUpdateEventTypedDict(TypedDict):
    data: EventUpdateTypedDict
    

class EventUpdateEvent(BaseModel):
    data: EventUpdate
    EVENT: Annotated[Final[Optional[EventUpdateEventEvent]], pydantic.Field(alias="event")] = EventUpdateEventEvent.EVENT_UPDATE # type: ignore
    
