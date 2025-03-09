"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .deploymentenvironment import DeploymentEnvironment
from .inputmodel import InputModel, InputModelTypedDict
from .machinewithname import MachineWithName, MachineWithNameTypedDict
from .outputmodel import OutputModel, OutputModelTypedDict
from .workflowwithname import WorkflowWithName, WorkflowWithNameTypedDict
from comfydeploy.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from datetime import datetime
from pydantic import model_serializer
from typing import List
from typing_extensions import NotRequired, TypedDict


class ShareOptionsTypedDict(TypedDict):
    pass


class ShareOptions(BaseModel):
    pass


class ShowcaseMediaTypedDict(TypedDict):
    pass


class ShowcaseMedia(BaseModel):
    pass


class VersionTypedDict(TypedDict):
    pass


class Version(BaseModel):
    pass


class DeploymentModelTypedDict(TypedDict):
    id: str
    user_id: str
    org_id: Nullable[str]
    workflow_version_id: str
    workflow_id: str
    machine_id: str
    share_slug: Nullable[str]
    description: Nullable[str]
    share_options: Nullable[ShareOptionsTypedDict]
    showcase_media: Nullable[List[ShowcaseMediaTypedDict]]
    environment: DeploymentEnvironment
    created_at: datetime
    updated_at: datetime
    workflow: NotRequired[Nullable[WorkflowWithNameTypedDict]]
    version: NotRequired[Nullable[VersionTypedDict]]
    machine: NotRequired[Nullable[MachineWithNameTypedDict]]
    input_types: NotRequired[Nullable[List[InputModelTypedDict]]]
    output_types: NotRequired[Nullable[List[OutputModelTypedDict]]]
    dub_link: NotRequired[Nullable[str]]
    gpu: NotRequired[Nullable[str]]
    machine_version_id: NotRequired[Nullable[str]]
    modal_image_id: NotRequired[Nullable[str]]
    concurrency_limit: NotRequired[Nullable[int]]
    run_timeout: NotRequired[Nullable[int]]
    idle_timeout: NotRequired[Nullable[int]]
    keep_warm: NotRequired[Nullable[int]]
    activated_at: NotRequired[Nullable[datetime]]
    modal_app_id: NotRequired[Nullable[str]]


class DeploymentModel(BaseModel):
    id: str

    user_id: str

    org_id: Nullable[str]

    workflow_version_id: str

    workflow_id: str

    machine_id: str

    share_slug: Nullable[str]

    description: Nullable[str]

    share_options: Nullable[ShareOptions]

    showcase_media: Nullable[List[ShowcaseMedia]]

    environment: DeploymentEnvironment

    created_at: datetime

    updated_at: datetime

    workflow: OptionalNullable[WorkflowWithName] = UNSET

    version: OptionalNullable[Version] = UNSET

    machine: OptionalNullable[MachineWithName] = UNSET

    input_types: OptionalNullable[List[InputModel]] = UNSET

    output_types: OptionalNullable[List[OutputModel]] = UNSET

    dub_link: OptionalNullable[str] = UNSET

    gpu: OptionalNullable[str] = UNSET

    machine_version_id: OptionalNullable[str] = UNSET

    modal_image_id: OptionalNullable[str] = UNSET

    concurrency_limit: OptionalNullable[int] = UNSET

    run_timeout: OptionalNullable[int] = UNSET

    idle_timeout: OptionalNullable[int] = UNSET

    keep_warm: OptionalNullable[int] = UNSET

    activated_at: OptionalNullable[datetime] = UNSET

    modal_app_id: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "workflow",
            "version",
            "machine",
            "input_types",
            "output_types",
            "dub_link",
            "gpu",
            "machine_version_id",
            "modal_image_id",
            "concurrency_limit",
            "run_timeout",
            "idle_timeout",
            "keep_warm",
            "activated_at",
            "modal_app_id",
        ]
        nullable_fields = [
            "org_id",
            "share_slug",
            "description",
            "share_options",
            "showcase_media",
            "workflow",
            "version",
            "machine",
            "input_types",
            "output_types",
            "dub_link",
            "gpu",
            "machine_version_id",
            "modal_image_id",
            "concurrency_limit",
            "run_timeout",
            "idle_timeout",
            "keep_warm",
            "activated_at",
            "modal_app_id",
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
