"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from comfydeploy.models.components import (
    cancelfunctionbody as components_cancelfunctionbody,
    httpmetadata as components_httpmetadata,
)
from comfydeploy.types import BaseModel
from comfydeploy.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Any, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CancelRunRunRunIDCancelPostRequestTypedDict(TypedDict):
    run_id: str
    cancel_function_body: components_cancelfunctionbody.CancelFunctionBodyTypedDict


class CancelRunRunRunIDCancelPostRequest(BaseModel):
    run_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    cancel_function_body: Annotated[
        components_cancelfunctionbody.CancelFunctionBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class CancelRunRunRunIDCancelPostResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    any: NotRequired[Any]
    r"""Successful Response"""


class CancelRunRunRunIDCancelPostResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    any: Optional[Any] = None
    r"""Successful Response"""