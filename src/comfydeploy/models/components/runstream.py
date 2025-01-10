"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .eventupdateevent import EventUpdateEvent, EventUpdateEventTypedDict
from .logupdateevent import LogUpdateEvent, LogUpdateEventTypedDict
from comfydeploy.utils import get_discriminator
from pydantic import Discriminator, Tag
from typing import Union
from typing_extensions import Annotated, TypeAliasType


RunStreamTypedDict = TypeAliasType(
    "RunStreamTypedDict", Union[LogUpdateEventTypedDict, EventUpdateEventTypedDict]
)


RunStream = Annotated[
    Union[
        Annotated[EventUpdateEvent, Tag("event_update")],
        Annotated[LogUpdateEvent, Tag("log_update")],
    ],
    Discriminator(lambda m: get_discriminator(m, "event", "event")),
]