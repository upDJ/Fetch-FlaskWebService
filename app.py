from flask import Flask, request, jsonify
from typing import Annotated
from pydantic import BaseModel, WithJsonSchema, Field, PrivateAttr
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request

app = Flask(__name__)

api = FlaskPydanticSpec("flask", title="Fetch Backend Challenge")
api.register(app)


@app.route("/")
def test():
    return "Testing"


RECEIPT_SCHEMA = {
    "retailer": "Target",
    "purchaseDate": "2022-01-01",
    "purchaseTime": "13:01",
    "items": [
        {"shortDescription": "Mountain Dew 12PK", "price": "6.49"},
        {"shortDescription": "Emils Cheese Pizza", "price": "12.25"},
        {"shortDescription": "Knorr Creamy Chicken", "price": "1.26"},
        {"shortDescription": "Doritos Nacho Cheese", "price": "3.35"},
        {"shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ", "price": "12.00"},
    ],
    "total": "35.35",
}

API_DOC_DICT = {
    "Receipt": {
        "id": {
            "description": "Unique ID assigned to receipt upon upload",
            "accessLevel": "Private",
            "type": "string",
            "pattern": "",
            "example": "1234",
        },
        "retailer": {
            "description": "The name of the retailer or store the receipt is from.",
            "type": "string",
            "pattern": "^[\\w\\s\\-&]+$",
            "example": "M&M Corner Market",
        },
        "purchaseDate": {
            "description": "The date of the purchase printed on the receipt.",
            "type": "string",
            "format": "date",
            "example": "2022-01-01",
        },
        "purchaseTime": {
            "description": "The time of the purchase printed on the receipt. 24-hour time expected.",
            "type": "string",
            "format": "time",
            "example": "13:01",
        },
        "items": {
            "type": "array",
            "minItems": "1",
            "items": {
                "type": "object",
                "description": "Object representation of item in receipt.",
                "$ref": "#/components/schemas/Item",
            },
        },
        "total": {
            "description": "The total amount paid on the receipt.",
            "type": "string",
            "pattern": "^\\d+\\.\\d{2}$",
            "example": "6.49",
        },
    },
    "Item": {
        "shortDescription": {
            "description": "The Short Product Description for the item.",
            "type": "string",
            "pattern": "^[\\w\\s\\-]+$",
            "example": "Mountain Dew 12PK",
        },
        "price": {
            "description": "The total price payed for this item.",
            "type": "string",
            "pattern": "^\\d+\\.\\d{2}$",
            "example": "6.49",
        },
    },
}

RECEIPT_DICT = {}
RECEIPT_ID = "0"
# create db module
def store_receipt(json_receipt: str):
    global RECEIPT_ID
    global RECEIPT_DICT

    RECEIPT_ID = f"{int(RECEIPT_ID) + 1}"
    RECEIPT_DICT[RECEIPT_ID] = {"data": json_receipt}

    return RECEIPT_ID


class Item(BaseModel):
    short_description: Annotated[str, Field(strict=True, alias="shortDescription"), WithJsonSchema(API_DOC_DICT["Item"]["shortDescription"])]
    price: Annotated[str, Field(strict=True), WithJsonSchema(API_DOC_DICT["Item"]["price"])]


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

    


@app.route("/receipts/process", methods=["POST"])
@api.validate(
    body=Request(Receipt), resp=Response(HTTP_200=None, HTTP_403=None), tags=["api"]
)
def process_recipt():
    receipt: Receipt = request.context.body
    receipt_id = receipt.save_receipt()

    return jsonify({"id": receipt_id})


if __name__ == "__main__":
    app.run(debug=True)  # maybe add env option?
