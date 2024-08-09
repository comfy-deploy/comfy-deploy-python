"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from comfydeploy import utils
from comfydeploy.models.components import httpmetadata as components_httpmetadata
from comfydeploy.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated

class GetRunRunResponseBodyData(BaseModel):
    error: str
    http_meta: Annotated[Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)] = None
    


class GetRunRunResponseBody(Exception):
    r"""Error getting output"""
    data: GetRunRunResponseBodyData

    def __init__(self, data: GetRunRunResponseBodyData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, GetRunRunResponseBodyData)

class GetRunResponseBodyData(BaseModel):
    code: str
    message: str
    http_meta: Annotated[Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)] = None
    


class GetRunResponseBody(Exception):
    r"""Workflow not found"""
    data: GetRunResponseBodyData

    def __init__(self, data: GetRunResponseBodyData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, GetRunResponseBodyData)

