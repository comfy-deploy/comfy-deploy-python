"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from comfydeploy.models.components import (
    httpmetadata as components_httpmetadata,
    workflowrunwebhookresponse as components_workflowrunwebhookresponse,
)
from comfydeploy.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateRunWorkflowStreamRunWorkflowStreamPostRunUpdateRequestBodyWebhookPostResponseTypedDict(
    TypedDict
):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    workflow_run_webhook_response: NotRequired[
        components_workflowrunwebhookresponse.WorkflowRunWebhookResponseTypedDict
    ]
    r"""Successful Response"""


class CreateRunWorkflowStreamRunWorkflowStreamPostRunUpdateRequestBodyWebhookPostResponse(
    BaseModel
):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    workflow_run_webhook_response: Optional[
        components_workflowrunwebhookresponse.WorkflowRunWebhookResponse
    ] = None
    r"""Successful Response"""
