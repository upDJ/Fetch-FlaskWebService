import pytest
from app.models import ReceiptDTO
from app.services import ReceiptService
from app.tests import fixture_list


@pytest.mark.parametrize("payload,expected_points,points", fixture_list)
def test_service_process_receipt(payload, expected_points, points):
    receipt_service = ReceiptService()
    receipt_dto = ReceiptDTO(**payload)
    receipt_uid = receipt_service.process_receipt(receipt_dto=receipt_dto)

    assert receipt_uid is not None


@pytest.mark.parametrize("payload,expected_points,points", fixture_list)
def test_service_get_points(payload, expected_points, points):
    receipt_service = ReceiptService()
    receipt_dto = ReceiptDTO(**payload)
    receipt_uid = receipt_service.process_receipt(receipt_dto=receipt_dto)

    points = receipt_service.get_points(receipt_uid)
    assert points == expected_points
