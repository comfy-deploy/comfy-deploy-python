"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from comfydeploy import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import List, Optional


class QueryParamRunOrigin(str, Enum):
    MANUAL = 'manual'
    API = 'api'
    PUBLIC_SHARE = 'public-share'
    PUBLIC_TEMPLATE = 'public-template'
    WORKSPACE = 'workspace'


@dataclasses.dataclass
class GetV1WorkflowsWorkflowIDOutputsRequest:
    workflow_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'workflow_id', 'style': 'simple', 'explode': False }})
    page: Optional[str] = dataclasses.field(default='1', metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    page_size: Optional[str] = dataclasses.field(default='12', metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    search: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'search', 'style': 'form', 'explode': True }})
    run_origin: Optional[QueryParamRunOrigin] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'runOrigin', 'style': 'form', 'explode': True }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Outputs:
    file_ur_ls: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fileURLs') }})
    run_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('runID') }})
    duration: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('duration') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetV1WorkflowsWorkflowIDOutputsResponseBody:
    r"""Specific workflow retrieved successfully"""
    outputs: List[Outputs] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('outputs') }})
    total: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetV1WorkflowsWorkflowIDOutputsResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    object: Optional[GetV1WorkflowsWorkflowIDOutputsResponseBody] = dataclasses.field(default=None)
    r"""Specific workflow retrieved successfully"""
    

