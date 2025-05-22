from typing import Annotated
from pydantic import BaseModel, WithJsonSchema, Field
from app.schema import API_DOC_DICT


class ItemBase(BaseModel):
    short_description: Annotated[
        str,
        Field(strict=True, alias="shortDescription"),
        WithJsonSchema(API_DOC_DICT["Item"]["shortDescription"]),
    ]
    price: Annotated[
        str, Field(strict=True), WithJsonSchema(API_DOC_DICT["Item"]["price"])
    ]
