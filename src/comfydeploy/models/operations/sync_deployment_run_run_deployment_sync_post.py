"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from comfydeploy.models.components import httpmetadata as components_httpmetadata, workflowrunoutputmodel as components_workflowrunoutputmodel
from comfydeploy.types import BaseModel
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class SyncDeploymentRunRunDeploymentSyncPostResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    response_sync_deployment_run_run_deployment_sync_post: NotRequired[List[components_workflowrunoutputmodel.WorkflowRunOutputModelTypedDict]]
    r"""Successful Response"""
    

class SyncDeploymentRunRunDeploymentSyncPostResponse(BaseModel):
    http_meta: Annotated[Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)] = None
    response_sync_deployment_run_run_deployment_sync_post: Optional[List[components_workflowrunoutputmodel.WorkflowRunOutputModel]] = None
    r"""Successful Response"""
    
