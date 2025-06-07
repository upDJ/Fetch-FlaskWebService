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