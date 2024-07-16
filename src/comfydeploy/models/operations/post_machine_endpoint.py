"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from comfydeploy import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostMachineEndpointRequestBody:
    machine_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('machine_id') }})
    type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostMachineEndpointResponseBody:
    r"""Create short lived machine endpoint"""
    url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url') }})
    gpu: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gpu') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostMachineEndpointResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    object: Optional[PostMachineEndpointResponseBody] = dataclasses.field(default=None)
    r"""Create short lived machine endpoint"""
    
