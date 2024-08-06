"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from comfydeploy.models.components import httpmetadata as components_httpmetadata
from comfydeploy.types import BaseModel
from comfydeploy.utils import FieldMetadata, QueryParamMetadata
from enum import Enum
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class Environment(str, Enum):
    PRODUCTION = "production"
    STAGING = "staging"

class GetDeploymentRequestTypedDict(TypedDict):
    environment: NotRequired[Environment]
    

class GetDeploymentRequest(BaseModel):
    environment: Annotated[Optional[Environment], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    

class GetDeploymentResponseBodyTypedDict(TypedDict):
    pass
    

class GetDeploymentResponseBody(BaseModel):
    pass
    

class GetDeploymentResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    response_bodies: NotRequired[List[GetDeploymentResponseBodyTypedDict]]
    r"""Display all production workflows"""
    

class GetDeploymentResponse(BaseModel):
    http_meta: Annotated[Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)] = None
    response_bodies: Optional[List[GetDeploymentResponseBody]] = None
    r"""Display all production workflows"""
    
