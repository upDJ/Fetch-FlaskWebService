from app.db import RECEIPT_DICT, RECEIPT_ID


def store_receipt(json_receipt: str):
    global RECEIPT_ID
    global RECEIPT_DICT

    RECEIPT_ID = f"{int(RECEIPT_ID) + 1}"
    RECEIPT_DICT[RECEIPT_ID] = {"data": json_receipt}

    return RECEIPT_ID
