"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from comfydeploy.models.components import httpmetadata as components_httpmetadata
from comfydeploy.types import BaseModel
from comfydeploy.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GetDeploymentIDInputsRequestTypedDict(TypedDict):
    id: str
    

class GetDeploymentIDInputsRequest(BaseModel):
    id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    

class ResponseBodyTypedDict(TypedDict):
    class_type: str
    input_id: str
    default_value: str
    min_value: float
    max_value: float
    

class ResponseBody(BaseModel):
    class_type: str
    input_id: str
    default_value: str
    min_value: float
    max_value: float
    

class GetDeploymentIDInputsResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    response_bodies: NotRequired[List[ResponseBodyTypedDict]]
    r"""Retrieve the output"""
    

class GetDeploymentIDInputsResponse(BaseModel):
    http_meta: Annotated[Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)] = None
    response_bodies: Optional[List[ResponseBody]] = None
    r"""Retrieve the output"""
    
