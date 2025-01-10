"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from comfydeploy.types import BaseModel
from enum import Enum
from typing_extensions import TypedDict


class ModelOutputClassType(str, Enum):
    COMFY_DEPLOY_STD_OUTPUT_IMAGE = "ComfyDeployStdOutputImage"
    COMFY_DEPLOY_STD_OUTPUT_ANY = "ComfyDeployStdOutputAny"


class ModelOutputTypedDict(TypedDict):
    class_type: ModelOutputClassType
    output_id: str


class ModelOutput(BaseModel):
    class_type: ModelOutputClassType

    output_id: str
