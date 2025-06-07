from app.models.base import ReceiptBase
from app.schema import RECEIPT_SCHEMA


class ReceiptDTO(ReceiptBase):
    class Config:
        json_schema_extra = RECEIPT_SCHEMA
