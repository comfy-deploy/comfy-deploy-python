"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from comfydeploy.models.components import (
    httpmetadata as components_httpmetadata,
    snapshotsessionbody as components_snapshotsessionbody,
)
from comfydeploy.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from comfydeploy.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from pydantic import model_serializer
from typing import Any, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SnapshotSessionSessionSessionIDSnapshotPostRequestTypedDict(TypedDict):
    session_id: str
    snapshot_session_body: NotRequired[
        Nullable[components_snapshotsessionbody.SnapshotSessionBodyTypedDict]
    ]


class SnapshotSessionSessionSessionIDSnapshotPostRequest(BaseModel):
    session_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    snapshot_session_body: Annotated[
        OptionalNullable[components_snapshotsessionbody.SnapshotSessionBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["SnapshotSessionBody"]
        nullable_fields = ["SnapshotSessionBody"]
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


class SnapshotSessionSessionSessionIDSnapshotPostResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    any: NotRequired[Any]
    r"""Successful Response"""


class SnapshotSessionSessionSessionIDSnapshotPostResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    any: Optional[Any] = None
    r"""Successful Response"""
