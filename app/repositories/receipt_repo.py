from app.db import DbContext
from app.models import ReceiptModel


class ReceiptRepository:
    def __init__(self):
        self.db = DbContext()

    def save_receipt(self, receipt):
        receipt_dict = receipt
        response_code, uid = self.db.create(receipt_dict)

        return response_code, uid

    def get_receipt_by_id(self, uid):
        id_dict = {"uid": uid}
        response_code, receipt_dict = self.db.query(**id_dict)

        if receipt_dict is None:
            return response_code, None

        receipt_dict["uid"] = uid
        print(receipt_dict)
        receipt = ReceiptModel.model_validate(receipt_dict)

        return response_code, receipt
