from app.models import ReceiptDTO
from app.models import ReceiptModel
from app.repositories import ReceiptRepository


class ReceiptService:
    def __init__(self):
        self.receipt_repository = ReceiptRepository()

    def process_receipt(self, receipt_dto: ReceiptDTO) -> str:
        # pydantic serialization: dto -> model
        receipt_model = ReceiptModel.model_validate(
            receipt_dto.model_dump(by_alias=True)
        )
        receipt_model.points = receipt_model.calculate_points()
        _, receipt_uid = self.receipt_repository.save_receipt(
            receipt=receipt_model.model_dump(by_alias=True)
        )
        return receipt_uid

    def get_points(self, search_id: str) -> int:
        _, receipt_model = self.receipt_repository.get_receipt_by_id(uid=search_id)
        return receipt_model.points
