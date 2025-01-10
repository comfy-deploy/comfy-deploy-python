"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from comfydeploy.types import BaseModel
from enum import Enum
from typing import Any, Dict, List, Optional, Union
from typing_extensions import NotRequired, TypeAliasType, TypedDict


ModelRunRequestInputsTypedDict = TypeAliasType(
    "ModelRunRequestInputsTypedDict", Union[str, int, float, bool, List[Any]]
)


ModelRunRequestInputs = TypeAliasType(
    "ModelRunRequestInputs", Union[str, int, float, bool, List[Any]]
)


class ModelRunRequestGpu(str, Enum):
    r"""The GPU to override the machine's default GPU"""

    T4 = "T4"
    L4 = "L4"
    A10_G = "A10G"
    A100 = "A100"
    A100_80_GB = "A100-80GB"
    H100 = "H100"


class ModelRunRequestTypedDict(TypedDict):
    model_id: str
    inputs: NotRequired[Dict[str, ModelRunRequestInputsTypedDict]]
    r"""The inputs to the workflow"""
    webhook: NotRequired[str]
    webhook_intermediate_status: NotRequired[bool]
    gpu: NotRequired[ModelRunRequestGpu]
    r"""The GPU to override the machine's default GPU"""


class ModelRunRequest(BaseModel):
    model_id: str

    inputs: Optional[Dict[str, ModelRunRequestInputs]] = None
    r"""The inputs to the workflow"""

    webhook: Optional[str] = None

    webhook_intermediate_status: Optional[bool] = False

    gpu: Optional[ModelRunRequestGpu] = None
    r"""The GPU to override the machine's default GPU"""
