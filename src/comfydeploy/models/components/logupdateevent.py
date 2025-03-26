"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .logdatacontent import LogDataContent, LogDataContentTypedDict
from comfydeploy.types import BaseModel
from comfydeploy.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal, Optional
from typing_extensions import Annotated, TypedDict


class LogUpdateEventTypedDict(TypedDict):
    data: LogDataContentTypedDict
    event: Literal["log_update"]


class LogUpdateEvent(BaseModel):
    data: LogDataContent

    EVENT: Annotated[
        Annotated[
            Optional[Literal["log_update"]],
            AfterValidator(validate_const("log_update")),
        ],
        pydantic.Field(alias="event"),
    ] = "log_update"
