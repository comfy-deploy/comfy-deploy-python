"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from comfydeploy.models.components import httpmetadata as components_httpmetadata
from comfydeploy.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from enum import Enum
import pydantic
from pydantic import model_serializer
from typing import Any, Dict, Optional, TypedDict, Union
from typing_extensions import Annotated, NotRequired


class Gpu(str, Enum):
    T4 = "T4"
    L4 = "L4"
    A10_G = "A10G"
    A100 = "A100"
    H100 = "H100"

class RunOrigin(str, Enum):
    MANUAL = "manual"
    API = "api"
    PUBLIC_SHARE = "public-share"
    PUBLIC_TEMPLATE = "public-template"
    WORKSPACE = "workspace"

class PostRunRequestBodyTypedDict(TypedDict):
    r"""Run options"""
    
    deployment_id: NotRequired[str]
    r"""Deployment ID to run"""
    workflow_api: NotRequired[Nullable[Any]]
    r"""Workflow API JSON to run"""
    workflow_api_json: NotRequired[str]
    r"""Workflow API JSON to run"""
    workflow_id: NotRequired[str]
    r"""Workflow ID to run"""
    machine_id: NotRequired[str]
    gpu: NotRequired[Gpu]
    concurrency_limit: NotRequired[float]
    private_volume_name: NotRequired[str]
    timeout: NotRequired[float]
    run_origin: NotRequired[RunOrigin]
    inputs: NotRequired[Dict[str, InputsTypedDict]]
    r"""External inputs to the workflow"""
    inputs_json: NotRequired[str]
    r"""External inputs to the workflow in JSON format"""
    webhook: NotRequired[str]
    r"""Webhook URL to receive workflow updates"""
    stream: NotRequired[bool]
    r"""Whether to return a streaming url"""
    batch_number: NotRequired[float]
    r"""Batch number to run"""
    

class PostRunRequestBody(BaseModel):
    r"""Run options"""
    
    deployment_id: Optional[str] = None
    r"""Deployment ID to run"""
    workflow_api: OptionalNullable[Any] = UNSET
    r"""Workflow API JSON to run"""
    workflow_api_json: Optional[str] = None
    r"""Workflow API JSON to run"""
    workflow_id: Optional[str] = None
    r"""Workflow ID to run"""
    machine_id: Optional[str] = None
    gpu: Optional[Gpu] = None
    concurrency_limit: Optional[float] = None
    private_volume_name: Optional[str] = None
    timeout: Optional[float] = None
    run_origin: Optional[RunOrigin] = None
    inputs: Optional[Dict[str, Inputs]] = None
    r"""External inputs to the workflow"""
    inputs_json: Optional[str] = None
    r"""External inputs to the workflow in JSON format"""
    webhook: Optional[str] = None
    r"""Webhook URL to receive workflow updates"""
    stream: Optional[bool] = None
    r"""Whether to return a streaming url"""
    batch_number: Optional[float] = 1
    r"""Batch number to run"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["deployment_id", "workflow_api", "workflow_api_json", "workflow_id", "machine_id", "gpu", "concurrency_limit", "private_volume_name", "timeout", "run_origin", "inputs", "inputs_json", "webhook", "stream", "batch_number"]
        nullable_fields = ["workflow_api"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields
                or (
                    k in optional_fields
                    and k in nullable_fields
                    and (
                        self.__pydantic_fields_set__.intersection({n})
                        or k in null_default_fields
                    )  # pylint: disable=no-member
                )
            ):
                m[k] = val

        return m
        

class PostRunResponseBodyTypedDict(TypedDict):
    r"""Workflow queued"""
    
    run_id: str
    

class PostRunResponseBody(BaseModel):
    r"""Workflow queued"""
    
    run_id: str
    

class PostRunResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    object: NotRequired[PostRunResponseBodyTypedDict]
    r"""Workflow queued"""
    

class PostRunResponse(BaseModel):
    http_meta: Annotated[Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)] = None
    object: Optional[PostRunResponseBody] = None
    r"""Workflow queued"""
    

InputsTypedDict = Union[str, float]


Inputs = Union[str, float]

