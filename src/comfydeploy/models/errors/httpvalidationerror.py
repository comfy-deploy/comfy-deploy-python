"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from comfydeploy import utils
from comfydeploy.models.components import validationerror as components_validationerror
from comfydeploy.types import BaseModel
from typing import List, Optional


class HTTPValidationErrorData(BaseModel):
    detail: Optional[List[components_validationerror.ValidationError]] = None


class HTTPValidationError(Exception):
    data: HTTPValidationErrorData

    def __init__(self, data: HTTPValidationErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, HTTPValidationErrorData)
