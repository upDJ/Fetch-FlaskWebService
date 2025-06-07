from pydantic import Field
import math
import time

from app.models.base import ReceiptBase


class ReceiptModel(ReceiptBase):
    uid: str = Field(default="internal")
    points: int = Field(default=0)

    # get points from retailer name -> test for non-alpha numeric characters
    # 1pt for every alphanumeric character
    def calculate_retailer_points(self):
        alnum_retailer_name = ""
        for char in self.retailer:
            if char.isalnum():
                alnum_retailer_name += char
        retailer_points = len(alnum_retailer_name)
        return retailer_points

    # get points from purchase total
    # 50pts if the purchase total is a round dollar amount with no cents
    def calculate_purchase_total_round_points(self):
        purchase_round_total_points = 0
        _dollars, cents = self.purchase_total.split(".")
        purchase_is_round_total = int(cents) == 0

        if purchase_is_round_total:
            purchase_round_total_points = 50

        return purchase_round_total_points

    # get points from purchase total
    # 25pts if the total is a multiple of .25
    def calculate_purchase_total_multiple_of_points(self):
        purchase_multiple_total_points = 0
        purchase_is_multiple_of_25_cents = (float(self.purchase_total) % 0.25) == 0

        if purchase_is_multiple_of_25_cents:
            purchase_multiple_total_points += 25

        return purchase_multiple_total_points

    # get points from item count
    # 5pts for every two items on the receipt
    def calculate_item_count_points(self):
        num_of_items = len(self.items)
        item_pairs = math.floor(num_of_items / 2)
        item_count_points = item_pairs * 5
        return item_count_points

    # get points from item description -> for each item in list
    # pts = price * .2 and round up
    # if length of item description is multiple of three
    def calculate_item_desc_points(self):
        item_desc_points = 0
        for item in self.items:
            item_desc_len = len(item.short_description.strip())
            if item_desc_len % 3 == 0:
                item_desc_points += math.ceil(float(item.price) * 0.2)
        return item_desc_points

    # Example time.struct_time(tm_year=1900, tm_mon=1, tm_mday=1, tm_hour=13, tm_min=1, tm_sec=0, tm_wday=0, tm_yday=1, tm_isdst=-1)
    # get points from purchase date
    # 6pts if the day in the purchase date is odd
    def calculate_purchase_day_points(self):
        purchase_day_points = 0
        _year, _month, day = self.purchase_date.split("-")
        if int(day) % 2 != 0:  # day is odd
            purchase_day_points = 6
        return purchase_day_points

    # get points from the purchase time
    # 10pts if the time of purchase is after 2:00pm and before 4:00pm
    def calculate_purchase_time_points(self):
        purchase_time_points = 0
        start_time_window_obj = time.strptime("14:00", "%H:%M")
        end_window_window_obj = time.strptime("16:00", "%H:%M")
        purchase_time_obj = time.strptime(self.purchase_time, "%H:%M")
        if (
            purchase_time_obj > start_time_window_obj
            and purchase_time_obj < end_window_window_obj
        ):
            purchase_time_points += 10
        return purchase_time_points

    def calculate_points(self):
        retailer_points = self.calculate_retailer_points()
        purchase_total_round_points = self.calculate_purchase_total_round_points()
        purchase_total_multiple_of_points = (
            self.calculate_purchase_total_multiple_of_points()
        )
        item_count_points = self.calculate_item_count_points()
        purchase_time_points = self.calculate_purchase_time_points()
        item_desc_points = self.calculate_item_desc_points()
        purchase_day_points = self.calculate_purchase_day_points()

        total_points = sum(
            [
                retailer_points,
                purchase_total_round_points,
                purchase_total_multiple_of_points,
                item_count_points,
                purchase_time_points,
                item_desc_points,
                purchase_day_points,
            ]
        )
        return total_points
