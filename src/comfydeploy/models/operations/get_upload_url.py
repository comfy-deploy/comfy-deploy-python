"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from comfydeploy.models.components import httpmetadata as components_httpmetadata
from comfydeploy.types import BaseModel
from comfydeploy.utils import FieldMetadata, QueryParamMetadata
from enum import Enum
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class Type(str, Enum):
    IMAGE_PNG = "image/png"
    IMAGE_JPG = "image/jpg"
    IMAGE_JPEG = "image/jpeg"
    IMAGE_WEBP = "image/webp"
    VIDEO_MP4 = "video/mp4"
    VIDEO_WEBM = "video/webm"
    APPLICATION_OCTET_STREAM = "application/octet-stream"

class GetUploadURLRequestTypedDict(TypedDict):
    type: Type
    file_size: str
    

class GetUploadURLRequest(BaseModel):
    type: Annotated[Type, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))]
    file_size: Annotated[str, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))]
    

class GetUploadURLResponseBodyTypedDict(TypedDict):
    r"""Retrieve the output"""
    
    upload_url: str
    file_id: str
    download_url: str
    

class GetUploadURLResponseBody(BaseModel):
    r"""Retrieve the output"""
    
    upload_url: str
    file_id: str
    download_url: str
    

class GetUploadURLResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    object: NotRequired[GetUploadURLResponseBodyTypedDict]
    r"""Retrieve the output"""
    

class GetUploadURLResponse(BaseModel):
    http_meta: Annotated[Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)] = None
    object: Optional[GetUploadURLResponseBody] = None
    r"""Retrieve the output"""
    
