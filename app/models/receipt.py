from typing import Annotated
from pydantic import BaseModel, WithJsonSchema, Field, PrivateAttr
from app.models import Item
from app.schema import API_DOC_DICT, RECEIPT_SCHEMA
from app.db import store_receipt


class Receipt(BaseModel):
    retailer: Annotated[
        str, Field(strict=True), WithJsonSchema(API_DOC_DICT["Receipt"]["retailer"])
    ]
    purchase_date: Annotated[
        str,
        Field(strict=True, alias="purchaseDate"),
        WithJsonSchema(API_DOC_DICT["Receipt"]["purchaseDate"]),
    ]
    purchase_time: Annotated[
        str,
        Field(strict=True, alias="purchaseTime"),
        WithJsonSchema(API_DOC_DICT["Receipt"]["purchaseTime"]),
    ]
    items: list[Item]
    total: Annotated[
        str, Field(strict=True), WithJsonSchema(API_DOC_DICT["Receipt"]["total"])
    ]

    # Private Variables - Instance Use Only
    _id: str = PrivateAttr()

    def save_receipt(self):
        self._id = store_receipt(self.model_dump_json())
        return self._id

    class Config:
        json_schema_extra = RECEIPT_SCHEMA
