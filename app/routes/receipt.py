from flask import Blueprint, jsonify, request
from flask_pydantic_spec import Response, Request
from app.dto import ReceiptDTO
from app.models import ReceiptModel
from app.repositories import ReceiptRepository

receipt_bp = Blueprint("process", __name__)


def register_routes(api):
    @receipt_bp.route("/receipts/process", methods=["POST"])
    @api.validate(
        body=Request(ReceiptDTO),
        resp=Response(HTTP_200=None, HTTP_403=None),
        tags=["api"],
    )
    def process_receipt() -> Response:
        receipt_dto = request.context.body
        receipt_model = ReceiptModel.model_validate(
            receipt_dto.model_dump(by_alias=True)
        )  # pydantic serialization: dto -> model
        receipt_model.points = receipt_model.calculate_points()
        receipt_repository = ReceiptRepository()
        _, receipt_uid = receipt_repository.save_receipt(
            receipt=receipt_model.model_dump(by_alias=True)
        )
        return jsonify({"id": receipt_uid})

    @receipt_bp.route("/receipts/<string:id>/points", methods=["GET"])
    def get_points(**kwargs):
        search_id = kwargs["id"]
        receipt_repository = ReceiptRepository()
        _, receipt_model = receipt_repository.get_receipt_by_id(uid=search_id)
        return jsonify({"points": receipt_model.points})
