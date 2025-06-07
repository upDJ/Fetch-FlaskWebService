from typing import Annotated
from pydantic import BaseModel, WithJsonSchema, Field
from .item_base import ItemBase
from typing import List
from app.schema import API_DOC_DICT


# alias is not working as expected. during model_dump its dumping the actual variable name rathere than the alias name
# total
#   Field required [type=missing, input_value={'retailer': 'M&M Corner ...purchase_total': '6.49'}, input_type=dict]
#     For further information visit https://errors.pydantic.dev/2.11/v/missing
class ReceiptBase(BaseModel):
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
    items: List[ItemBase]
    purchase_total: Annotated[
        str,
        Field(strict=True, alias="total"),
        WithJsonSchema(API_DOC_DICT["Receipt"]["total"]),
    ]
