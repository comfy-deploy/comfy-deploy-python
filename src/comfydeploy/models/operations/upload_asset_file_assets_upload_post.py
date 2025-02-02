"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from comfydeploy.models.components import (
    assetresponse as components_assetresponse,
    body_upload_asset_file_assets_upload_post as components_body_upload_asset_file_assets_upload_post,
    httpmetadata as components_httpmetadata,
)
from comfydeploy.types import BaseModel
from comfydeploy.utils import FieldMetadata, QueryParamMetadata, RequestMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UploadAssetFileAssetsUploadPostRequestTypedDict(TypedDict):
    body_upload_asset_file_assets_upload_post: components_body_upload_asset_file_assets_upload_post.BodyUploadAssetFileAssetsUploadPostTypedDict
    parent_path: NotRequired[str]
    r"""Parent folder path"""


class UploadAssetFileAssetsUploadPostRequest(BaseModel):
    body_upload_asset_file_assets_upload_post: Annotated[
        components_body_upload_asset_file_assets_upload_post.BodyUploadAssetFileAssetsUploadPost,
        FieldMetadata(request=RequestMetadata(media_type="multipart/form-data")),
    ]

    parent_path: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = "/"
    r"""Parent folder path"""


class UploadAssetFileAssetsUploadPostResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    asset_response: NotRequired[components_assetresponse.AssetResponseTypedDict]
    r"""Successful Response"""


class UploadAssetFileAssetsUploadPostResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    asset_response: Optional[components_assetresponse.AssetResponse] = None
    r"""Successful Response"""
