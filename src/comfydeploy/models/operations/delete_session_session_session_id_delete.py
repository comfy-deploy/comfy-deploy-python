"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from comfydeploy.models.components import (
    deletesessionresponse as components_deletesessionresponse,
    httpmetadata as components_httpmetadata,
)
from comfydeploy.types import BaseModel
from comfydeploy.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class DeleteSessionSessionSessionIDDeleteRequestTypedDict(TypedDict):
    session_id: str


class DeleteSessionSessionSessionIDDeleteRequest(BaseModel):
    session_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]


class DeleteSessionSessionSessionIDDeleteResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    delete_session_response: NotRequired[
        components_deletesessionresponse.DeleteSessionResponseTypedDict
    ]
    r"""Successful Response"""


class DeleteSessionSessionSessionIDDeleteResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    delete_session_response: Optional[
        components_deletesessionresponse.DeleteSessionResponse
    ] = None
    r"""Successful Response"""