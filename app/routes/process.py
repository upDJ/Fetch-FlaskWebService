from flask import Blueprint, jsonify, request
from flask_pydantic_spec import Response, Request
from app.models import Receipt

process_bp = Blueprint("process", __name__)


def register_routes(api):
    @process_bp.route("/receipts/process", methods=["POST"])
    @api.validate(
        body=Request(Receipt), resp=Response(HTTP_200=None, HTTP_403=None), tags=["api"]
    )
    def process_receipt() -> Response:
        receipt = request.context.body
        receipt_id = receipt.save_receipt()

        return jsonify({"id": receipt_id})
