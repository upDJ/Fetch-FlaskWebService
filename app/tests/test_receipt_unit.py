import pytest
from app.models import ReceiptModel

fixture_list = [
    (
        {
            "retailer": "M&M Corner Market",
            "purchaseDate": "2022-03-20",
            "purchaseTime": "14:33",
            "items": [{"shortDescription": "Gatorade", "price": "2.25"}] * 4,
            "total": "9.00",
        },
        109,
        {
            "retailer": 14,
            "purchase_total_multiple": 25,
            "purchase_total_round": 50,
            "item_count": 10,
            "item_desc": 0,
            "purchase_date": 0,
            "purchase_time": 10,
        },
    ),
    (
        {
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
        },
        28,
        {
            "retailer": 6,
            "purchase_total_multiple": 0,
            "purchase_total_round": 0,
            "item_count": 10,
            "item_desc": 6,
            "purchase_date": 6,
            "purchase_time": 0,
        },
    ),
]


@pytest.mark.parametrize("payload,expected_points,points", fixture_list)
def test_receipt_calculate_retailer_points(payload, expected_points, points):
    receipt = ReceiptModel.model_validate(payload)
    retailer_points = receipt.calculate_retailer_points()
    assert points["retailer"] == retailer_points


@pytest.mark.parametrize("payload,expected_points,points", fixture_list)
def test_receipt_calculate_purchase_round_total_points(
    payload, expected_points, points
):
    receipt = ReceiptModel.model_validate(payload)
    purchase_total_points = receipt.calculate_purchase_total_round_points()
    assert points["purchase_total_round"] == purchase_total_points


@pytest.mark.parametrize("payload,expected_points,points", fixture_list)
def test_receipt_calculate_purchase_multiple_of_total_points(
    payload, expected_points, points
):
    receipt = ReceiptModel.model_validate(payload)
    purchase_total_points = receipt.calculate_purchase_total_multiple_of_points()
    assert points["purchase_total_multiple"] == purchase_total_points


@pytest.mark.parametrize("payload,expected_points,points", fixture_list)
def test_item_count_points(payload, expected_points, points):
    receipt = ReceiptModel.model_validate(payload)
    item_count_points = receipt.calculate_item_count_points()
    assert points["item_count"] == item_count_points


@pytest.mark.parametrize("payload,expected_points,points", fixture_list)
def test_calculate_item_desc_points(payload, expected_points, points):
    receipt = ReceiptModel.model_validate(payload)
    item_desc_points = receipt.calculate_item_desc_points()
    assert points["item_desc"] == item_desc_points


@pytest.mark.parametrize("payload,expected_points,points", fixture_list)
def test_calculate_purchase_day_points(payload, expected_points, points):
    receipt = ReceiptModel.model_validate(payload)
    purchase_day_points = receipt.calculate_purchase_day_points()
    assert points["purchase_date"] == purchase_day_points


@pytest.mark.parametrize("payload,expected_points,points", fixture_list)
def test_calculate_purchase_time_points(payload, expected_points, points):
    receipt = ReceiptModel.model_validate(payload)
    purchase_time_points = receipt.calculate_purchase_time_points()
    assert points["purchase_time"] == purchase_time_points


@pytest.mark.parametrize("payload,expected_points,points", fixture_list)
def test_receipt_calculate_points(payload, expected_points, points):
    receipt = ReceiptModel.model_validate(payload)
    points = receipt.calculate_points()
    assert points == expected_points
