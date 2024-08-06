"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from comfydeploy.models.components import httpmetadata as components_httpmetadata
from comfydeploy.types import BaseModel
import comfydeploy.utils as utils
import pydantic
from typing import Optional
from typing_extensions import Annotated

class PostMachineEndpointResponseBodyData(BaseModel):
    error: str
    http_meta: Annotated[Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)] = None
    


class PostMachineEndpointResponseBody(Exception):
    r"""Error creating run"""
    data: PostMachineEndpointResponseBodyData

    def __init__(self, data: PostMachineEndpointResponseBodyData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, PostMachineEndpointResponseBodyData)

