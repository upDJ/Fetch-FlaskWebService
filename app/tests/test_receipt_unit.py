import pytest
from app.models import ReceiptModel
from app.tests import fixture_list


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
