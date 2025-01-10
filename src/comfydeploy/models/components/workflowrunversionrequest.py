"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from comfydeploy.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from enum import Enum
from pydantic import model_serializer
from typing import Any, Dict, List, Optional, Union
from typing_extensions import NotRequired, TypeAliasType, TypedDict


WorkflowRunVersionRequestInputsTypedDict = TypeAliasType(
    "WorkflowRunVersionRequestInputsTypedDict", Union[str, int, float, bool, List[Any]]
)


WorkflowRunVersionRequestInputs = TypeAliasType(
    "WorkflowRunVersionRequestInputs", Union[str, int, float, bool, List[Any]]
)


class WorkflowRunVersionRequestGpu(str, Enum):
    r"""The GPU to override the machine's default GPU"""

    T4 = "T4"
    L4 = "L4"
    A10_G = "A10G"
    A100 = "A100"
    A100_80_GB = "A100-80GB"
    H100 = "H100"


class WorkflowRunVersionRequestTypedDict(TypedDict):
    workflow_version_id: str
    inputs: NotRequired[Dict[str, WorkflowRunVersionRequestInputsTypedDict]]
    r"""The inputs to the workflow"""
    webhook: NotRequired[str]
    webhook_intermediate_status: NotRequired[bool]
    gpu: NotRequired[WorkflowRunVersionRequestGpu]
    r"""The GPU to override the machine's default GPU"""
    machine_id: NotRequired[Nullable[str]]


class WorkflowRunVersionRequest(BaseModel):
    workflow_version_id: str

    inputs: Optional[Dict[str, WorkflowRunVersionRequestInputs]] = None
    r"""The inputs to the workflow"""

    webhook: Optional[str] = None

    webhook_intermediate_status: Optional[bool] = False

    gpu: Optional[WorkflowRunVersionRequestGpu] = None
    r"""The GPU to override the machine's default GPU"""

    machine_id: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "inputs",
            "webhook",
            "webhook_intermediate_status",
            "gpu",
            "machine_id",
        ]
        nullable_fields = ["machine_id"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
