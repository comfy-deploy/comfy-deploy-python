"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .gpuprovidertype import GPUProviderType
from .machinegpu_output import MachineGPUOutput
from .workspacegpu import WorkspaceGPU
from comfydeploy.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from comfydeploy.utils import validate_const
from datetime import datetime
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GPUEventModelTypedDict(TypedDict):
    id: str
    user_id: str
    org_id: Nullable[str]
    machine_id: Nullable[str]
    start_time: Nullable[datetime]
    end_time: Nullable[datetime]
    gpu: Nullable[MachineGPUOutput]
    gpu_provider: GPUProviderType
    ws_gpu: Nullable[WorkspaceGPU]
    created_at: NotRequired[datetime]
    updated_at: NotRequired[datetime]
    session_timeout: NotRequired[Nullable[int]]
    session_id: NotRequired[Nullable[str]]
    modal_function_id: NotRequired[Nullable[str]]
    tunnel_url: NotRequired[Nullable[str]]
    cost_item_title: NotRequired[Nullable[str]]
    cost: NotRequired[Nullable[float]]


class GPUEventModel(BaseModel):
    id: str

    user_id: str

    org_id: Nullable[str]

    machine_id: Nullable[str]

    start_time: Nullable[datetime]

    end_time: Nullable[datetime]

    gpu: Nullable[MachineGPUOutput]

    gpu_provider: GPUProviderType

    WS_GPU: Annotated[
        Annotated[
            Nullable[WorkspaceGPU],
            AfterValidator(validate_const(WorkspaceGPU.FOUR_THOUSAND_AND_NINETY)),
        ],
        pydantic.Field(alias="ws_gpu"),
    ] = WorkspaceGPU.FOUR_THOUSAND_AND_NINETY

    created_at: Optional[datetime] = None

    updated_at: Optional[datetime] = None

    session_timeout: OptionalNullable[int] = UNSET

    session_id: OptionalNullable[str] = UNSET

    modal_function_id: OptionalNullable[str] = UNSET

    tunnel_url: OptionalNullable[str] = UNSET

    cost_item_title: OptionalNullable[str] = UNSET

    cost: OptionalNullable[float] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "created_at",
            "updated_at",
            "session_timeout",
            "session_id",
            "modal_function_id",
            "tunnel_url",
            "cost_item_title",
            "cost",
        ]
        nullable_fields = [
            "org_id",
            "machine_id",
            "start_time",
            "end_time",
            "gpu",
            "ws_gpu",
            "session_timeout",
            "session_id",
            "modal_function_id",
            "tunnel_url",
            "cost_item_title",
            "cost",
        ]
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
