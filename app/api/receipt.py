from flask import Blueprint, jsonify, request
from flask_pydantic_spec import Response, Request
from app.models import ReceiptDTO
from app.services import ReceiptService

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
        receipt_service = ReceiptService()
        receipt_uid = receipt_service.process_receipt(receipt_dto)
        return jsonify({"id": receipt_uid})

    @receipt_bp.route("/receipts/<string:id>/points", methods=["GET"])
    def get_points(**kwargs) -> Response:
        search_id = kwargs["id"]
        receipt_service = ReceiptService()
        points = receipt_service.get_points(search_id)
        return jsonify({"points": points})
