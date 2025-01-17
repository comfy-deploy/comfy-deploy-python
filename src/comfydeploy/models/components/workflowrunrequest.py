"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from comfydeploy.types import BaseModel
from enum import Enum
from typing import Any, Dict, List, Optional, Union
from typing_extensions import NotRequired, TypeAliasType, TypedDict


WorkflowRunRequestInputsTypedDict = TypeAliasType(
    "WorkflowRunRequestInputsTypedDict", Union[str, int, float, bool, List[Any]]
)


WorkflowRunRequestInputs = TypeAliasType(
    "WorkflowRunRequestInputs", Union[str, int, float, bool, List[Any]]
)


class WorkflowRunRequestGpu(str, Enum):
    r"""The GPU to override the machine's default GPU"""

    T4 = "T4"
    L4 = "L4"
    A10_G = "A10G"
    L40_S = "L40S"
    A100 = "A100"
    A100_80_GB = "A100-80GB"
    H100 = "H100"


class WorkflowAPIJSONTypedDict(TypedDict):
    pass


class WorkflowAPIJSON(BaseModel):
    pass


class WorkflowTypedDict(TypedDict):
    pass


class Workflow(BaseModel):
    pass


class WorkflowRunRequestTypedDict(TypedDict):
    workflow_id: str
    workflow_api_json: WorkflowAPIJSONTypedDict
    inputs: NotRequired[Dict[str, WorkflowRunRequestInputsTypedDict]]
    r"""The inputs to the workflow"""
    webhook: NotRequired[str]
    webhook_intermediate_status: NotRequired[bool]
    gpu: NotRequired[WorkflowRunRequestGpu]
    r"""The GPU to override the machine's default GPU"""
    workflow: NotRequired[WorkflowTypedDict]
    machine_id: NotRequired[str]


class WorkflowRunRequest(BaseModel):
    workflow_id: str

    workflow_api_json: WorkflowAPIJSON

    inputs: Optional[Dict[str, WorkflowRunRequestInputs]] = None
    r"""The inputs to the workflow"""

    webhook: Optional[str] = None

    webhook_intermediate_status: Optional[bool] = False

    gpu: Optional[WorkflowRunRequestGpu] = None
    r"""The GPU to override the machine's default GPU"""

    workflow: Optional[Workflow] = None

    machine_id: Optional[str] = None
