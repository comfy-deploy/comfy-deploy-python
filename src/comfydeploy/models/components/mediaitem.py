"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from comfydeploy.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing_extensions import NotRequired, TypedDict


class MediaItemTypedDict(TypedDict):
    url: str
    type: str
    filename: str
    is_public: NotRequired[Nullable[bool]]
    subfolder: NotRequired[Nullable[str]]
    upload_duration: NotRequired[Nullable[float]]


class MediaItem(BaseModel):
    url: str

    type: str

    filename: str

    is_public: OptionalNullable[bool] = UNSET

    subfolder: OptionalNullable[str] = UNSET

    upload_duration: OptionalNullable[float] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["is_public", "subfolder", "upload_duration"]
        nullable_fields = ["is_public", "subfolder", "upload_duration"]
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
