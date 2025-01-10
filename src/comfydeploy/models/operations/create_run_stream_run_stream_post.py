"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from comfydeploy.models.components import deploymentrunrequest as components_deploymentrunrequest, httpmetadata as components_httpmetadata, modelrunrequest as components_modelrunrequest, runstream as components_runstream, workflowrunrequest as components_workflowrunrequest, workflowrunversionrequest as components_workflowrunversionrequest
from comfydeploy.types import BaseModel
import pydantic
from pydantic import SkipValidation
from typing import AsyncGenerator, Generator, Optional, TypedDict, Union
from typing_extensions import Annotated, NotRequired


CreateRunStreamRunStreamPostDataTypedDict = Union[components_deploymentrunrequest.DeploymentRunRequestTypedDict, components_modelrunrequest.ModelRunRequestTypedDict, components_workflowrunversionrequest.WorkflowRunVersionRequestTypedDict, components_workflowrunrequest.WorkflowRunRequestTypedDict]


CreateRunStreamRunStreamPostData = Union[components_deploymentrunrequest.DeploymentRunRequest, components_modelrunrequest.ModelRunRequest, components_workflowrunversionrequest.WorkflowRunVersionRequest, components_workflowrunrequest.WorkflowRunRequest]


class CreateRunStreamRunStreamPostResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    run_stream: NotRequired[Union[Generator[components_runstream.RunStreamTypedDict, None, None], AsyncGenerator[components_runstream.RunStreamTypedDict, None]]]
    r"""Stream of workflow run events"""
    

class CreateRunStreamRunStreamPostResponse(BaseModel):
    http_meta: Annotated[Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)] = None
    run_stream: SkipValidation[Optional[Union[Generator[components_runstream.RunStream, None, None], AsyncGenerator[components_runstream.RunStream, None]]]] = None
    r"""Stream of workflow run events"""
    
