"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from comfydeploy.models.components import (
    httpmetadata as components_httpmetadata,
    session as components_session,
)
from comfydeploy.types import BaseModel
from comfydeploy.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetSessionSessionSessionIDGetRequestTypedDict(TypedDict):
    session_id: str


class GetSessionSessionSessionIDGetRequest(BaseModel):
    session_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]


class GetSessionSessionSessionIDGetResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    session: NotRequired[components_session.SessionTypedDict]
    r"""Successful Response"""


class GetSessionSessionSessionIDGetResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    session: Optional[components_session.Session] = None
    r"""Successful Response"""
