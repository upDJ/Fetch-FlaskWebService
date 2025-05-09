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


# seed db with a receipt
def test_process_receipt(client):
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
    assert response.json["id"] == "1"


def test_get_points(client):
    receipt_id = "1"

    response = client.get(f"receipts/{receipt_id}/points")
    assert response.json["points"] == 109
