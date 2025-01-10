"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .modelsearchquery import ModelSearchQuery, ModelSearchQueryTypedDict
from comfydeploy.types import BaseModel
from typing import List, TypedDict


class SearchModelsResponseTypedDict(TypedDict):
    models: List[ModelSearchQueryTypedDict]
    

class SearchModelsResponse(BaseModel):
    models: List[ModelSearchQuery]
    
