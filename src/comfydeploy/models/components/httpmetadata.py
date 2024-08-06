"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from comfydeploy.types import BaseModel
import httpx
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated


class HTTPMetadataTypedDict(TypedDict):
    response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    request: httpx.Request
    r"""Raw HTTP request; suitable for debugging"""
    

class HTTPMetadata(BaseModel):
    response: Annotated[Optional[httpx.Response], pydantic.Field(exclude=True)] = None
    r"""Raw HTTP response; suitable for custom response parsing"""
    request: Annotated[Optional[httpx.Request], pydantic.Field(exclude=True)] = None
    r"""Raw HTTP request; suitable for debugging"""
    
