import pytest
from app import create_app


@pytest.fixture(scope="session")
def app():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )
    # setup
    yield app
    print("\n\nTearing down\n\n")
    # teardown


@pytest.fixture(scope="session")
def client(app):
    return app.test_client()


@pytest.fixture()
def receipt_uid(client):  # seed db with a receipt
    payload = {
        "retailer": "M&M Corner Market",
        "purchaseDate": "2022-03-20",
        "purchaseTime": "14:33",
        "items": [
            {"shortDescription": "Gatorade", "price": "2.25"},
            {"shortDescription": "Gatorade", "price": "2.25"},
            {"shortDescription": "Gatorade", "price": "2.25"},
            {"shortDescription": "Gatorade", "price": "2.25"},
        ],
        "total": "9.00",
    }

    response = client.post("/receipts/process", json=payload)
    uid = response.json["id"]
    return uid


def test_receipt_uid_not_null(receipt_uid):
    assert receipt_uid is not None


def test_receipt_uid_is_string(receipt_uid):
    assert type(receipt_uid) is str


def test_get_points(client, receipt_uid):
    response = client.get(f"receipts/{receipt_uid}/points")
    assert response.json["points"] == 109
