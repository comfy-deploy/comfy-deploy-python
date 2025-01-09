"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from comfydeploy.models.components import httpmetadata as components_httpmetadata
from comfydeploy.types import BaseModel, Nullable, UNSET_SENTINEL
from comfydeploy.utils import FieldMetadata, QueryParamMetadata
from enum import Enum
import pydantic
from pydantic import model_serializer
from typing import List, Optional, TypedDict, Union
from typing_extensions import Annotated, NotRequired


class Environment(str, Enum):
    PRODUCTION = "production"
    STAGING = "staging"

class GetDeploymentRequestTypedDict(TypedDict):
    environment: NotRequired[Environment]
    

class GetDeploymentRequest(BaseModel):
    environment: Annotated[Optional[Environment], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    

class GetDeploymentClassType(str, Enum):
    COMFY_UI_DEPLOY_EXTERNAL_TEXT = "ComfyUIDeployExternalText"
    COMFY_UI_DEPLOY_EXTERNAL_TEXT_ANY = "ComfyUIDeployExternalTextAny"
    COMFY_UI_DEPLOY_EXTERNAL_TEXT_SINGLE_LINE = "ComfyUIDeployExternalTextSingleLine"
    COMFY_UI_DEPLOY_EXTERNAL_IMAGE = "ComfyUIDeployExternalImage"
    COMFY_UI_DEPLOY_EXTERNAL_IMAGE_ALPHA = "ComfyUIDeployExternalImageAlpha"
    COMFY_UI_DEPLOY_EXTERNAL_NUMBER = "ComfyUIDeployExternalNumber"
    COMFY_UI_DEPLOY_EXTERNAL_NUMBER_INT = "ComfyUIDeployExternalNumberInt"
    COMFY_UI_DEPLOY_EXTERNAL_LORA = "ComfyUIDeployExternalLora"
    COMFY_UI_DEPLOY_EXTERNAL_CHECKPOINT = "ComfyUIDeployExternalCheckpoint"
    COMFY_DEPLOY_WEBSCOKET_IMAGE_INPUT = "ComfyDeployWebscoketImageInput"
    COMFY_UI_DEPLOY_EXTERNAL_IMAGE_BATCH = "ComfyUIDeployExternalImageBatch"
    COMFY_UI_DEPLOY_EXTERNAL_VIDEO = "ComfyUIDeployExternalVideo"
    COMFY_UI_DEPLOY_EXTERNAL_BOOLEAN = "ComfyUIDeployExternalBoolean"
    COMFY_UI_DEPLOY_EXTERNAL_NUMBER_SLIDER = "ComfyUIDeployExternalNumberSlider"
    COMFY_UI_DEPLOY_EXTERNAL_NUMBER_SLIDER_INT = "ComfyUIDeployExternalNumberSliderInt"
    COMFY_UI_DEPLOY_EXTERNAL_ENUM = "ComfyUIDeployExternalEnum"
    COMFY_UI_DEPLOY_EXTERNAL_COLOR = "ComfyUIDeployExternalColor"

GetDeploymentDefaultValueTypedDict = Union[str, float]


GetDeploymentDefaultValue = Union[str, float]


class InputsDefinitionTypedDict(TypedDict):
    class_type: GetDeploymentClassType
    input_id: str
    default_value: GetDeploymentDefaultValueTypedDict
    min_value: NotRequired[float]
    max_value: NotRequired[float]
    display_name: NotRequired[str]
    description: NotRequired[str]
    enum_values: NotRequired[List[str]]
    

class InputsDefinition(BaseModel):
    class_type: GetDeploymentClassType
    input_id: str
    default_value: GetDeploymentDefaultValue
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    display_name: Optional[str] = None
    description: Optional[str] = None
    enum_values: Optional[List[str]] = None
    

class GetDeploymentResponseBodyTypedDict(TypedDict):
    deployment_id: str
    name: str
    inputs_definition: Nullable[List[InputsDefinitionTypedDict]]
    

class GetDeploymentResponseBody(BaseModel):
    deployment_id: str
    name: str
    inputs_definition: Nullable[List[InputsDefinition]]
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["inputs_definition"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
        

class GetDeploymentResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    response_bodies: NotRequired[List[GetDeploymentResponseBodyTypedDict]]
    r"""Display all production workflows"""
    

class GetDeploymentResponse(BaseModel):
    http_meta: Annotated[Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)] = None
    response_bodies: Optional[List[GetDeploymentResponseBody]] = None
    r"""Display all production workflows"""
    
