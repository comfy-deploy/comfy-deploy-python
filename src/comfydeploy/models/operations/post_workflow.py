"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from comfydeploy.models.components import httpmetadata as components_httpmetadata
from comfydeploy.types import BaseModel
from enum import Enum
import pydantic
from typing import Any, Dict, List, Optional, TypedDict, Union
from typing_extensions import Annotated, NotRequired


class WorkflowAPITypedDict(TypedDict):
    inputs: Dict[str, Any]
    class_type: NotRequired[str]
    

class WorkflowAPI(BaseModel):
    inputs: Dict[str, Any]
    class_type: Optional[str] = None
    

class GitCustomNodesTypedDict(TypedDict):
    hash: str
    disabled: bool
    

class GitCustomNodes(BaseModel):
    hash: str
    disabled: bool
    

class SnapshotTypedDict(TypedDict):
    comfyui: str
    git_custom_nodes: Dict[str, GitCustomNodesTypedDict]
    file_custom_nodes: List[Any]
    

class Snapshot(BaseModel):
    comfyui: str
    git_custom_nodes: Dict[str, GitCustomNodes]
    file_custom_nodes: List[Any]
    

class NodeTypedDict(TypedDict):
    inputs: Dict[str, Any]
    class_type: NotRequired[str]
    

class Node(BaseModel):
    inputs: Dict[str, Any]
    class_type: Optional[str] = None
    

class One(str, Enum):
    COPY = "copy"
    UNZIP = "unzip"
    GIT_CLONE = "git-clone"

InstallTypeTypedDict = Union[One, str]


InstallType = Union[One, str]


class CustomNodesTypedDict(TypedDict):
    name: str
    url: str
    node: NotRequired[List[NodeTypedDict]]
    hash: NotRequired[str]
    files: NotRequired[List[str]]
    install_type: NotRequired[InstallTypeTypedDict]
    warning: NotRequired[str]
    pip: NotRequired[List[str]]
    

class CustomNodes(BaseModel):
    name: str
    url: str
    node: Optional[List[Node]] = None
    hash: Optional[str] = None
    files: Optional[List[str]] = None
    install_type: Optional[InstallType] = None
    warning: Optional[str] = None
    pip: Optional[List[str]] = None
    

class ModelsTypedDict(TypedDict):
    name: str
    hash: NotRequired[str]
    url: NotRequired[str]
    

class Models(BaseModel):
    name: str
    hash: Optional[str] = None
    url: Optional[str] = None
    

class FilesTypedDict(TypedDict):
    name: str
    hash: NotRequired[str]
    url: NotRequired[str]
    

class Files(BaseModel):
    name: str
    hash: Optional[str] = None
    url: Optional[str] = None
    

class DependenciesTypedDict(TypedDict):
    comfyui: str
    missing_nodes: List[str]
    custom_nodes: Dict[str, CustomNodesTypedDict]
    models: Dict[str, List[ModelsTypedDict]]
    files: Dict[str, List[FilesTypedDict]]
    

class Dependencies(BaseModel):
    comfyui: str
    missing_nodes: List[str]
    custom_nodes: Dict[str, CustomNodes]
    models: Dict[str, List[Models]]
    files: Dict[str, List[Files]]
    

class PostWorkflowRequestBodyTypedDict(TypedDict):
    workflow_api: Dict[str, WorkflowAPITypedDict]
    snapshot: SnapshotTypedDict
    workflow_id: NotRequired[str]
    workflow_name: NotRequired[str]
    workflow: NotRequired[Any]
    dependencies: NotRequired[DependenciesTypedDict]
    

class PostWorkflowRequestBody(BaseModel):
    workflow_api: Dict[str, WorkflowAPI]
    snapshot: Snapshot
    workflow_id: Optional[str] = None
    workflow_name: Optional[str] = None
    workflow: Optional[Any] = None
    dependencies: Optional[Dependencies] = None
    

class PostWorkflowResponseBodyTypedDict(TypedDict):
    r"""Retrieve the output"""
    
    workflow_id: str
    version: str
    

class PostWorkflowResponseBody(BaseModel):
    r"""Retrieve the output"""
    
    workflow_id: str
    version: str
    

class PostWorkflowResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    object: NotRequired[PostWorkflowResponseBodyTypedDict]
    r"""Retrieve the output"""
    

class PostWorkflowResponse(BaseModel):
    http_meta: Annotated[Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)] = None
    object: Optional[PostWorkflowResponseBody] = None
    r"""Retrieve the output"""
    
