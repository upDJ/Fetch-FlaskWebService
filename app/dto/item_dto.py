from .item_base import ItemBase
from app.schema import ITEM_SCHEMA


class ItemDTO(ItemBase):
    class Config:
        json_schema_extra = ITEM_SCHEMA
