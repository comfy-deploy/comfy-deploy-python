"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from comfydeploy.models.components import (
    assetresponse as components_assetresponse,
    httpmetadata as components_httpmetadata,
)
from comfydeploy.types import BaseModel
from comfydeploy.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ListAssetsAssetsGetRequestTypedDict(TypedDict):
    path: NotRequired[str]
    r"""Folder path to list items from"""


class ListAssetsAssetsGetRequest(BaseModel):
    path: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = "/"
    r"""Folder path to list items from"""


class ListAssetsAssetsGetResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    response_list_assets_assets_get: NotRequired[
        List[components_assetresponse.AssetResponseTypedDict]
    ]
    r"""Successful Response"""


class ListAssetsAssetsGetResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    response_list_assets_assets_get: Optional[
        List[components_assetresponse.AssetResponse]
    ] = None
    r"""Successful Response"""
