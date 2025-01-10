"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from comfydeploy.types import BaseModel
from typing import TypedDict


class IncreaseTimeoutBodyTypedDict(TypedDict):
    machine_id: str
    session_id: str
    timeout: int
    gpu: str
    

class IncreaseTimeoutBody(BaseModel):
    machine_id: str
    session_id: str
    timeout: int
    gpu: str
    
