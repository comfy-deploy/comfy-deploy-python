"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from comfydeploy.models.components import httpmetadata as components_httpmetadata
from comfydeploy.types import BaseModel
import comfydeploy.utils as utils
import pydantic
from typing import Optional
from typing_extensions import Annotated

class GetWebsocketDeploymentIDResponseBodyData(BaseModel):
    error: str
    http_meta: Annotated[Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)] = None
    


class GetWebsocketDeploymentIDResponseBody(Exception):
    r"""Error creating run"""
    data: GetWebsocketDeploymentIDResponseBodyData

    def __init__(self, data: GetWebsocketDeploymentIDResponseBodyData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, GetWebsocketDeploymentIDResponseBodyData)

