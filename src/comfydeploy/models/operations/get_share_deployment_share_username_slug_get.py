"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from comfydeploy.models.components import (
    deploymentsharemodel as components_deploymentsharemodel,
    httpmetadata as components_httpmetadata,
)
from comfydeploy.types import BaseModel
from comfydeploy.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetShareDeploymentShareUsernameSlugGetRequestTypedDict(TypedDict):
    username: str
    slug: str


class GetShareDeploymentShareUsernameSlugGetRequest(BaseModel):
    username: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    slug: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]


class GetShareDeploymentShareUsernameSlugGetResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    deployment_share_model: NotRequired[
        components_deploymentsharemodel.DeploymentShareModelTypedDict
    ]
    r"""Successful Response"""


class GetShareDeploymentShareUsernameSlugGetResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    deployment_share_model: Optional[
        components_deploymentsharemodel.DeploymentShareModel
    ] = None
    r"""Successful Response"""
