"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from comfydeploy.models.components import httpmetadata as components_httpmetadata
from comfydeploy.types import BaseModel, Nullable, UNSET_SENTINEL
from comfydeploy.utils import FieldMetadata, QueryParamMetadata
import pydantic
from pydantic import model_serializer
from typing import Any, List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GetV1WorkflowsRequestTypedDict(TypedDict):
    page: NotRequired[str]
    page_size: NotRequired[str]
    search: NotRequired[str]
    

class GetV1WorkflowsRequest(BaseModel):
    page: Annotated[Optional[str], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = "1"
    page_size: Annotated[Optional[str], pydantic.Field(alias="pageSize"), FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = "12"
    search: Annotated[Optional[str], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    

class UserTypedDict(TypedDict):
    name: str
    

class User(BaseModel):
    name: str
    

class VersionsTypedDict(TypedDict):
    id: str
    version: float
    

class Versions(BaseModel):
    id: str
    version: float
    

class GetV1WorkflowsResponseBodyTypedDict(TypedDict):
    id: str
    updated_at: str
    name: str
    selected_machine_id: Nullable[str]
    count: str
    user: UserTypedDict
    versions: List[VersionsTypedDict]
    deployments: List[Any]
    runs: List[Any]
    

class GetV1WorkflowsResponseBody(BaseModel):
    id: str
    updated_at: str
    name: str
    selected_machine_id: Nullable[str]
    count: str
    user: User
    versions: List[Versions]
    deployments: List[Any]
    runs: List[Any]
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["selected_machine_id"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
        

class GetV1WorkflowsResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    response_bodies: NotRequired[List[GetV1WorkflowsResponseBodyTypedDict]]
    r"""Workflows retrieved successfully"""
    

class GetV1WorkflowsResponse(BaseModel):
    http_meta: Annotated[Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)] = None
    response_bodies: Optional[List[GetV1WorkflowsResponseBody]] = None
    r"""Workflows retrieved successfully"""
    
