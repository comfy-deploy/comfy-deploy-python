"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from comfydeploy.models.components import httpmetadata as components_httpmetadata, runstream as components_runstream
from comfydeploy.types import BaseModel
import pydantic
from pydantic import SkipValidation
from typing import AsyncGenerator, Generator, Optional, TypedDict, Union
from typing_extensions import Annotated, NotRequired


class CreateRunDeploymentStreamRunDeploymentStreamPostResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    run_stream: NotRequired[Union[Generator[components_runstream.RunStreamTypedDict, None, None], AsyncGenerator[components_runstream.RunStreamTypedDict, None]]]
    r"""Stream of workflow run events"""
    

class CreateRunDeploymentStreamRunDeploymentStreamPostResponse(BaseModel):
    http_meta: Annotated[Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)] = None
    run_stream: SkipValidation[Optional[Union[Generator[components_runstream.RunStream, None, None], AsyncGenerator[components_runstream.RunStream, None]]]] = None
    r"""Stream of workflow run events"""
    
