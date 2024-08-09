"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from comfydeploy import utils
from comfydeploy.models.components import httpmetadata as components_httpmetadata
from comfydeploy.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated

class GetV1WorkflowsWorkflowIDOutputsResponseBodyData(BaseModel):
    error: str
    http_meta: Annotated[Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)] = None
    


class GetV1WorkflowsWorkflowIDOutputsResponseBody(Exception):
    r"""Error in retrieving the specific workflow"""
    data: GetV1WorkflowsWorkflowIDOutputsResponseBodyData

    def __init__(self, data: GetV1WorkflowsWorkflowIDOutputsResponseBodyData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, GetV1WorkflowsWorkflowIDOutputsResponseBodyData)

